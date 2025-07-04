# 🎯 FINAL SETUP - Copy & Paste This!

## ⚡ ONE COMMAND TO RULE THEM ALL

Just copy and paste this into your terminal:

```bash
cd "/Users/ayush/Desktop/School /smart-school-erp/backend" && ./setup_and_run.sh
```

**That's it!** Everything will be done automatically! 🚀

---

## 📝 What This Does:

1. ✅ Activates virtual environment
2. ✅ Installs Django and all dependencies
3. ✅ Creates database (SQLite)
4. ✅ Asks you to create admin user
5. ✅ Starts the server

---

## 🔑 When Asked for Admin User:

Just enter these:
- **Email:** admin@school.com
- **First name:** Admin
- **Last name:** User
- **Password:** admin123

---

## ✅ After Server Starts:

Open in your browser:

### 1. Admin Panel
```
http://localhost:8000/admin/
```
Login: admin@school.com / admin123

### 2. API Documentation
```
http://localhost:8000/swagger/
```

### 3. API Root
```
http://localhost:8000/api/v1/
```

---

## 🎉 Success!

You now have a fully working Smart School ERP System!

**Features:**
- ✅ Django REST Framework backend
- ✅ JWT authentication
- ✅ Admin panel
- ✅ API documentation
- ✅ 100+ API endpoints
- ✅ Role-based access control

---

## 📱 Next: Setup Mobile App (Optional)

Open a **new terminal** and run:

```bash
cd "/Users/ayush/Desktop/School /smart-school-erp/mobile-app"
npm install
cp .env.example .env
npm start
```

Then in **another terminal**:
```bash
cd "/Users/ayush/Desktop/School /smart-school-erp/mobile-app"
npm run ios
```

---

## 🐛 If Script Doesn't Run:

Make it executable:
```bash
chmod +x "/Users/ayush/Desktop/School /smart-school-erp/backend/setup_and_run.sh"
```

Then run again:
```bash
cd "/Users/ayush/Desktop/School /smart-school-erp/backend" && ./setup_and_run.sh
```

---

## 🔄 To Run Again Later:

Just run:
```bash
cd "/Users/ayush/Desktop/School /smart-school-erp/backend"
source venv/bin/activate
python manage.py runserver
```

---

## 📚 Documentation:

All documentation is in the project root:
- **README.md** - Complete documentation
- **API_DOCUMENTATION.md** - API reference
- **INSTALLATION_GUIDE.md** - Full guide
- **DEPLOYMENT_GUIDE.md** - Production deployment

---

**🎓 Your Smart School ERP System is Ready! 🚀**
