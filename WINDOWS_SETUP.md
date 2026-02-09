# Windows Local Setup - Quick Start Guide

## Prerequisites (One-time Installation)
1. **Node.js** (v18+): https://nodejs.org/
2. **Python** (v3.9+): https://www.python.org/ ✅ Check "Add to PATH"
3. **MongoDB**: https://www.mongodb.com/try/download/community
4. **Git Bash** (optional, for easier commands): https://git-scm.com/

---

## 🚀 AUTOMATED SETUP (Recommended)

### Option 1: Using setup.bat (Windows)

**Step 1:** Create `setup.bat` in project root folder:
```batch
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
echo 1. Start MongoDB (if not running as service)
echo 2. Run: start-app.bat
echo ========================================
pause
```

**Step 2:** Double-click `setup.bat` to install everything!

---

### Option 2: Using start-app.bat (Run the App)

**Create `start-app.bat` in project root:**
```batch
@echo off
echo Starting Image Authenticity Detector...

echo.
echo Starting Backend Server...
start cmd /k "cd backend && venv\Scripts\activate && uvicorn server:app --host 0.0.0.0 --port 8001 --reload"

echo.
echo Waiting 5 seconds for backend to start...
timeout /t 5 /nobreak

echo.
echo Starting Frontend Server...
start cmd /k "cd frontend && yarn start"

echo.
echo ========================================
echo App will open at: http://localhost:3000
echo Backend API: http://localhost:8001/api/
echo ========================================
echo.
echo Press any key to stop all servers...
pause

taskkill /F /FI "WindowTitle eq *uvicorn*"
taskkill /F /FI "WindowTitle eq *yarn*"
```

---

## 📝 MANUAL SETUP (Alternative)

### Step 1: Install Backend Dependencies

```cmd
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
pip install emergentintegrations --extra-index-url https://d33sy5i8bnduwe.cloudfront.net/simple/
```

### Step 2: Install Frontend Dependencies

```cmd
cd frontend
npm install -g yarn
yarn install
```

### Step 3: Create Environment Files

**backend/.env:**
```
MONGO_URL=mongodb://localhost:27017
DB_NAME=test_database
CORS_ORIGINS=*
EMERGENT_LLM_KEY=sk-emergent-aAf2546B027360d1e4
```

**frontend/.env:**
```
REACT_APP_BACKEND_URL=http://localhost:8001
```

### Step 4: Start MongoDB

**Option A - Windows Service (Auto-starts):**
```cmd
net start MongoDB
```

**Option B - Manual Start:**
```cmd
"C:\Program Files\MongoDB\Server\7.0\bin\mongod.exe"
```

### Step 5: Run Backend (Terminal 1)

```cmd
cd backend
venv\Scripts\activate
uvicorn server:app --host 0.0.0.0 --port 8001 --reload
```

### Step 6: Run Frontend (Terminal 2)

```cmd
cd frontend
yarn start
```

---

## ✅ Verify Installation

1. Backend: http://localhost:8001/api/
   - Should show: `{"message":"Hello World"}`

2. Frontend: http://localhost:3000
   - Should show the image upload interface

3. Test: Upload an image and click ANALYZE
   - Should get FAKE/REAL verdict using **FREE** Emergent LLM credits

---

## 🔧 Troubleshooting

### "emergentintegrations not found"
```cmd
cd backend
venv\Scripts\activate
pip install emergentintegrations --extra-index-url https://d33sy5i8bnduwe.cloudfront.net/simple/ --force-reinstall
```

### "MongoDB connection failed"
```cmd
net start MongoDB
```

### Port already in use
```cmd
# Kill backend (8001)
netstat -ano | findstr :8001
taskkill /PID <PID_NUMBER> /F

# Kill frontend (3000)
netstat -ano | findstr :3000
taskkill /PID <PID_NUMBER> /F
```

### Python virtual environment issues
- Delete `backend/venv` folder
- Run setup again

---

## 💰 Cost Information

✅ **COMPLETELY FREE** - Uses Emergent LLM Key (Free Credits)
- No OpenAI API key needed
- No credit card required
- Pre-configured key included: `sk-emergent-aAf2546B027360d1e4`

---

## 📁 File Structure

```
project-root/
├── setup.bat              ← Run this first (automated setup)
├── start-app.bat          ← Run this to start app
├── backend/
│   ├── server.py          ← Main backend code
│   ├── requirements.txt   ← Python dependencies (AUTO INSTALL)
│   ├── .env              ← Environment variables (AUTO CREATED)
│   └── venv/             ← Virtual environment (AUTO CREATED)
└── frontend/
    ├── src/
    │   ├── App.js        ← Main React component
    │   ├── App.css       ← Styles
    │   ├── index.js      ← Entry point
    │   └── index.css     ← Global styles
    ├── package.json      ← Node dependencies (AUTO INSTALL)
    └── .env              ← Environment variables (AUTO CREATED)
```

---

## 🎯 Quick Commands Reference

```cmd
# Setup (one time)
setup.bat

# Start app
start-app.bat

# Or manually:
# Terminal 1
cd backend && venv\Scripts\activate && uvicorn server:app --host 0.0.0.0 --port 8001 --reload

# Terminal 2
cd frontend && yarn start
```

---

## 🌐 Alternative: No Local Setup Required!

Your app is already deployed and working online:
**Preview URL:** Check your Emergent dashboard for the live link!

---

**Need Help?** All dependencies auto-install from:
- `backend/requirements.txt` → Python packages
- `frontend/package.json` → Node packages
