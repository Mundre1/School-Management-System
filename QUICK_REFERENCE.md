# 🚀 Quick Reference Guide

## System Access

### URLs
- **Frontend:** http://localhost:3001
- **Backend API:** http://localhost:8000
- **Admin Panel:** http://localhost:8000/admin

### Login Credentials
- **Email:** admin@school.com
- **Password:** admin123

---

## Working Pages

### Dashboard
**URL:** http://localhost:3001/dashboard  
**Features:** Charts, Timetable, Events, Quick Actions

### Students Module
- **List:** http://localhost:3001/students
- **Add:** http://localhost:3001/students/add
- **View:** http://localhost:3001/students/{id}
- **Edit:** http://localhost:3001/students/edit/{id}

### Staff Module
- **List:** http://localhost:3001/staff

### Attendance Module
- **View:** http://localhost:3001/attendance

### Fees Module
- **View:** http://localhost:3001/fees

### Results Module
- **View:** http://localhost:3001/results

---

## Quick Actions (Dashboard Buttons)

1. **Students** → View all students
2. **Add Student** → Add new student
3. **Staff** → View all staff
4. **Attendance** → View attendance
5. **Fees** → View fee payments
6. **Results** → View exam results

---

## API Endpoints

### Authentication
```
POST /auth/login/
POST /auth/logout/
POST /auth/token/refresh/
```

### Students
```
GET    /students/students/
POST   /students/students/
GET    /students/students/{id}/
PUT    /students/students/{id}/
DELETE /students/students/{id}/
```

### Staff
```
GET    /staff/staff/
POST   /staff/staff/
GET    /staff/staff/{id}/
PUT    /staff/staff/{id}/
DELETE /staff/staff/{id}/
```

### Attendance
```
GET  /attendance/attendance/
POST /attendance/attendance/
POST /attendance/attendance/bulk_mark/
GET  /attendance/attendance/statistics/
GET  /attendance/attendance/by_date/?date=YYYY-MM-DD
```

### Fees
```
GET  /fees/structures/
POST /fees/structures/
GET  /fees/payments/
POST /fees/payments/
GET  /fees/payments/statistics/
GET  /fees/payments/pending/
POST /fees/payments/{id}/make_payment/
```

### Results
```
GET  /results/exams/
POST /results/exams/
GET  /results/subjects/
POST /results/subjects/
GET  /results/results/
POST /results/results/
POST /results/results/bulk_create/
GET  /results/results/statistics/?exam={id}
GET  /results/results/student_report/?student_id={id}&exam_id={id}
```

---

## Server Commands

### Start Backend
```bash
cd backend
source venv/bin/activate
python manage.py runserver
```

### Start Frontend
```bash
cd frontend
PORT=3001 npm start
```

### Stop Servers
Press `Ctrl+C` in the terminal running the server

---

## Database Commands

### Create Migrations
```bash
cd backend
source venv/bin/activate
python manage.py makemigrations
```

### Apply Migrations
```bash
python manage.py migrate
```

### Create Superuser
```bash
python manage.py createsuperuser
```

### Access Django Shell
```bash
python manage.py shell
```

---

## Common Tasks

### Add a Student
1. Go to http://localhost:3001/students/add
2. Fill in the form
3. Click "Add Student"

### View Student Profile
1. Go to http://localhost:3001/students
2. Click "View" on any student
3. See full profile details

### Edit Student
1. From student profile, click "Edit Profile"
2. Update information
3. Click "Update Student"

### View Attendance
1. Go to http://localhost:3001/attendance
2. Select date
3. View attendance records

### Check Fee Payments
1. Go to http://localhost:3001/fees
2. View statistics dashboard
3. Filter by payment status

### View Results
1. Go to http://localhost:3001/results
2. Select exam from dropdown
3. View results with grades

---

## Module Status

### ✅ Complete (100%)
- Authentication
- Students Management

### ✅ Working (70%)
- Staff Management (list only)
- Attendance (view only)
- Fees (view only)
- Results (view only)

### ⏳ Not Started (0%)
- Courses
- Timetable
- Assignments
- Communication
- Library
- Events
- Leave
- Analytics

---

## Progress: 55%

**Backend:** 50% (5 of 13 modules)  
**Frontend:** 60% (5 modules with pages)  
**Overall:** 55% Complete

---

## Next Steps

1. **Add Forms** - Create Add/Edit forms for Staff, Attendance, Fees, Results
2. **Khalti Integration** - Add payment gateway
3. **More Modules** - Build remaining 8 modules
4. **Advanced Features** - QR codes, PDFs, notifications

---

## Troubleshooting

### Frontend Not Loading
```bash
cd frontend
npm install
PORT=3001 npm start
```

### Backend Errors
```bash
cd backend
source venv/bin/activate
python manage.py migrate
python manage.py runserver
```

### CORS Errors
Check `backend/core/settings.py`:
```python
CORS_ALLOW_ALL_ORIGINS = True  # For development
```

### Database Issues
```bash
cd backend
rm db.sqlite3
python manage.py migrate
python manage.py createsuperuser
```

---

## File Structure

```
smart-school-erp/
├── backend/
│   ├── apps/
│   │   ├── authentication/
│   │   ├── students/
│   │   ├── staff/
│   │   ├── attendance/
│   │   ├── fees/
│   │   └── results/
│   ├── core/
│   │   ├── settings.py
│   │   └── urls.py
│   ├── manage.py
│   └── db.sqlite3
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── auth/
│   │   │   ├── dashboard/
│   │   │   ├── students/
│   │   │   ├── staff/
│   │   │   ├── attendance/
│   │   │   ├── fees/
│   │   │   └── results/
│   │   ├── services/
│   │   ├── context/
│   │   └── App.js
│   └── package.json
└── Documentation files
```

---

## Important Notes

- ✅ Both servers must be running
- ✅ Backend on port 8000
- ✅ Frontend on port 3001
- ✅ Login required for all pages except login
- ✅ JWT tokens stored in localStorage
- ✅ CORS enabled for development

---

## Support

### Documentation Files
- `FINAL_STATUS.md` - Complete system status
- `ALL_MODULES_COMPLETE.md` - Module details
- `CURRENT_STATE.md` - Current progress
- `STUDENTS_MODULE_COMPLETE.md` - Students guide

### Need Help?
1. Check documentation files
2. Check browser console for errors
3. Check terminal for server errors
4. Verify both servers are running

---

**Last Updated:** May 27, 2026  
**Status:** ✅ Live and Running  
**Progress:** 55% Complete
