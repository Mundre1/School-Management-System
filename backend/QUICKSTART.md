# 🚀 Quick Start Guide - Itahari International School

## For VS Code Users (Easiest Method)

### Step 1: Open Project
```bash
cd "/Users/ayush/Desktop/School /smart-school-erp"
code .
```

### Step 2: Open Terminal in VS Code
Press `` Ctrl + ` `` (backtick) or go to Terminal → New Terminal

### Step 3: Run the Project
```bash
npm run dev
```

**That's it!** Both servers will start automatically:
- ✅ Backend: http://127.0.0.1:8000/
- ✅ Frontend: http://localhost:3001/

### Step 4: Login
Open browser: http://localhost:3001

**Credentials:**
- Email: `admin@school.com`
- Password: `admin123`

---

## Alternative: Run Servers Separately

### Terminal 1 - Backend
```bash
cd backend
npm run dev
```

### Terminal 2 - Frontend
```bash
cd frontend
npm start
```

---

## 📋 All Available Commands

### From Root Directory:
```bash
npm run dev              # 🚀 Run both servers (RECOMMENDED)
npm run backend          # Run only backend
npm run frontend         # Run only frontend
npm run install-all      # Install all dependencies
```

### Backend Commands:
```bash
cd backend
npm run dev              # Start server
npm run migrate          # Update database
npm run createsuperuser  # Create new admin
```

### Frontend Commands:
```bash
cd frontend
npm start                # Start React app
npm run build            # Build for production
```

---

## 🔧 First Time Setup

If this is your first time running the project:

```bash
# Install all dependencies
npm run install-all

# Or install separately:
pip3 install -r backend/requirements.txt  # Backend
cd frontend && npm install                 # Frontend
```

---

## ✅ System Features

### Dashboard
- Real-time statistics (Students, Teachers, Parents, Earnings)
- Monthly earnings chart
- Top performers leaderboard
- Attendance tracking
- Events calendar

### Modules
- 👨‍🎓 Students Management
- 👨‍🏫 Staff Management
- 📅 Attendance Tracking
- 💰 Fee Management
- 📊 Results & Grades
- 📚 Library Management
- 📢 Communication & Notices
- 📝 Assignments & Homework
- 🗓️ Timetable Management
- 🎉 Events Management
- 📋 Leave Applications
- 📈 Analytics Dashboard

---

## 🎯 Quick Tips

### Stop Servers
Press `Ctrl + C` in the terminal

### View Logs
All logs appear in the terminal where you ran `npm run dev`

### Database Location
`backend/db.sqlite3` - SQLite database file

### API Documentation
Backend API: http://127.0.0.1:8000/api/

---

## 🆘 Troubleshooting

### Port Already in Use
```bash
# Kill process on port 8000 (backend)
lsof -ti:8000 | xargs kill -9

# Kill process on port 3001 (frontend)
lsof -ti:3001 | xargs kill -9
```

### Module Not Found (Backend)
```bash
cd backend
pip3 install -r requirements.txt
```

### Dependencies Error (Frontend)
```bash
cd frontend
rm -rf node_modules package-lock.json
npm install
```

### Database Issues
```bash
cd backend
python3 manage.py migrate
```

---

## 📱 Access Points

| Service | URL | Purpose |
|---------|-----|---------|
| Frontend | http://localhost:3001 | Main Application |
| Backend API | http://127.0.0.1:8000 | REST API |
| Admin Panel | http://127.0.0.1:8000/admin | Django Admin |

---

## 🎓 Default Login

**Admin Account:**
- Email: admin@school.com
- Password: admin123

**Note:** Change these credentials in production!

---

## 📞 Need Help?

Check the main README.md for detailed documentation.

---

**Happy Coding! 🎉**

Built for Itahari International School with ❤️
