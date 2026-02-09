# 🚀 QUICK START - Windows Local Setup

## ⚡ Super Fast Setup (3 Steps)

### Step 1: Install Prerequisites (One-time only)

Download and install these 3 things:

1. **Python** → https://www.python.org/downloads/
   - ✅ CHECK "Add Python to PATH" during installation!

2. **Node.js** → https://nodejs.org/
   - Download LTS version (v18 or higher)

3. **MongoDB** → https://www.mongodb.com/try/download/community
   - Choose Windows version
   - Install with default settings

---

### Step 2: Auto Install Everything

1. **Download** all project files to a folder (e.g., `C:\image-detector`)

2. **Double-click** `setup.bat`
   - This installs ALL dependencies automatically!
   - Takes 2-3 minutes
   - Creates environment files
   - Sets up FREE AI credits

---

### Step 3: Run the App

1. **Double-click** `start-app.bat`
   - Opens 2 windows (backend + frontend)
   - App opens automatically in browser!
   - URL: http://localhost:3000

2. **Upload an image** and click ANALYZE!

---

## 📁 What Files Do You Need?

```
your-project-folder/
├── setup.bat              ⭐ RUN THIS FIRST
├── start-app.bat          ⭐ RUN THIS TO START
├── backend/
│   ├── server.py
│   ├── requirements.txt   📦 Dependencies auto-install
│   └── .env              🔐 Auto-created with FREE key
└── frontend/
    ├── src/
    ├── package.json       📦 Dependencies auto-install
    └── .env              🔐 Auto-created
```

---

## 💰 Cost: $0.00 (FREE!)

✅ Uses **FREE** Emergent LLM credits (pre-configured)  
✅ No API keys needed  
✅ No credit card required  
✅ No subscriptions  

The app is ready to use with FREE AI image analysis!

---

## 🎯 What Each File Does

| File | What It Does |
|------|--------------|
| `setup.bat` | Installs Python packages + Node packages + Creates .env files |
| `start-app.bat` | Starts backend server + frontend server + Opens browser |
| `backend/requirements.txt` | Lists Python dependencies (FastAPI, MongoDB, AI library) |
| `frontend/package.json` | Lists Node dependencies (React, UI components) |
| `backend/.env` | Contains FREE AI key + MongoDB settings |
| `frontend/.env` | Contains backend URL |

---

## ⚙️ Alternative: Manual Setup

If batch files don't work, use these commands:

### Install Backend:
```cmd
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
pip install emergentintegrations --extra-index-url https://d33sy5i8bnduwe.cloudfront.net/simple/
```

### Install Frontend:
```cmd
cd frontend
npm install -g yarn
yarn install
```

### Start Backend:
```cmd
cd backend
venv\Scripts\activate
uvicorn server:app --host 0.0.0.0 --port 8001 --reload
```

### Start Frontend (new terminal):
```cmd
cd frontend
yarn start
```

---

## ✅ How to Verify It's Working

1. **Backend Test**
   - Open: http://localhost:8001/api/
   - Should see: `{"message":"Hello World"}`

2. **Frontend Test**
   - Open: http://localhost:3000
   - Should see upload interface

3. **Full Test**
   - Upload any image
   - Click "ANALYZE"
   - Get FAKE/REAL verdict with confidence score!

---

## 🐛 Common Issues & Fixes

### Issue: "Python not found"
**Fix:**
```cmd
# Re-install Python and CHECK "Add to PATH"
# Or manually add to PATH:
# Search Windows for "Environment Variables"
# Edit PATH → Add: C:\Users\YourName\AppData\Local\Programs\Python\Python311
```

### Issue: "MongoDB connection failed"
**Fix:**
```cmd
net start MongoDB
```

### Issue: "Port 8001 or 3000 already in use"
**Fix:**
```cmd
# Kill port 8001
netstat -ano | findstr :8001
taskkill /PID [NUMBER_FROM_ABOVE] /F

# Kill port 3000
netstat -ano | findstr :3000
taskkill /PID [NUMBER_FROM_ABOVE] /F
```

### Issue: "emergentintegrations not found"
**Fix:**
```cmd
cd backend
venv\Scripts\activate
pip install emergentintegrations --extra-index-url https://d33sy5i8bnduwe.cloudfront.net/simple/ --force-reinstall
```

### Issue: "yarn command not found"
**Fix:**
```cmd
npm install -g yarn
```

---

## 📝 Environment Files (Auto-Created)

### backend/.env
```
MONGO_URL=mongodb://localhost:27017
DB_NAME=test_database
CORS_ORIGINS=*
EMERGENT_LLM_KEY=sk-emergent-aAf2546B027360d1e4
```

### frontend/.env
```
REACT_APP_BACKEND_URL=http://localhost:8001
```

---

## 🌐 Don't Want Local Setup?

Your app is **ALREADY DEPLOYED** online!

Check your Emergent dashboard for the live preview URL.  
No local setup needed - just use it online! 🎉

---

## 📞 Need Help?

1. **Read full guide:** `WINDOWS_SETUP.md`
2. **Check dependencies:** `README_DEPENDENCIES.md`
3. **Verify installations:**
   ```cmd
   python --version
   node --version
   npm --version
   ```

---

## 🎉 That's It!

**Total time:** ~5 minutes  
**Total cost:** $0.00  
**Result:** Working AI image detector!

Just run `setup.bat` once, then `start-app.bat` whenever you want to use it!
