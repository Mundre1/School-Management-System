# Smart School ERP System - Quick Start Guide

## 🚀 Get Started in 10 Minutes!

This guide will help you quickly set up and run the Smart School ERP System on your local machine.

---

## ⚡ Prerequisites (5 minutes)

Install these tools if you don't have them:

```bash
# Check if installed
python3 --version  # Should be 3.10+
node --version     # Should be 16+
psql --version     # PostgreSQL
redis-cli --version # Redis

# macOS Installation
brew install python@3.10 node postgresql redis

# Ubuntu/Debian Installation
sudo apt-get update
sudo apt-get install python3.10 nodejs postgresql redis-server

# Start services
brew services start postgresql redis  # macOS
sudo systemctl start postgresql redis # Linux
```

---

## 🔧 Backend Setup (3 minutes)

```bash
# 1. Clone and navigate
git clone https://github.com/yourusername/smart-school-erp.git
cd smart-school-erp/backend

# 2. Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Setup database
createdb school_erp_db

# 5. Configure environment
cp .env.example .env
# Edit .env with your database credentials

# 6. Run migrations
python manage.py migrate

# 7. Create admin user
python manage.py createsuperuser
# Email: admin@school.com
# Password: admin123 (change in production!)

# 8. Start server
python manage.py runserver
```

**✅ Backend is running at http://localhost:8000**

---

## 📱 Mobile App Setup (2 minutes)

```bash
# 1. Navigate to mobile app
cd ../mobile-app

# 2. Install dependencies
npm install

# 3. Setup environment
cp .env.example .env

# 4. iOS setup (macOS only)
cd ios && pod install && cd ..

# 5. Start Metro bundler
npm start

# 6. Run app (in new terminal)
npm run android  # For Android
npm run ios      # For iOS
```

**✅ Mobile app is running!**

---

## 🌐 Quick Test

### Test Backend API

```bash
# Open browser and visit:
http://localhost:8000/admin/          # Admin panel
http://localhost:8000/swagger/        # API documentation
http://localhost:8000/api/v1/         # API root

# Login with:
# Email: admin@school.com
# Password: admin123
```

### Test Mobile App

1. App should launch on emulator/device
2. You'll see the login screen
3. Login with admin credentials
4. Explore the dashboard!

---

## 📊 Sample Data (Optional)

```bash
# Create sample data for testing
cd backend
python manage.py shell

# In Python shell:
from apps.authentication.models import User
from apps.students.models import Student

# Create sample student
student_user = User.objects.create_user(
    email='student@school.com',
    password='student123',
    first_name='John',
    last_name='Doe',
    role='STUDENT'
)

# Create sample teacher
teacher_user = User.objects.create_user(
    email='teacher@school.com',
    password='teacher123',
    first_name='Jane',
    last_name='Smith',
    role='STAFF'
)

print("Sample users created!")
exit()
```

---

## 🎯 Quick Feature Tour

### Admin Dashboard
1. Login as admin
2. Navigate to Dashboard
3. View analytics and statistics
4. Manage students, staff, courses

### Student Management
1. Go to Students section
2. Click "Add Student"
3. Fill in details
4. Upload photo
5. Save

### Attendance System
1. Go to Attendance
2. Select class
3. Mark attendance (Present/Absent)
4. Or use QR code scanner
5. View attendance report

### Fee Management
1. Go to Fees section
2. Create fee structure
3. Assign to students
4. Students can pay via Khalti
5. View payment history

### Results System
1. Go to Results
2. Select exam/term
3. Enter marks
4. Publish results
5. Generate report cards (PDF)

---

## 🔑 Default Credentials

### Admin
- **Email:** admin@school.com
- **Password:** admin123
- **Role:** Head of School

### Sample Teacher
- **Email:** teacher@school.com
- **Password:** teacher123
- **Role:** Staff/Teacher

### Sample Student
- **Email:** student@school.com
- **Password:** student123
- **Role:** Student

**⚠️ Change these passwords in production!**

---

## 📱 Mobile App Features

### Login Screen
- Email/Password login
- OTP login option
- Biometric authentication
- Forgot password

### Admin Dashboard
- Total students/staff count
- Attendance analytics
- Fee collection charts
- Quick actions

### Staff Dashboard
- Mark attendance
- Upload results
- Create assignments
- Send notices

### Student Dashboard
- View profile
- Check attendance
- View results
- Pay fees
- View timetable

---

## 🛠️ Common Commands

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

# Collect static files
python manage.py collectstatic

# Run tests
python manage.py test

# Start Celery worker
celery -A core worker -l info
```

### Mobile App Commands

```bash
# Start Metro bundler
npm start

# Run on Android
npm run android

# Run on iOS
npm run ios

# Clear cache
npm start -- --reset-cache

# Run tests
npm test

# Build for production
npm run build:android
npm run build:ios
```

---

## 🐛 Quick Troubleshooting

### Backend Issues

**Database error:**
```bash
# Reset database
dropdb school_erp_db
createdb school_erp_db
python manage.py migrate
```

**Port already in use:**
```bash
# Kill process on port 8000
lsof -ti:8000 | xargs kill -9
```

**Module not found:**
```bash
pip install -r requirements.txt
```

### Mobile App Issues

**Metro bundler error:**
```bash
npm start -- --reset-cache
```

**Build error:**
```bash
# Clean and rebuild
cd android && ./gradlew clean && cd ..
npm run android
```

**Module not found:**
```bash
rm -rf node_modules
npm install
```

---

## 📚 Next Steps

1. ✅ **Explore Features**
   - Try all user roles
   - Test attendance system
   - Create sample data
   - Generate reports

2. ✅ **Customize**
   - Update branding
   - Configure settings
   - Add school logo
   - Customize colors

3. ✅ **Configure Integrations**
   - Setup Khalti payment
   - Configure email
   - Setup SMS gateway
   - Enable push notifications

4. ✅ **Read Documentation**
   - [README.md](README.md) - Full documentation
   - [INSTALLATION_GUIDE.md](INSTALLATION_GUIDE.md) - Detailed setup
   - [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md) - Production deployment
   - [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md) - Project overview

5. ✅ **Development**
   - Review code structure
   - Understand architecture
   - Add custom features
   - Write tests

---

## 🎓 Learning Resources

### Django REST Framework
- Official Docs: https://www.django-rest-framework.org/
- JWT Auth: https://django-rest-framework-simplejwt.readthedocs.io/

### React Native
- Official Docs: https://reactnative.dev/
- React Navigation: https://reactnavigation.org/

### PostgreSQL
- Official Docs: https://www.postgresql.org/docs/

### Khalti Payment
- Integration Guide: https://docs.khalti.com/

---

## 💡 Pro Tips

1. **Use API Documentation**
   - Visit http://localhost:8000/swagger/
   - Test endpoints interactively
   - View request/response formats

2. **Enable Debug Toolbar**
   - Already configured in development
   - View SQL queries
   - Check performance

3. **Use React Native Debugger**
   - Install React Native Debugger
   - Debug Redux state
   - Inspect network requests

4. **Hot Reload**
   - Backend: Auto-reloads on file changes
   - Mobile: Shake device → Enable Fast Refresh

5. **Database GUI**
   - Use pgAdmin or DBeaver
   - Visual database management
   - Easy data inspection

---

## 🤝 Getting Help

### Documentation
- Check README.md for detailed info
- Review code comments
- Read API documentation

### Community
- GitHub Issues: Report bugs
- Stack Overflow: Ask questions
- Discord/Slack: Join community

### Support
- Email: support@smartschoolerp.com
- GitHub: Create issue with details
- Documentation: Check guides

---

## ✅ Checklist

Before you start development:

- [ ] Backend running successfully
- [ ] Mobile app running on emulator
- [ ] Admin panel accessible
- [ ] API documentation working
- [ ] Sample data created
- [ ] All features tested
- [ ] Documentation reviewed
- [ ] Development environment ready

---

## 🎉 You're All Set!

Congratulations! You now have a fully functional Smart School ERP System running locally.

**Happy Coding! 🚀**

---

## 📞 Quick Links

- **Backend:** http://localhost:8000
- **Admin Panel:** http://localhost:8000/admin/
- **API Docs:** http://localhost:8000/swagger/
- **API Root:** http://localhost:8000/api/v1/

---

**Built with ❤️ during Django & React Full-Stack Internship**  
**Code IT, Dharan, Nepal**
