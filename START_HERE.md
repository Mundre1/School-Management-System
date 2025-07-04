# 🚀 START HERE - Quick Setup Guide

## Step-by-Step Setup Instructions

Follow these commands **exactly** in order:

---

## ✅ Step 1: Navigate to Project Directory

```bash
cd "/Users/ayush/Desktop/School /smart-school-erp"
```

---

## 🔧 Step 2: Backend Setup

### 2.1 Navigate to Backend Directory
```bash
cd backend
```

### 2.2 Create Virtual Environment
```bash
python3 -m venv venv
```

### 2.3 Activate Virtual Environment
```bash
source venv/bin/activate
```

You should see `(venv)` in your terminal prompt.

### 2.4 Upgrade pip
```bash
pip install --upgrade pip
```

### 2.5 Install Dependencies
```bash
pip install -r requirements.txt
```

This will take a few minutes. Wait for it to complete.

### 2.6 Setup Environment Variables
```bash
cp .env.example .env
```

Now edit the `.env` file with your settings:
```bash
nano .env
```

**Minimum required changes:**
- Set `SECRET_KEY` to a random string
- Set `DB_NAME=school_erp_db`
- Set `DB_USER=postgres`
- Set `DB_PASSWORD=your_password`

Press `Ctrl+X`, then `Y`, then `Enter` to save.

### 2.7 Create PostgreSQL Database
```bash
createdb school_erp_db
```

If this fails, install PostgreSQL first:
```bash
brew install postgresql
brew services start postgresql
createdb school_erp_db
```

### 2.8 Run Database Migrations
```bash
python manage.py migrate
```

### 2.9 Create Admin User
```bash
python manage.py createsuperuser
```

Enter:
- Email: `admin@school.com`
- First name: `Admin`
- Last name: `User`
- Password: `admin123` (or your choice)

### 2.10 Start Backend Server
```bash
python manage.py runserver
```

**✅ Backend is now running at http://localhost:8000**

Keep this terminal open and open a **new terminal** for the next steps.

---

## 📱 Step 3: Mobile App Setup (Optional)

### 3.1 Navigate to Mobile App Directory (in new terminal)
```bash
cd "/Users/ayush/Desktop/School /smart-school-erp/mobile-app"
```

### 3.2 Install Node Dependencies
```bash
npm install
```

This will take several minutes.

### 3.3 Setup Environment Variables
```bash
cp .env.example .env
```

Edit the `.env` file:
```bash
nano .env
```

Change:
```
API_BASE_URL=http://localhost:8000/api/v1
```

Press `Ctrl+X`, then `Y`, then `Enter` to save.

### 3.4 iOS Setup (macOS only)
```bash
cd ios
pod install
cd ..
```

### 3.5 Start Metro Bundler
```bash
npm start
```

Keep this terminal open and open **another new terminal** for running the app.

### 3.6 Run Mobile App (in another new terminal)

**For Android:**
```bash
cd "/Users/ayush/Desktop/School /smart-school-erp/mobile-app"
npm run android
```

**For iOS (macOS only):**
```bash
cd "/Users/ayush/Desktop/School /smart-school-erp/mobile-app"
npm run ios
```

---

## 🎉 You're Done!

### What's Running:

1. **Backend API:** http://localhost:8000
   - Admin Panel: http://localhost:8000/admin/
   - API Docs: http://localhost:8000/swagger/
   - Login: admin@school.com / admin123

2. **Mobile App:** Running on emulator/device

---

## 🐛 Troubleshooting

### Backend Issues

**"command not found: python"**
```bash
# Use python3 instead
python3 -m venv venv
```

**"createdb: command not found"**
```bash
# Install PostgreSQL
brew install postgresql
brew services start postgresql
createdb school_erp_db
```

**"No module named 'django'"**
```bash
# Make sure virtual environment is activated
source venv/bin/activate
pip install -r requirements.txt
```

**"Database connection error"**
```bash
# Check PostgreSQL is running
brew services list
# Start if not running
brew services start postgresql
```

### Mobile App Issues

**"command not found: npm"**
```bash
# Install Node.js
brew install node
```

**"Metro bundler error"**
```bash
# Clear cache
npm start -- --reset-cache
```

**"Android build error"**
```bash
# Clean build
cd android
./gradlew clean
cd ..
npm run android
```

**"iOS build error"**
```bash
# Reinstall pods
cd ios
rm -rf Pods
pod install
cd ..
npm run ios
```

---

## 📚 Next Steps

1. **Explore Admin Panel:** http://localhost:8000/admin/
2. **Test API:** http://localhost:8000/swagger/
3. **Read Documentation:** See README.md
4. **Create Sample Data:** Add students, staff, etc.

---

## 🆘 Need Help?

1. Check [QUICK_START.md](QUICK_START.md)
2. Read [INSTALLATION_GUIDE.md](INSTALLATION_GUIDE.md)
3. Review [INDEX.md](INDEX.md) for all documentation

---

## ⚡ Quick Commands Reference

### Backend Commands
```bash
# Activate virtual environment
source venv/bin/activate

# Run server
python manage.py runserver

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run tests
python manage.py test
```

### Mobile App Commands
```bash
# Install dependencies
npm install

# Start Metro
npm start

# Run Android
npm run android

# Run iOS
npm run ios

# Clear cache
npm start -- --reset-cache
```

---

**Happy Coding! 🚀**
