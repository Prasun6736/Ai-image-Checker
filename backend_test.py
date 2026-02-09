import requests
import sys
import base64
from datetime import datetime
import json
import io
from PIL import Image
import numpy as np

class ImageDetectionAPITester:
    def __init__(self, base_url="https://authenticity-scan-4.preview.emergentagent.com"):
        self.base_url = base_url
        self.tests_run = 0
        self.tests_passed = 0

    def run_test(self, name, method, endpoint, expected_status, data=None):
        """Run a single API test"""
        url = f"{self.base_url}/{endpoint}"
        headers = {'Content-Type': 'application/json'}

        self.tests_run += 1
        print(f"\n🔍 Testing {name}...")
        
        try:
            if method == 'GET':
                response = requests.get(url, headers=headers, timeout=30)
            elif method == 'POST':
                response = requests.post(url, json=data, headers=headers, timeout=30)

            success = response.status_code == expected_status
            if success:
                self.tests_passed += 1
                print(f"✅ Passed - Status: {response.status_code}")
                if response.status_code == 200:
                    try:
                        json_response = response.json()
                        print(f"📄 Response: {json.dumps(json_response, indent=2)}")
                        return True, json_response
                    except:
                        print(f"📄 Response: {response.text}")
                        return True, response.text
            else:
                print(f"❌ Failed - Expected {expected_status}, got {response.status_code}")
                try:
                    error_detail = response.json()
                    print(f"📄 Error Response: {json.dumps(error_detail, indent=2)}")
                except:
                    print(f"📄 Error Response: {response.text}")

            return success, response.json() if success else {}

        except Exception as e:
            print(f"❌ Failed - Error: {str(e)}")
            return False, {}

    def create_test_image(self, width=300, height=300, format='JPEG'):
        """Create a test image with visual features"""
        # Create an image with patterns and features (not solid color)
        img_array = np.zeros((height, width, 3), dtype=np.uint8)
        
        # Add gradient background
        for i in range(height):
            for j in range(width):
                img_array[i, j] = [
                    int(255 * (i / height)),  # Red gradient
                    int(255 * (j / width)),   # Green gradient
                    128                       # Blue constant
                ]
        
        # Add some geometric shapes for features
        # Add a rectangle
        cv_start_x, cv_start_y = width//4, height//4
        cv_end_x, cv_end_y = 3*width//4, 3*height//4
        img_array[cv_start_y:cv_end_y, cv_start_x:cv_end_x] = [255, 255, 255]
        
        # Add a smaller colored rectangle inside
        cv_start_x2, cv_start_y2 = width//3, height//3
        cv_end_x2, cv_end_y2 = 2*width//3, 2*height//3
        img_array[cv_start_y2:cv_end_y2, cv_start_x2:cv_end_x2] = [255, 0, 0]
        
        # Convert to PIL Image
        img = Image.fromarray(img_array)
        
        # Convert to base64
        buffer = io.BytesIO()
        img.save(buffer, format=format)
        img_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
        
        return f"data:image/{format.lower()};base64,{img_base64}"

    def test_root_endpoint(self):
        """Test root API endpoint"""
        success, response = self.run_test(
            "Root API Endpoint",
            "GET", 
            "api/",
            200
        )
        return success

    def test_status_endpoints(self):
        """Test status check endpoints"""
        # Test creating status check
        test_data = {
            "client_name": f"test_client_{datetime.now().strftime('%H%M%S')}"
        }
        
        success, response = self.run_test(
            "Create Status Check",
            "POST",
            "api/status",
            200,
            data=test_data
        )
        
        if success:
            # Test getting status checks
            success2, _ = self.run_test(
                "Get Status Checks",
                "GET",
                "api/status", 
                200
            )
            return success and success2
        
        return success

    def test_image_analysis_valid(self):
        """Test image analysis with valid image"""
        print(f"\n🖼️ Creating test image with visual features...")
        test_image_base64 = self.create_test_image()
        
        test_data = {
            "image_base64": test_image_base64
        }
        
        success, response = self.run_test(
            "Image Analysis - Valid Image",
            "POST",
            "api/analyze-image",
            200,
            data=test_data
        )
        
        if success and response:
            # Validate response structure
            required_fields = ['verdict', 'confidence', 'details']
            missing_fields = [field for field in required_fields if field not in response]
            
            if missing_fields:
                print(f"❌ Response missing required fields: {missing_fields}")
                return False
            
            # Validate verdict is FAKE or REAL
            if response['verdict'] not in ['FAKE', 'REAL']:
                print(f"❌ Invalid verdict: {response['verdict']}")
                return False
            
            # Validate confidence is between 0-100
            confidence = response['confidence']
            if not isinstance(confidence, (int, float)) or confidence < 0 or confidence > 100:
                print(f"❌ Invalid confidence score: {confidence}")
                return False
            
            print(f"✅ Valid response structure:")
            print(f"   - Verdict: {response['verdict']}")
            print(f"   - Confidence: {response['confidence']}%")
            print(f"   - Details length: {len(response['details'])} chars")
            
        return success

    def test_image_analysis_invalid_data(self):
        """Test image analysis with invalid data"""
        # Test with invalid base64 data
        test_data = {
            "image_base64": "invalid_base64_data"
        }
        
        success, response = self.run_test(
            "Image Analysis - Invalid Base64",
            "POST",
            "api/analyze-image",
            500,
            data=test_data
        )
        
        # For this test, we expect it to fail (500 error), so success means we got the expected error
        return success

    def test_image_analysis_missing_data(self):
        """Test image analysis with missing image data"""
        test_data = {}
        
        success, response = self.run_test(
            "Image Analysis - Missing Data",
            "POST", 
            "api/analyze-image",
            422,  # FastAPI validation error
            data=test_data
        )
        
        return success

def main():
    print("🚀 Starting Image Detection API Tests...")
    print("=" * 50)
    
    tester = ImageDetectionAPITester()
    
    # Test sequence
    tests = [
        ("Root API Endpoint", tester.test_root_endpoint),
        ("Status Check Endpoints", tester.test_status_endpoints),
        ("Valid Image Analysis", tester.test_image_analysis_valid),
        ("Invalid Base64 Data", tester.test_image_analysis_invalid_data),
        ("Missing Image Data", tester.test_image_analysis_missing_data),
    ]
    
    print(f"📋 Running {len(tests)} test categories...")
    
    for test_name, test_func in tests:
        print(f"\n{'='*50}")
        print(f"🧪 Test Category: {test_name}")
        print(f"{'='*50}")
        
        try:
            result = test_func()
            if not result:
                print(f"⚠️  {test_name} failed")
        except Exception as e:
            print(f"❌ {test_name} crashed: {str(e)}")
            tester.tests_run += 1  # Count crashed tests

    # Print final results
    print(f"\n{'='*50}")
    print(f"📊 FINAL RESULTS")
    print(f"{'='*50}")
    print(f"✅ Tests passed: {tester.tests_passed}")
    print(f"❌ Tests failed: {tester.tests_run - tester.tests_passed}")  
    print(f"📈 Total tests: {tester.tests_run}")
    print(f"📊 Success rate: {(tester.tests_passed/tester.tests_run*100):.1f}%" if tester.tests_run > 0 else "No tests run")
    
    return 0 if tester.tests_passed == tester.tests_run else 1

if __name__ == "__main__":
    sys.exit(main())