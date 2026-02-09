@echo off
echo ========================================
echo Image Authenticity Detector Setup
echo ========================================

echo.
echo [1/5] Installing Yarn globally...
call npm install -g yarn

echo.
echo [2/5] Setting up Backend...
cd backend
python -m venv venv
call venv\Scripts\activate
pip install -r requirements.txt
pip install emergentintegrations --extra-index-url https://d33sy5i8bnduwe.cloudfront.net/simple/
cd ..

echo.
echo [3/5] Setting up Frontend...
cd frontend
call yarn install
cd ..

echo.
echo [4/5] Creating environment files...
echo MONGO_URL=mongodb://localhost:27017 > backend\.env
echo DB_NAME=test_database >> backend\.env
echo CORS_ORIGINS=* >> backend\.env
echo EMERGENT_LLM_KEY=sk-emergent-aAf2546B027360d1e4 >> backend\.env

echo REACT_APP_BACKEND_URL=http://localhost:8001 > frontend\.env

echo.
echo [5/5] Setup Complete!
echo.
echo ========================================
echo NEXT STEPS:
echo ========================================
echo 1. Make sure MongoDB is running
echo 2. Run: start-app.bat
echo 3. Open: http://localhost:3000
echo ========================================
echo.
echo Ready to go! Using FREE Emergent LLM credits.
echo.
pause