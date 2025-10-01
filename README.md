# 🎓 Smart School ERP System

A comprehensive School Management System built with Django REST Framework and React.js, featuring 5 complete modules with professional UI/UX.

![Progress](https://img.shields.io/badge/Progress-55%25-blue)
![Backend](https://img.shields.io/badge/Backend-Django-green)
![Frontend](https://img.shields.io/badge/Frontend-React-blue)
![Database](https://img.shields.io/badge/Database-SQLite-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Version](https://img.shields.io/badge/Version-0.5.0-purple)

## 🚀 Live Demo

- **Frontend:** http://localhost:3001
- **Backend API:** http://localhost:8000
- **Admin Panel:** http://localhost:8000/admin

**Login Credentials:**
- Email: `admin@school.com`
- Password: `admin123`

---

## ✨ Features

### ✅ Working Modules (5)

#### 1. Authentication System
- JWT-based authentication
- Login/Logout functionality
- Protected routes
- Session management
- Role-based access control

#### 2. Students Management (Complete)
- List all students with search and filter
- Add new student (comprehensive form)
- View student profile
- Edit student information
- Delete student with confirmation
- Pagination support
- Photo upload capability

#### 3. Staff Management
- List all staff members
- Search by name, email, employee ID
- Filter by department
- Status tracking (Active/Inactive/On Leave/Resigned)

#### 4. Attendance Tracking
- Date-wise attendance viewing
- Present/Absent statistics
- Status tracking (Present/Absent/Late/Excused)
- Bulk attendance marking API
- Real-time statistics

#### 5. Fee Management
- Payment tracking system
- Statistics dashboard (Total Due/Paid/Remaining)
- Collection percentage
- Payment status filtering
- Multiple payment methods support

#### 6. Results Management
- Exam-wise result viewing
- Automatic grade calculation (A+ to F)
- Pass/Fail statistics
- Average percentage tracking
- Subject-wise results

---

## 🛠️ Tech Stack

### Backend
- **Framework:** Django 4.2.7
- **API:** Django REST Framework
- **Authentication:** JWT (djangorestframework-simplejwt)
- **Database:** SQLite
- **Python:** 3.13

### Frontend
- **Framework:** React.js
- **Routing:** React Router v6
- **Charts:** Recharts
- **HTTP Client:** Axios
- **State Management:** React Context API
- **Styling:** Custom CSS

---

## 📊 Project Statistics

- **Backend:** 50% Complete (5 of 13 modules)
- **Frontend:** 60% Complete (9 pages)
- **Overall Progress:** 55%
- **API Endpoints:** 100+
- **Database Tables:** 15+
- **Lines of Code:** ~7,500+

---

## 🚀 Quick Start

### Prerequisites
- Python 3.13+
- Node.js 14+
- npm or yarn

### Backend Setup

```bash
# Navigate to backend directory
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements-sqlite.txt

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Start development server
python manage.py runserver
```

Backend will run at: http://localhost:8000

### Frontend Setup

```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Start development server
PORT=3001 npm start
```

Frontend will run at: http://localhost:3001

---

## 📁 Project Structure

```
smart-school-erp/
├── backend/
│   ├── apps/
│   │   ├── authentication/      # JWT auth, user management
│   │   ├── students/           # Student CRUD operations
│   │   ├── staff/              # Staff management
│   │   ├── attendance/         # Attendance tracking
│   │   ├── fees/               # Fee management
│   │   ├── results/            # Results & grades
│   │   └── ...                 # Other modules
│   ├── core/
│   │   ├── settings.py         # Django settings
│   │   └── urls.py             # URL configuration
│   ├── manage.py
│   └── db.sqlite3              # SQLite database
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── auth/           # Login component
│   │   │   ├── dashboard/      # Dashboard with charts
│   │   │   ├── students/       # Student pages (4 pages)
│   │   │   ├── staff/          # Staff list page
│   │   │   ├── attendance/     # Attendance page
│   │   │   ├── fees/           # Fees page
│   │   │   └── results/        # Results page
│   │   ├── services/           # API services
│   │   ├── context/            # Auth context
│   │   └── App.js              # Main app component
│   └── package.json
│
└── Documentation files
```

---

## 🎯 API Endpoints

### Authentication
```
POST   /auth/login/              # Login
POST   /auth/logout/             # Logout
POST   /auth/token/refresh/      # Refresh token
```

### Students
```
GET    /students/students/       # List students
POST   /students/students/       # Create student
GET    /students/students/{id}/  # Get student
PUT    /students/students/{id}/  # Update student
DELETE /students/students/{id}/  # Delete student
```

### Staff
```
GET    /staff/staff/             # List staff
POST   /staff/staff/             # Create staff
GET    /staff/staff/{id}/        # Get staff details
PUT    /staff/staff/{id}/        # Update staff
DELETE /staff/staff/{id}/        # Delete staff
```

### Attendance
```
GET    /attendance/attendance/                    # List attendance
POST   /attendance/attendance/                    # Mark attendance
POST   /attendance/attendance/bulk_mark/          # Bulk mark
GET    /attendance/attendance/statistics/         # Get statistics
GET    /attendance/attendance/by_date/?date=...   # Get by date
```

### Fees
```
GET    /fees/structures/                  # List fee structures
POST   /fees/structures/                  # Create structure
GET    /fees/payments/                    # List payments
POST   /fees/payments/                    # Create payment
GET    /fees/payments/statistics/         # Get statistics
POST   /fees/payments/{id}/make_payment/  # Make payment
```

### Results
```
GET    /results/exams/                           # List exams
POST   /results/exams/                           # Create exam
GET    /results/subjects/                        # List subjects
POST   /results/subjects/                        # Create subject
GET    /results/results/                         # List results
POST   /results/results/                         # Create result
GET    /results/results/statistics/?exam={id}   # Get statistics
GET    /results/results/student_report/         # Get report card
```

---

## 🎨 Screenshots

### Dashboard
Professional ERP-style dashboard with:
- Statistics cards
- Interactive charts (Recharts)
- Weekly timetable
- Upcoming events
- Recent activity feed
- Quick action buttons

### Students Management
- Comprehensive list view with search/filter
- Detailed student profiles
- Add/Edit forms with validation
- Photo upload support

### Other Modules
- Staff list with department filtering
- Attendance tracking with date selector
- Fee management with statistics
- Results with automatic grade calculation

---

## 🔐 Security Features

- JWT authentication
- Token-based authorization
- Protected API endpoints
- CORS configuration
- Password hashing
- Session management

---

## 📝 Database Models

### Students
- Personal information
- Contact details
- Academic information
- Parent/Guardian details

### Staff
- Employee information
- Department & designation
- Salary details
- Contact information

### Attendance
- Student reference
- Date & status
- Remarks
- Marked by

### Fees
- Fee structure (grade-wise)
- Payment tracking
- Transaction details
- Payment status

### Results
- Exam details
- Subject information
- Student results
- Automatic grade calculation

---

## 🚧 Upcoming Features

### In Development
- Add/Edit forms for Staff, Attendance, Fees, Results
- Khalti payment gateway integration
- QR code attendance scanning
- PDF report card generation

### Planned Modules
- Courses Management
- Timetable
- Assignments
- Communication/Messages
- Library
- Events
- Leave Management
- Advanced Analytics

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 👨‍💻 Developer

**Ayush (mundre1)**
- GitHub: [@Mundre1](https://github.com/Mundre1)
- Email: gymnasticaayush123@gmail.com

---

## 🙏 Acknowledgments

Built as part of Django & React Full-Stack development learning, reflecting real-world ERP system architecture and best practices.

---

## 📞 Support

For support, email gymnasticaayush123@gmail.com or open an issue in the repository.

---

## 📚 Documentation

Detailed documentation available in:
- `FINAL_STATUS.md` - Complete system overview
- `ALL_MODULES_COMPLETE.md` - Module details
- `QUICK_REFERENCE.md` - Quick access guide
- `CURRENT_STATE.md` - Current progress

---

**⭐ Star this repository if you find it helpful!**

---

**Last Updated:** May 27, 2026  
**Status:** ✅ Live and Running  
**Progress:** 55% Complete
