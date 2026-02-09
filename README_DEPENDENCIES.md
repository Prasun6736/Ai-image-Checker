# Dependency Files - Auto Installation Guide

## 📦 Dependency Files Location

### Backend Dependencies
**File:** `/backend/requirements.txt`
**Location:** Store in the `backend` folder

```
fastapi==0.110.1
uvicorn==0.25.0
motor==3.3.1
python-dotenv==1.2.1
pydantic==2.12.5
starlette==0.37.2
emergentintegrations==0.1.0
```

**Install command:**
```cmd
cd backend
pip install -r requirements.txt
pip install emergentintegrations --extra-index-url https://d33sy5i8bnduwe.cloudfront.net/simple/
```

---

### Frontend Dependencies
**File:** `/frontend/package.json`
**Location:** Store in the `frontend` folder

Already exists with all React, Radix UI, and Tailwind dependencies.

**Install command:**
```cmd
cd frontend
yarn install
```

---

## 🚀 Automated Installation Options

### Option 1: One-Click Setup (Easiest)

1. **Download all project files**
2. **Run setup.bat** (double-click in Windows)
   - Installs all backend dependencies
   - Installs all frontend dependencies
   - Creates .env files
   - Ready to use!

3. **Run start-app.bat** to launch

---

### Option 2: PowerShell Script

Create `setup.ps1`:

```powershell
Write-Host "Installing Backend Dependencies..." -ForegroundColor Green
Set-Location backend
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
pip install emergentintegrations --extra-index-url https://d33sy5i8bnduwe.cloudfront.net/simple/
Set-Location ..

Write-Host "Installing Frontend Dependencies..." -ForegroundColor Green
Set-Location frontend
npm install -g yarn
yarn install
Set-Location ..

Write-Host "Setup Complete!" -ForegroundColor Green
```

Run:
```powershell
powershell -ExecutionPolicy Bypass -File setup.ps1
```

---

### Option 3: Git Bash / WSL

Create `setup.sh`:

```bash
#!/bin/bash

echo "[1/3] Setting up Backend..."
cd backend
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt
pip install emergentintegrations --extra-index-url https://d33sy5i8bnduwe.cloudfront.net/simple/
cd ..

echo "[2/3] Setting up Frontend..."
cd frontend
yarn install
cd ..

echo "[3/3] Creating .env files..."
cat > backend/.env << EOF
MONGO_URL=mongodb://localhost:27017
DB_NAME=test_database
CORS_ORIGINS=*
EMERGENT_LLM_KEY=sk-emergent-aAf2546B027360d1e4
EOF

cat > frontend/.env << EOF
REACT_APP_BACKEND_URL=http://localhost:8001
EOF

echo "✅ Setup Complete!"
```

Run:
```bash
bash setup.sh
```

---

## 📋 What Gets Installed?

### Backend (Python)
- **FastAPI**: Web framework
- **Uvicorn**: ASGI server
- **Motor**: Async MongoDB driver
- **Pydantic**: Data validation
- **python-dotenv**: Environment variables
- **emergentintegrations**: AI integration library (FREE credits)

### Frontend (Node.js)
- **React 19**: UI framework
- **Radix UI**: Component library
- **Tailwind CSS**: Styling
- **Lucide React**: Icons
- **Axios**: HTTP client
- **Sonner**: Toast notifications

---

## 💡 Extra Configuration Needed

### 1. Environment Variables (AUTO CREATED by setup.bat)

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

### 2. MongoDB

**Option A - Install locally:**
- Download: https://www.mongodb.com/try/download/community
- Runs automatically as Windows service

**Option B - Use MongoDB Atlas (Cloud, FREE):**
1. Sign up: https://www.mongodb.com/cloud/atlas
2. Create free cluster
3. Get connection string
4. Update `backend/.env`:
   ```
   MONGO_URL=mongodb+srv://username:password@cluster.mongodb.net/
   ```

### 3. Required Folders (AUTO CREATED)
- `backend/venv/` - Python virtual environment
- `frontend/node_modules/` - Node packages

---

## ✅ Verification Steps

```cmd
# 1. Check Python
python --version
# Should show: Python 3.9+

# 2. Check Node
node --version
# Should show: v18+

# 3. Check MongoDB
net start MongoDB
# Should show: service is running

# 4. Check dependencies installed
cd backend && venv\Scripts\activate && pip list
cd frontend && yarn list
```

---

## 🎯 Quick Start Summary

```
1. Install Prerequisites:
   ✅ Python 3.9+
   ✅ Node.js 18+
   ✅ MongoDB

2. Run Auto Setup:
   ✅ Double-click: setup.bat
   
3. Start App:
   ✅ Double-click: start-app.bat
   
4. Open Browser:
   ✅ http://localhost:3000
```

---

## 💰 Cost Breakdown

| Item | Cost |
|------|------|
| Python packages | **FREE** |
| Node packages | **FREE** |
| MongoDB | **FREE** (Community Edition) |
| Emergent LLM Key | **FREE** (Pre-configured credits) |
| **TOTAL** | **$0.00** |

✅ No API keys to buy
✅ No subscriptions
✅ No credit card needed

---

## 🔍 Dependency Details

### Why emergentintegrations needs special install?

It's a custom library hosted on Emergent's private repository:

```cmd
pip install emergentintegrations --extra-index-url https://d33sy5i8bnduwe.cloudfront.net/simple/
```

This library provides:
- Unified API for OpenAI, Anthropic, Gemini
- Free credits via Emergent LLM Key
- No need for individual API keys

---

## 🛠️ Troubleshooting

### "pip not found"
- Add Python to PATH:
  - Windows Search → "Environment Variables"
  - Edit PATH
  - Add: `C:\Users\YourName\AppData\Local\Programs\Python\Python311`

### "yarn not found"
```cmd
npm install -g yarn
```

### "emergentintegrations install fails"
```cmd
pip install emergentintegrations --extra-index-url https://d33sy5i8bnduwe.cloudfront.net/simple/ --force-reinstall --no-cache-dir
```

### Permission errors
- Run Command Prompt as Administrator
- Or use: `pip install --user -r requirements.txt`

---

**That's it!** All dependencies will install automatically. Just run `setup.bat` and you're ready to go! 🚀
