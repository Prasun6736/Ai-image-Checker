# 📋 Complete Setup Checklist

## ✅ PRE-INSTALLATION CHECKLIST

```
□ Windows 10/11 computer
□ Internet connection
□ 1GB free disk space
□ Administrator access (for installations)
```

---

## 📥 STEP 1: Download Prerequisites

### Python 3.9+
```
□ Go to: https://www.python.org/downloads/
□ Download: "Download Python 3.11" (or higher)
□ Run installer
□ ✅ MUST CHECK: "Add Python to PATH"
□ Click "Install Now"
□ Wait for completion
□ Verify:
  Open CMD → type: python --version
  Should show: Python 3.11.x
```

### Node.js 18+
```
□ Go to: https://nodejs.org/
□ Download: LTS version (left button)
□ Run installer
□ Click "Next" with defaults
□ Wait for completion (3-5 minutes)
□ Verify:
  Open CMD → type: node --version
  Should show: v18.x.x or higher
```

### MongoDB Community
```
□ Go to: https://www.mongodb.com/try/download/community
□ Download: Windows MSI
□ Run installer
□ Choose: "Complete" installation
□ Check: "Install MongoDB as a Service"
□ Wait for completion (5-8 minutes)
□ Verify:
  Open CMD → type: net start MongoDB
  Should show: service is running
```

---

## 📁 STEP 2: Project Files Setup

### Download Project
```
□ Download all project files
□ Extract to folder: C:\image-detector (or any location)
□ Verify folder structure:
  C:\image-detector\
  ├── setup.bat              ✅
  ├── start-app.bat          ✅
  ├── backend\
  │   ├── server.py          ✅
  │   └── requirements.txt   ✅
  └── frontend\
      ├── package.json       ✅
      └── src\               ✅
```

---

## ⚙️ STEP 3: Auto Installation

### Run Setup
```
□ Navigate to: C:\image-detector
□ Double-click: setup.bat
□ Wait and watch progress:
  □ [1/5] Installing Yarn... (30 seconds)
  □ [2/5] Backend setup... (1-2 minutes)
  □ [3/5] Frontend setup... (2-3 minutes)
  □ [4/5] Creating .env files... (instant)
  □ [5/5] Setup complete!
□ Press any key to close
```

### Verify Installation
```
□ Check backend\venv\ folder exists
□ Check frontend\node_modules\ folder exists
□ Check backend\.env file exists
□ Check frontend\.env file exists
```

---

## 🚀 STEP 4: Launch Application

### Start App
```
□ Double-click: start-app.bat
□ Two windows will open:
  □ Backend window (black, shows server logs)
  □ Frontend window (black, shows React logs)
□ Browser opens automatically to: http://localhost:3000
□ Wait 10-15 seconds for full startup
```

### Verify Running
```
□ Backend check:
  Open: http://localhost:8001/api/
  Should see: {"message":"Hello World"}

□ Frontend check:
  Open: http://localhost:3000
  Should see: Upload interface with "VERIFY." header

□ Full test:
  □ Click upload area
  □ Select any image from computer
  □ Image preview appears
  □ Click "ANALYZE" button
  □ Wait 3-5 seconds
  □ See FAKE or REAL verdict
  □ See confidence score (0-100%)
  □ See analysis details
```

---

## 🎯 DAILY USE CHECKLIST

### Every Time You Want to Use the App:

```
□ Make sure MongoDB is running:
  CMD → net start MongoDB

□ Double-click: start-app.bat

□ Wait for browser to open

□ Start analyzing images!

□ To stop: Press any key in start-app window
```

---

## 🐛 TROUBLESHOOTING CHECKLIST

### If Setup Fails:

#### Python Issues
```
□ Python command not found
  → Reinstall Python with "Add to PATH" checked
  → Or add manually to environment variables

□ Pip not found
  → Same as above

□ Virtual environment error
  → Delete backend\venv folder
  → Run setup.bat again
```

#### Node Issues
```
□ Node/npm command not found
  → Reinstall Node.js
  → Restart computer

□ Yarn command not found
  → Open CMD → npm install -g yarn
  → Run setup.bat again

□ Package install fails
  → Delete frontend\node_modules folder
  → Run setup.bat again
```

#### MongoDB Issues
```
□ MongoDB not starting
  → Open Services (Win+R → services.msc)
  → Find "MongoDB Server"
  → Right-click → Start

□ Connection refused
  → Check MongoDB service is running
  → Check port 27017 is not blocked

□ Alternative: Use MongoDB Atlas (cloud)
  → Sign up at mongodb.com/cloud/atlas
  → Create free cluster
  → Get connection string
  → Update backend\.env → MONGO_URL=your_connection_string
```

#### App Issues
```
□ Port 8001 already in use
  → netstat -ano | findstr :8001
  → taskkill /PID [number] /F
  → Run start-app.bat again

□ Port 3000 already in use
  → netstat -ano | findstr :3000
  → taskkill /PID [number] /F
  → Run start-app.bat again

□ Frontend won't load
  → Check backend is running (should see logs)
  → Check http://localhost:8001/api/ works
  → Check frontend\.env has correct URL

□ Analysis fails
  → Check backend\.env has EMERGENT_LLM_KEY
  → Check internet connection (API call needs internet)
  → Check backend logs for errors
```

---

## 🎓 LEARNING CHECKLIST

### Understanding Your Setup:

```
□ I know where my project files are
□ I know how to start the app (start-app.bat)
□ I know how to stop the app (press any key)
□ I know where to see backend logs (Backend window)
□ I know where to see frontend logs (Frontend window)
□ I know the app uses FREE AI credits
□ I know I don't need to pay for anything
□ I know how to update .env files if needed
```

---

## 📊 INSTALLATION TIMELINE

```
Total Time: ~15 minutes

Prerequisites (one-time):
├── Python install: 2 min
├── Node install: 3 min
├── MongoDB install: 5 min
└── Total: 10 minutes

Auto Setup (one-time):
├── Yarn install: 30 sec
├── Backend setup: 1 min
├── Frontend setup: 3 min
└── Total: 5 minutes

Daily Usage (every time):
└── Start app: 15 seconds
```

---

## 💾 BACKUP CHECKLIST

### Important Files to Backup:

```
□ backend\server.py (your code)
□ frontend\src\App.js (your code)
□ backend\.env (configuration)
□ frontend\.env (configuration)

DO NOT backup:
✗ backend\venv\ (regenerate with setup.bat)
✗ frontend\node_modules\ (regenerate with setup.bat)
```

---

## 🔐 SECURITY CHECKLIST

```
□ Free Emergent LLM key is pre-configured
□ No personal API keys exposed
□ MongoDB runs locally (not exposed to internet)
□ CORS set to * (for local development only)
□ All connections are localhost (secure)
```

---

## ✅ SUCCESS CRITERIA

### You're Done When:

```
□ setup.bat completed without errors
□ start-app.bat opens two windows
□ Browser shows upload interface
□ Can upload an image
□ Can click ANALYZE button
□ See FAKE or REAL verdict
□ See confidence percentage
□ See analysis details
□ Can click RESET button
□ Can upload another image
```

---

## 🎉 CONGRATULATIONS!

If all checkboxes above are ✅, you're ready to use your Image Authenticity Detector!

**Total Cost: $0.00**  
**Setup Time: ~15 minutes**  
**Daily Use: 15 seconds to start**

---

## 📞 QUICK REFERENCE

```
Start App:     start-app.bat
Frontend URL:  http://localhost:3000
Backend URL:   http://localhost:8001/api/
MongoDB:       mongodb://localhost:27017
AI Credits:    FREE (Emergent LLM Key)
```

---

## 🔄 NEXT STEPS

```
□ Try uploading different images
□ Test with real photos
□ Test with AI-generated images
□ Share with friends
□ Check the live deployed version online
□ Explore customization options
```

**Enjoy your AI-powered image detector!** 🚀
