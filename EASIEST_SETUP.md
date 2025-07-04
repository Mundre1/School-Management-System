# ⚡ EASIEST SETUP - 3 Commands Only!

## 🎯 No PostgreSQL Needed - Uses SQLite Instead!

I've configured the project to use SQLite by default, so you don't need to install PostgreSQL!

---

## 🚀 Option 1: Automated Setup (Recommended)

Just run this one command:

```bash
cd "/Users/ayush/Desktop/School /smart-school-erp" && ./RUN_NOW.sh
```

That's it! The script will:
- ✅ Create virtual environment
- ✅ Install all dependencies
- ✅ Setup database (SQLite)
- ✅ Ask you to create admin user
- ✅ Start the server

---

## 🔧 Option 2: Manual Setup (3 Commands)

If you prefer manual setup:

### Command 1: Install Dependencies
```bash
cd "/Users/ayush/Desktop/School /smart-school-erp/backend"
source venv/bin/activate
pip install -r requirements-sqlite.txt
```

### Command 2: Setup Database
```bash
python manage.py migrate
python manage.py createsuperuser
```

When prompted:
- Email: `admin@school.com`
- First name: `Admin`
- Last name: `User`
- Password: `admin123`

### Command 3: Start Server
```bash
python manage.py runserver
```

---

## ✅ Access Your Application

Once the server starts, open in browser:

1. **Admin Panel:** http://localhost:8000/admin/
   - Login: admin@school.com / admin123

2. **API Documentation:** http://localhost:8000/swagger/
   - Interactive API testing

3. **API Root:** http://localhost:8000/api/v1/
   - JSON API endpoints

---

## 🎨 What You Can Do Now

### In Admin Panel (http://localhost:8000/admin/)
- ✅ Create students
- ✅ Create staff/teachers
- ✅ Create classes
- ✅ Create courses
- ✅ Manage users
- ✅ View all data

### In API Docs (http://localhost:8000/swagger/)
- ✅ Test authentication
- ✅ Try API endpoints
- ✅ See request/response formats
- ✅ Test CRUD operations

---

## 📱 Setup Mobile App (Optional)

Once backend is running, open a **new terminal**:

```bash
cd "/Users/ayush/Desktop/School /smart-school-erp/mobile-app"
npm install
cp .env.example .env
npm start
```

Then in **another new terminal**:
```bash
cd "/Users/ayush/Desktop/School /smart-school-erp/mobile-app"
npm run ios
# or
npm run android
```

---

## 🔄 Switch to PostgreSQL Later (Optional)

When you want to use PostgreSQL:

1. Install PostgreSQL:
   ```bash
   brew install postgresql@15
   brew services start postgresql@15
   ```

2. Edit `.env` file:
   ```bash
   USE_SQLITE=False
   DB_NAME=school_erp_db
   DB_USER=postgres
   DB_PASSWORD=your_password
   ```

3. Install psycopg2:
   ```bash
   pip install psycopg2-binary
   ```

4. Create database:
   ```bash
   createdb school_erp_db
   python manage.py migrate
   ```

---

## 🐛 Troubleshooting

### "Module not found" error
```bash
source venv/bin/activate
pip install -r requirements-sqlite.txt
```

### "Port 8000 already in use"
```bash
lsof -ti:8000 | xargs kill -9
python manage.py runserver
```

### "Permission denied" for RUN_NOW.sh
```bash
chmod +x RUN_NOW.sh
./RUN_NOW.sh
```

---

## 📚 Next Steps

1. ✅ **Explore Admin Panel** - Create sample data
2. ✅ **Test API** - Use Swagger UI
3. ✅ **Read Documentation** - Check README.md
4. ✅ **Setup Mobile App** - Follow instructions above
5. ✅ **Customize** - Add your school's data

---

## 🎉 You're All Set!

Your Smart School ERP System is now running with:
- ✅ Django REST Framework backend
- ✅ JWT authentication
- ✅ Role-based access control
- ✅ SQLite database (easy development)
- ✅ Admin panel
- ✅ API documentation
- ✅ 100+ API endpoints

**Start building your school management system! 🚀**

---

## 📞 Need Help?

Check these files:
- **QUICK_FIX.md** - SQLite setup details
- **INSTALL_POSTGRESQL.md** - PostgreSQL installation
- **INSTALLATION_GUIDE.md** - Complete guide
- **API_DOCUMENTATION.md** - API reference

---

**Happy Coding! 🎓**
