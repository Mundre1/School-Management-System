# Smart School ERP System - Production Deployment Guide

## 🚀 PythonAnywhere Deployment (Backend)

### Prerequisites
- PythonAnywhere account (Paid plan recommended for PostgreSQL)
- GitHub repository with your code
- PostgreSQL database credentials
- Domain name (optional)

---

## Step 1: Create PythonAnywhere Account

1. Go to https://www.pythonanywhere.com/
2. Sign up for an account
3. Choose appropriate plan:
   - **Hacker Plan** ($5/month) - For testing
   - **Web Developer Plan** ($12/month) - Recommended for production

---

## Step 2: Clone Repository

```bash
# Open Bash console in PythonAnywhere

# Clone your repository
git clone https://github.com/yourusername/smart-school-erp.git
cd smart-school-erp/backend
```

---

## Step 3: Create Virtual Environment

```bash
# Create virtual environment with Python 3.10
mkvirtualenv --python=/usr/bin/python3.10 school-erp-env

# Activate virtual environment
workon school-erp-env

# Upgrade pip
pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt
```

---

## Step 4: Setup PostgreSQL Database

### Option A: PythonAnywhere PostgreSQL (Paid plans)

```bash
# In PythonAnywhere Dashboard:
# 1. Go to "Databases" tab
# 2. Click "Create PostgreSQL database"
# 3. Note down database credentials
```

### Option B: External PostgreSQL (e.g., ElephantSQL)

1. Go to https://www.elephantsql.com/
2. Create free account
3. Create new database instance
4. Copy database URL

---

## Step 5: Configure Environment Variables

```bash
# Create .env file
nano .env
```

**Production .env Configuration:**

```env
# Django Settings
SECRET_KEY=your-production-secret-key-generate-new-one
DEBUG=False
ALLOWED_HOSTS=yourusername.pythonanywhere.com,www.yourdomain.com

# Database Configuration (PythonAnywhere)
DB_NAME=yourusername$school_erp_db
DB_USER=yourusername
DB_PASSWORD=your_database_password
DB_HOST=yourusername-postgres.postgres.pythonanywhere-services.com
DB_PORT=5432

# Or External Database URL
DATABASE_URL=postgresql://user:password@host:port/database

# JWT Settings
JWT_ACCESS_TOKEN_LIFETIME=60
JWT_REFRESH_TOKEN_LIFETIME=1440

# Email Configuration
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-production-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password

# Khalti Payment Gateway
KHALTI_PUBLIC_KEY=your-production-khalti-public-key
KHALTI_SECRET_KEY=your-production-khalti-secret-key

# Redis (if using external Redis)
REDIS_URL=redis://your-redis-url:6379/0

# Frontend URL
FRONTEND_URL=https://yourdomain.com

# CORS Settings
CORS_ALLOWED_ORIGINS=https://yourdomain.com,https://www.yourdomain.com

# Security
SECURE_SSL_REDIRECT=True
SESSION_COOKIE_SECURE=True
CSRF_COOKIE_SECURE=True
```

---

## Step 6: Run Database Migrations

```bash
# Activate virtual environment
workon school-erp-env

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Collect static files
python manage.py collectstatic --noinput
```

---

## Step 7: Configure WSGI

```bash
# In PythonAnywhere Dashboard:
# 1. Go to "Web" tab
# 2. Click "Add a new web app"
# 3. Choose "Manual configuration"
# 4. Select Python 3.10
```

**Edit WSGI configuration file:**

```python
# /var/www/yourusername_pythonanywhere_com_wsgi.py

import os
import sys

# Add your project directory to the sys.path
path = '/home/yourusername/smart-school-erp/backend'
if path not in sys.path:
    sys.path.insert(0, path)

# Set environment variable for Django settings
os.environ['DJANGO_SETTINGS_MODULE'] = 'core.settings'

# Activate virtual environment
activate_this = '/home/yourusername/.virtualenvs/school-erp-env/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

# Import Django WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

---

## Step 8: Configure Static Files

```bash
# In PythonAnywhere Web tab:
# Static files section:

# URL: /static/
# Directory: /home/yourusername/smart-school-erp/backend/staticfiles

# URL: /media/
# Directory: /home/yourusername/smart-school-erp/backend/media
```

---

## Step 9: Configure Virtual Environment

```bash
# In PythonAnywhere Web tab:
# Virtualenv section:

# Enter path:
/home/yourusername/.virtualenvs/school-erp-env
```

---

## Step 10: Reload Web App

```bash
# In PythonAnywhere Web tab:
# Click "Reload yourusername.pythonanywhere.com" button
```

---

## Step 11: Setup Scheduled Tasks (Celery Alternative)

Since PythonAnywhere doesn't support Celery, use scheduled tasks:

```bash
# In PythonAnywhere "Tasks" tab:

# Daily task at 9:00 AM - Send fee reminders
/home/yourusername/.virtualenvs/school-erp-env/bin/python /home/yourusername/smart-school-erp/backend/manage.py send_fee_reminders

# Daily task at 6:00 PM - Send attendance notifications
/home/yourusername/.virtualenvs/school-erp-env/bin/python /home/yourusername/smart-school-erp/backend/manage.py send_attendance_notifications
```

---

## Step 12: Setup Custom Domain (Optional)

1. Purchase domain from registrar (Namecheap, GoDaddy, etc.)
2. In PythonAnywhere Web tab, add domain
3. Configure DNS records:

```
Type: CNAME
Host: www
Value: yourusername.pythonanywhere.com

Type: A
Host: @
Value: (PythonAnywhere IP address)
```

4. Enable HTTPS (Let's Encrypt)

---

## Step 13: Configure HTTPS

```bash
# In PythonAnywhere Web tab:
# 1. Go to "Security" section
# 2. Click "Enable HTTPS"
# 3. Follow Let's Encrypt setup
```

---

## 📱 Mobile App Deployment

### Android Deployment (Google Play Store)

#### Step 1: Generate Signing Key

```bash
cd android/app

# Generate keystore
keytool -genkeypair -v -storetype PKCS12 -keystore smart-school-erp.keystore -alias smart-school-erp -keyalg RSA -keysize 2048 -validity 10000
```

#### Step 2: Configure Gradle

Edit `android/gradle.properties`:

```properties
MYAPP_UPLOAD_STORE_FILE=smart-school-erp.keystore
MYAPP_UPLOAD_KEY_ALIAS=smart-school-erp
MYAPP_UPLOAD_STORE_PASSWORD=your_keystore_password
MYAPP_UPLOAD_KEY_PASSWORD=your_key_password
```

Edit `android/app/build.gradle`:

```gradle
android {
    ...
    signingConfigs {
        release {
            if (project.hasProperty('MYAPP_UPLOAD_STORE_FILE')) {
                storeFile file(MYAPP_UPLOAD_STORE_FILE)
                storePassword MYAPP_UPLOAD_STORE_PASSWORD
                keyAlias MYAPP_UPLOAD_KEY_ALIAS
                keyPassword MYAPP_UPLOAD_KEY_PASSWORD
            }
        }
    }
    buildTypes {
        release {
            ...
            signingConfig signingConfigs.release
        }
    }
}
```

#### Step 3: Build Release APK/AAB

```bash
# Build APK
cd android
./gradlew assembleRelease

# APK location: android/app/build/outputs/apk/release/app-release.apk

# Build AAB (for Play Store)
./gradlew bundleRelease

# AAB location: android/app/build/outputs/bundle/release/app-release.aab
```

#### Step 4: Upload to Play Store

1. Go to https://play.google.com/console
2. Create new application
3. Fill in app details:
   - App name: Smart School ERP
   - Description: (from README)
   - Screenshots: (prepare 2-8 screenshots)
   - Feature graphic: 1024x500px
   - App icon: 512x512px
4. Upload AAB file
5. Set pricing (Free/Paid)
6. Select countries
7. Content rating questionnaire
8. Submit for review

---

### iOS Deployment (App Store)

#### Step 1: Configure Xcode Project

```bash
cd ios
open SmartSchoolERP.xcworkspace
```

#### Step 2: Update Bundle Identifier

1. Select project in Xcode
2. Go to "Signing & Capabilities"
3. Update Bundle Identifier: `com.yourcompany.smartschoolerp`
4. Select Team (Apple Developer Account required)

#### Step 3: Configure App Icons

1. Prepare app icons (1024x1024px)
2. Use https://appicon.co/ to generate all sizes
3. Add to `ios/SmartSchoolERP/Images.xcassets/AppIcon.appiconset/`

#### Step 4: Archive App

1. In Xcode, select "Any iOS Device"
2. Product → Archive
3. Wait for archive to complete
4. Click "Distribute App"
5. Choose "App Store Connect"
6. Upload to App Store Connect

#### Step 5: Submit to App Store

1. Go to https://appstoreconnect.apple.com/
2. Create new app
3. Fill in app information
4. Add screenshots (required sizes)
5. Select build
6. Submit for review

---

## 🌐 Frontend Web Deployment (Optional)

### Vercel Deployment

```bash
# Install Vercel CLI
npm install -g vercel

# Navigate to frontend directory
cd frontend

# Deploy
vercel

# Follow prompts
# Production deployment
vercel --prod
```

### Netlify Deployment

```bash
# Install Netlify CLI
npm install -g netlify-cli

# Navigate to frontend directory
cd frontend

# Build project
npm run build

# Deploy
netlify deploy

# Production deployment
netlify deploy --prod
```

---

## 🔒 Production Security Checklist

### Backend Security

- [ ] Change SECRET_KEY to strong random value
- [ ] Set DEBUG=False
- [ ] Configure ALLOWED_HOSTS properly
- [ ] Enable HTTPS/SSL
- [ ] Set secure cookie flags
- [ ] Configure CORS properly
- [ ] Use environment variables for secrets
- [ ] Enable database backups
- [ ] Setup error monitoring (Sentry)
- [ ] Configure rate limiting
- [ ] Enable SQL injection protection
- [ ] Setup firewall rules
- [ ] Regular security updates

### Mobile App Security

- [ ] Use production API URL
- [ ] Enable SSL pinning
- [ ] Obfuscate code (ProGuard for Android)
- [ ] Remove debug logs
- [ ] Secure local storage
- [ ] Implement certificate pinning
- [ ] Enable app signing
- [ ] Test on real devices
- [ ] Security audit

---

## 📊 Monitoring & Maintenance

### Setup Error Monitoring

```bash
# Install Sentry
pip install sentry-sdk

# Configure in settings.py
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

sentry_sdk.init(
    dsn="your-sentry-dsn",
    integrations=[DjangoIntegration()],
    traces_sample_rate=1.0,
    send_default_pii=True
)
```

### Database Backups

```bash
# Automated daily backup script
#!/bin/bash
DATE=$(date +%Y%m%d_%H%M%S)
pg_dump -U username dbname > backup_$DATE.sql
# Upload to cloud storage
```

### Log Monitoring

```bash
# View Django logs
tail -f /var/log/pythonanywhere.log

# View error logs
tail -f /var/log/pythonanywhere.error.log
```

---

## 🧪 Post-Deployment Testing

### Backend Testing

```bash
# Test API endpoints
curl https://yourusername.pythonanywhere.com/api/v1/

# Test authentication
curl -X POST https://yourusername.pythonanywhere.com/api/v1/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{"email":"admin@school.com","password":"password"}'

# Test static files
curl https://yourusername.pythonanywhere.com/static/admin/css/base.css
```

### Mobile App Testing

- [ ] Test on multiple devices
- [ ] Test all user roles
- [ ] Test payment integration
- [ ] Test push notifications
- [ ] Test offline functionality
- [ ] Test camera/QR features
- [ ] Performance testing
- [ ] Battery usage testing

---

## 📈 Performance Optimization

### Backend Optimization

```python
# Enable database connection pooling
DATABASES = {
    'default': {
        ...
        'CONN_MAX_AGE': 600,
    }
}

# Enable caching
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
    }
}

# Optimize queries
# Use select_related() and prefetch_related()
students = Student.objects.select_related('user', 'class').all()
```

### Mobile App Optimization

```javascript
// Enable Hermes engine (Android)
// In android/app/build.gradle
project.ext.react = [
    enableHermes: true
]

// Optimize images
// Use react-native-fast-image

// Enable ProGuard (Android)
// In android/app/build.gradle
buildTypes {
    release {
        minifyEnabled true
        proguardFiles getDefaultProguardFile('proguard-android.txt'), 'proguard-rules.pro'
    }
}
```

---

## 🔄 Continuous Deployment

### Setup GitHub Actions

Create `.github/workflows/deploy.yml`:

```yaml
name: Deploy to PythonAnywhere

on:
  push:
    branches: [ main ]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      
      - name: Deploy to PythonAnywhere
        env:
          PYTHONANYWHERE_USERNAME: ${{ secrets.PYTHONANYWHERE_USERNAME }}
          PYTHONANYWHERE_TOKEN: ${{ secrets.PYTHONANYWHERE_TOKEN }}
        run: |
          # Add deployment script here
```

---

## 📞 Support & Troubleshooting

### Common Issues

**Issue: 502 Bad Gateway**
- Check WSGI configuration
- Verify virtual environment path
- Check error logs

**Issue: Static files not loading**
- Run collectstatic
- Check static files configuration
- Verify WhiteNoise setup

**Issue: Database connection error**
- Verify database credentials
- Check database host/port
- Ensure database is running

---

## 🎉 Deployment Complete!

Your Smart School ERP System is now live in production!

**Production URLs:**
- Backend API: https://yourusername.pythonanywhere.com/api/v1/
- Admin Panel: https://yourusername.pythonanywhere.com/admin/
- API Docs: https://yourusername.pythonanywhere.com/swagger/
- Mobile App: Available on Play Store / App Store

**Next Steps:**
1. Monitor application performance
2. Setup automated backups
3. Configure monitoring alerts
4. Gather user feedback
5. Plan feature updates

---

**Congratulations on your successful deployment! 🚀**
