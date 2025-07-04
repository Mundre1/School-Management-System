# Smart School ERP System - Complete Installation Guide

## 📋 Prerequisites

### System Requirements
- **Operating System:** macOS, Linux, or Windows
- **Python:** 3.10 or higher
- **Node.js:** 16.x or higher
- **PostgreSQL:** 13.x or higher
- **Redis:** 6.x or higher (for Celery)
- **Git:** Latest version

### Development Tools
- **Code Editor:** VS Code (recommended)
- **API Testing:** Postman
- **Database Client:** pgAdmin or DBeaver
- **Mobile Development:**
  - Xcode (for iOS development on macOS)
  - Android Studio (for Android development)
  - React Native CLI

---

## 🚀 Backend Setup (Django REST Framework)

### Step 1: Clone Repository

```bash
git clone https://github.com/yourusername/smart-school-erp.git
cd smart-school-erp
```

### Step 2: Create Virtual Environment

```bash
# Navigate to backend directory
cd backend

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

### Step 3: Install Python Dependencies

```bash
# Upgrade pip
pip install --upgrade pip

# Install all dependencies
pip install -r requirements.txt
```

### Step 4: Setup PostgreSQL Database

```bash
# Install PostgreSQL (if not installed)
# On macOS:
brew install postgresql
brew services start postgresql

# On Ubuntu/Debian:
sudo apt-get install postgresql postgresql-contrib
sudo systemctl start postgresql

# Create database
psql postgres
CREATE DATABASE school_erp_db;
CREATE USER school_admin WITH PASSWORD 'your_password';
ALTER ROLE school_admin SET client_encoding TO 'utf8';
ALTER ROLE school_admin SET default_transaction_isolation TO 'read committed';
ALTER ROLE school_admin SET timezone TO 'Asia/Kathmandu';
GRANT ALL PRIVILEGES ON DATABASE school_erp_db TO school_admin;
\q
```

### Step 5: Setup Redis (for Celery)

```bash
# Install Redis
# On macOS:
brew install redis
brew services start redis

# On Ubuntu/Debian:
sudo apt-get install redis-server
sudo systemctl start redis

# Verify Redis is running
redis-cli ping
# Should return: PONG
```

### Step 6: Configure Environment Variables

```bash
# Copy example environment file
cp .env.example .env

# Edit .env file with your configuration
nano .env
```

**Required Environment Variables:**

```env
# Django Settings
SECRET_KEY=your-secret-key-here-generate-new-one
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Database Configuration
DB_NAME=school_erp_db
DB_USER=school_admin
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432

# JWT Settings
JWT_ACCESS_TOKEN_LIFETIME=60
JWT_REFRESH_TOKEN_LIFETIME=1440

# Email Configuration (Gmail example)
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password

# Khalti Payment Gateway
KHALTI_PUBLIC_KEY=your-khalti-public-key
KHALTI_SECRET_KEY=your-khalti-secret-key

# Redis Configuration
REDIS_URL=redis://localhost:6379/0
CELERY_BROKER_URL=redis://localhost:6379/0
```

### Step 7: Run Database Migrations

```bash
# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Verify migrations
python manage.py showmigrations
```

### Step 8: Create Superuser

```bash
python manage.py createsuperuser

# Follow prompts:
# Email: admin@school.com
# First name: Admin
# Last name: User
# Password: (enter secure password)
```

### Step 9: Collect Static Files

```bash
python manage.py collectstatic --noinput
```

### Step 10: Load Sample Data (Optional)

```bash
# Create sample data fixture
python manage.py loaddata sample_data.json
```

### Step 11: Start Development Server

```bash
# Start Django development server
python manage.py runserver

# Server will start at: http://localhost:8000
```

### Step 12: Start Celery Worker (Separate Terminal)

```bash
# Activate virtual environment
source venv/bin/activate

# Start Celery worker
celery -A core worker -l info

# Start Celery beat (for scheduled tasks)
celery -A core beat -l info
```

### Step 13: Verify Backend Installation

Open browser and navigate to:
- **Admin Panel:** http://localhost:8000/admin/
- **API Documentation:** http://localhost:8000/swagger/
- **API Root:** http://localhost:8000/api/v1/

---

## 📱 Mobile App Setup (React Native)

### Step 1: Navigate to Mobile App Directory

```bash
cd ../mobile-app
```

### Step 2: Install Node Dependencies

```bash
# Install dependencies
npm install

# Or using Yarn
yarn install
```

### Step 3: Setup Environment Variables

```bash
# Copy example environment file
cp .env.example .env

# Edit .env file
nano .env
```

**Required Environment Variables:**

```env
API_BASE_URL=http://localhost:8000/api/v1
KHALTI_PUBLIC_KEY=your-khalti-public-key
FIREBASE_API_KEY=your-firebase-api-key
FIREBASE_PROJECT_ID=your-project-id
```

### Step 4: iOS Setup (macOS only)

```bash
# Navigate to iOS directory
cd ios

# Install CocoaPods dependencies
pod install

# Go back to mobile-app directory
cd ..
```

### Step 5: Android Setup

```bash
# Ensure Android SDK is installed
# Set ANDROID_HOME environment variable

# On macOS/Linux, add to ~/.bash_profile or ~/.zshrc:
export ANDROID_HOME=$HOME/Library/Android/sdk
export PATH=$PATH:$ANDROID_HOME/emulator
export PATH=$PATH:$ANDROID_HOME/tools
export PATH=$PATH:$ANDROID_HOME/tools/bin
export PATH=$PATH:$ANDROID_HOME/platform-tools
```

### Step 6: Start Metro Bundler

```bash
# Start Metro bundler
npm start

# Or
npx react-native start
```

### Step 7: Run on Android

```bash
# In a new terminal, run:
npm run android

# Or
npx react-native run-android

# Make sure Android emulator is running or device is connected
```

### Step 8: Run on iOS (macOS only)

```bash
# In a new terminal, run:
npm run ios

# Or
npx react-native run-ios

# Make sure iOS simulator is running
```

### Step 9: Verify Mobile App Installation

- App should launch on emulator/device
- Login screen should appear
- Test login with superuser credentials

---

## 🌐 Frontend Web Setup (React.js) - Optional

### Step 1: Navigate to Frontend Directory

```bash
cd ../frontend
```

### Step 2: Install Dependencies

```bash
npm install
```

### Step 3: Setup Environment Variables

```bash
cp .env.example .env
nano .env
```

```env
REACT_APP_API_URL=http://localhost:8000/api/v1
REACT_APP_KHALTI_PUBLIC_KEY=your-khalti-public-key
```

### Step 4: Start Development Server

```bash
npm start

# Server will start at: http://localhost:3000
```

---

## 🧪 Testing Installation

### Backend Tests

```bash
cd backend
source venv/bin/activate

# Run all tests
python manage.py test

# Run specific app tests
python manage.py test apps.authentication

# Run with coverage
coverage run --source='.' manage.py test
coverage report
coverage html
```

### Mobile App Tests

```bash
cd mobile-app

# Run tests
npm test

# Run with coverage
npm test -- --coverage
```

### API Testing with Postman

1. Import Postman collection from `docs/postman/`
2. Set environment variables
3. Test authentication endpoints
4. Test CRUD operations

---

## 🔧 Troubleshooting

### Common Backend Issues

**Issue: Database connection error**
```bash
# Check PostgreSQL is running
pg_isready

# Check database exists
psql -l | grep school_erp_db

# Verify credentials in .env file
```

**Issue: Redis connection error**
```bash
# Check Redis is running
redis-cli ping

# Restart Redis
brew services restart redis  # macOS
sudo systemctl restart redis  # Linux
```

**Issue: Migration errors**
```bash
# Reset migrations (development only)
python manage.py migrate --fake
python manage.py migrate --fake-initial

# Or drop database and recreate
dropdb school_erp_db
createdb school_erp_db
python manage.py migrate
```

**Issue: Static files not loading**
```bash
# Collect static files again
python manage.py collectstatic --clear --noinput
```

### Common Mobile App Issues

**Issue: Metro bundler error**
```bash
# Clear cache
npm start -- --reset-cache

# Or
npx react-native start --reset-cache
```

**Issue: Android build error**
```bash
# Clean Android build
cd android
./gradlew clean
cd ..

# Rebuild
npm run android
```

**Issue: iOS build error**
```bash
# Clean iOS build
cd ios
rm -rf build
pod deintegrate
pod install
cd ..

# Rebuild
npm run ios
```

**Issue: Module not found**
```bash
# Reinstall dependencies
rm -rf node_modules
npm install

# iOS specific
cd ios
pod install
cd ..
```

---

## 📊 Database Management

### Create Backup

```bash
# Backup database
pg_dump -U school_admin school_erp_db > backup.sql

# Backup with timestamp
pg_dump -U school_admin school_erp_db > backup_$(date +%Y%m%d_%H%M%S).sql
```

### Restore Backup

```bash
# Restore database
psql -U school_admin school_erp_db < backup.sql
```

### Database Migrations

```bash
# Create new migration
python manage.py makemigrations app_name

# Apply specific migration
python manage.py migrate app_name migration_name

# Rollback migration
python manage.py migrate app_name previous_migration_name

# Show migration status
python manage.py showmigrations
```

---

## 🔐 Security Setup

### Generate Secret Key

```python
# In Python shell
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

### Setup Gmail App Password

1. Go to Google Account settings
2. Enable 2-Factor Authentication
3. Generate App Password
4. Use App Password in EMAIL_HOST_PASSWORD

### Setup Khalti Payment Gateway

1. Register at https://khalti.com/
2. Get API keys from dashboard
3. Add keys to .env file

---

## 📱 Mobile App Configuration

### Configure Firebase (Push Notifications)

1. Create Firebase project
2. Add Android app
3. Download `google-services.json`
4. Place in `android/app/`
5. Add iOS app
6. Download `GoogleService-Info.plist`
7. Place in `ios/`

### Configure App Icons

```bash
# Generate app icons
# Place icon.png (1024x1024) in assets/
npx react-native-asset
```

### Configure Splash Screen

```bash
# Install splash screen package
npm install react-native-splash-screen

# Configure for Android and iOS
# Follow package documentation
```

---

## 🚀 Development Workflow

### Git Workflow

```bash
# Create feature branch
git checkout -b feature/new-feature

# Make changes and commit
git add .
git commit -m "Add new feature"

# Push to remote
git push origin feature/new-feature

# Create pull request on GitHub
```

### Code Quality

```bash
# Backend - Format code
black .
isort .

# Backend - Lint code
flake8 .
pylint apps/

# Mobile - Format code
npm run lint
npm run format
```

---

## 📝 Next Steps

After successful installation:

1. ✅ Explore Admin Panel
2. ✅ Test API endpoints in Swagger
3. ✅ Create sample students and staff
4. ✅ Test mobile app features
5. ✅ Configure payment gateway
6. ✅ Setup email notifications
7. ✅ Test attendance system
8. ✅ Generate sample reports
9. ✅ Review documentation
10. ✅ Start development!

---

## 📞 Support

If you encounter any issues:

1. Check troubleshooting section
2. Review error logs
3. Search GitHub issues
4. Create new issue with details
5. Contact support: support@smartschoolerp.com

---

## 🎉 Congratulations!

You have successfully installed Smart School ERP System!

**Happy Coding! 🚀**
