from fastapi import FastAPI, APIRouter, HTTPException
from dotenv import load_dotenv
from starlette.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient
import os
import logging
from pathlib import Path
from pydantic import BaseModel, Field, ConfigDict
from typing import List
import uuid
from datetime import datetime, timezone
from emergentintegrations.llm.chat import LlmChat, UserMessage, ImageContent
import base64
import re

ROOT_DIR = Path(__file__).parent
load_dotenv(ROOT_DIR / '.env')

# MongoDB connection
mongo_url = os.environ.get('MONGO_URL')
client = AsyncIOMotorClient(mongo_url)
db = client[os.environ.get('DB_NAME')]

# Create the main app without a prefix
app = FastAPI()

# Create a router with the /api prefix
api_router = APIRouter(prefix="/api")

# Define Models
class StatusCheck(BaseModel):
    model_config = ConfigDict(extra="ignore")
    
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    client_name: str
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class StatusCheckCreate(BaseModel):
    client_name: str

class ImageAnalysisRequest(BaseModel):
    image_base64: str

class ImageAnalysisResponse(BaseModel):
    verdict: str
    confidence: float
    details: str

# Add your routes to the router instead of directly to app
@api_router.get("/")
async def root():
    return {"message": "Hello World"}

@api_router.post("/status", response_model=StatusCheck)
async def create_status_check(input: StatusCheckCreate):
    status_dict = input.model_dump()
    status_obj = StatusCheck(**status_dict)
    
    doc = status_obj.model_dump()
    doc['timestamp'] = doc['timestamp'].isoformat()
    
    _ = await db.status_checks.insert_one(doc)
    return status_obj

@api_router.get("/status", response_model=List[StatusCheck])
async def get_status_checks():
    status_checks = await db.status_checks.find({}, {"_id": 0}).to_list(1000)
    
    for check in status_checks:
        if isinstance(check['timestamp'], str):
            check['timestamp'] = datetime.fromisoformat(check['timestamp'])
    
    return status_checks

@api_router.post("/analyze-image", response_model=ImageAnalysisResponse)
async def analyze_image(request: ImageAnalysisRequest):
    try:
        # Get API key from environment
        api_key = os.environ.get('EMERGENT_LLM_KEY')
        if not api_key:
            raise HTTPException(status_code=500, detail="API key not configured")
        
        # Remove data URL prefix if present
        base64_data = request.image_base64
        if 'base64,' in base64_data:
            base64_data = base64_data.split('base64,')[1]
        
        # Initialize LLM Chat with OpenAI GPT-5.2
        chat = LlmChat(
            api_key=api_key,
            session_id=f"analysis-{uuid.uuid4()}",
            system_message="You are an expert image forensics analyst. Analyze images to determine if they are fake (AI-generated, manipulated, deepfake) or real (authentic photograph). Provide a confidence score between 0-100 and detailed reasoning."
        ).with_model("openai", "gpt-5.2")
        
        # Create image content
        image_content = ImageContent(image_base64=base64_data)
        
        # Create analysis prompt
        prompt = """Analyze this image and determine if it is FAKE or REAL.
        
FAKE includes:
- AI-generated images
- Deepfakes
- Heavily manipulated/photoshopped images
- Synthetic images

REAL includes:
- Authentic photographs
- Unaltered or minimally edited photos
- Natural camera captures

Provide your response in this exact format:
VERDICT: [FAKE or REAL]
CONFIDENCE: [0-100]
REASONING: [Brief explanation of why you made this determination]"""
        
        # Send message with image
        user_message = UserMessage(
            text=prompt,
            file_contents=[image_content]
        )
        
        response = await chat.send_message(user_message)
        
        # Parse response
        verdict = "UNCERTAIN"
        confidence = 50.0
        details = response
        
        # Extract verdict
        verdict_match = re.search(r'VERDICT:\s*(FAKE|REAL)', response, re.IGNORECASE)
        if verdict_match:
            verdict = verdict_match.group(1).upper()
        
        # Extract confidence
        confidence_match = re.search(r'CONFIDENCE:\s*(\d+)', response)
        if confidence_match:
            confidence = float(confidence_match.group(1))
        
        # Extract reasoning
        reasoning_match = re.search(r'REASONING:\s*(.+)', response, re.DOTALL)
        if reasoning_match:
            details = reasoning_match.group(1).strip()
        
        # Store analysis in database
        analysis_doc = {
            "id": str(uuid.uuid4()),
            "verdict": verdict,
            "confidence": confidence,
            "details": details,
            "timestamp": datetime.now(timezone.utc).isoformat()
        }
        await db.image_analyses.insert_one(analysis_doc)
        
        return ImageAnalysisResponse(
            verdict=verdict,
            confidence=confidence,
            details=details
        )
        
    except Exception as e:
        logging.error(f"Error analyzing image: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Analysis failed: {str(e)}")

# Include the router in the main app
app.include_router(api_router)

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=os.environ.get('CORS_ORIGINS', '*').split(','),
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@app.on_event("shutdown")
async def shutdown_db_client():
    client.close()