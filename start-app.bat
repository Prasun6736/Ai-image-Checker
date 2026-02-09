@echo off
title Image Authenticity Detector Launcher
echo ========================================
echo Starting Image Authenticity Detector
echo ========================================

echo.
echo [1/3] Checking MongoDB...
net start MongoDB 2>nul
if errorlevel 1 (
    echo MongoDB service not found. Make sure MongoDB is installed.
    echo Download from: https://www.mongodb.com/try/download/community
    echo.
)

echo.
echo [2/3] Starting Backend Server...
start "Backend - FastAPI" cmd /k "cd backend && venv\Scripts\activate && echo Backend running on http://localhost:8001 && echo API Docs: http://localhost:8001/docs && uvicorn server:app --host 0.0.0.0 --port 8001 --reload"

echo Waiting 5 seconds for backend to initialize...
timeout /t 5 /nobreak >nul

echo.
echo [3/3] Starting Frontend Server...
start "Frontend - React" cmd /k "cd frontend && echo Frontend running on http://localhost:3000 && yarn start"

echo.
echo ========================================
echo ✅ App Started Successfully!
echo ========================================
echo Frontend: http://localhost:3000
echo Backend:  http://localhost:8001/api/
echo.
echo Using FREE Emergent LLM credits (no API key needed)
echo ========================================
echo.
echo Press any key to STOP all servers...
pause >nul

echo.
echo Stopping servers...
taskkill /F /FI "WindowTitle eq Backend - FastAPI*" 2>nul
taskkill /F /FI "WindowTitle eq Frontend - React*" 2>nul
echo.
echo All servers stopped.
pause