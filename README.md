# Smart School ERP System

## 🎓 Production-Level School Management System

A comprehensive, enterprise-grade School ERP system built with Django REST Framework and React.js, reflecting real-world full-stack development experience from Code IT internship, Dharan, Nepal.

---

## 🚀 Project Overview

**Project Type:** Full-Stack School Management ERP System  
**Developer:** Django & React Full-Stack Intern  
**Company:** Code IT, Dharan, Nepal  
**Tech Stack:** Django REST Framework + React.js + PostgreSQL + JWT Authentication

---

## 👥 User Roles & Access Control

### 1. Head of School (Admin)
- Complete system management
- Student & Staff CRUD operations
- Fee management & analytics
- Attendance tracking & reports
- Results & examination management
- Timetable scheduling
- Library management
- Event & calendar management
- Analytics dashboard with charts
- Leave request approvals
- System configuration

### 2. Staff / Teacher
- View students & staff
- Manage attendance (QR/One-tap)
- Upload results & marks
- Manage assigned classes
- Upload assignments
- Send notices & messages
- View timetable
- Track student performance
- Approve student leave requests

### 3. Student
- View personal profile
- View courses & classes
- Check attendance records
- View fee/payment history
- View results & grades
- Access assignments
- View timetable
- Receive notifications
- Chat with teachers
- Submit leave requests
- Download reports (PDF)

---

## 🛠️ Technology Stack

### Backend
- **Python 3.10+**
- **Django 4.2+**
- **Django REST Framework (DRF)**
- **djangorestframework-simplejwt** - JWT Authentication
- **PostgreSQL** - Production Database
- **Django Signals** - Event-driven actions
- **Python-Decouple** - Environment variables
- **WhiteNoise** - Static file serving
- **django-cors-headers** - CORS handling
- **Pillow** - Image processing
- **django-filter** - Advanced filtering
- **celery** - Async task processing
- **redis** - Caching & message broker

### Frontend
- **React.js 18+**
- **Tailwind CSS** - Modern styling
- **Axios** - HTTP client
- **React Router v6** - Navigation
- **React Query** - Data fetching
- **Recharts** - Analytics charts
- **React Hot Toast** - Notifications
- **Framer Motion** - Animations
- **Headless UI** - Accessible components
- **React Icons** - Icon library

### Deployment
- **PythonAnywhere** - Hosting platform
- **PostgreSQL** - Production database
- **WSGI** - Application server
- **WhiteNoise** - Static files
- **Environment Variables** - Secure configuration
- **HTTPS** - Secure communication

### Development Tools
- **Git & GitHub** - Version control
- **Trello** - Project management
- **Postman** - API testing
- **Notion** - Documentation
- **VS Code** - IDE

---

## 📦 Main Modules

### 1. Authentication System
- Email/Password login
- Phone OTP login
- JWT access + refresh tokens
- Token blacklisting
- Password reset via email
- Email verification
- Role-based permissions
- Session management

### 2. Student Management
- Complete CRUD operations
- Student profiles with photos
- Parent details
- Academic history
- Advanced search & filters
- Server-side pagination
- CSV bulk import
- Student ID cards

### 3. Staff Management
- Teacher/Staff profiles
- Department management
- Subject assignments
- Staff attendance
- Performance tracking

### 4. Course & Class Management
- Subjects & courses
- Sections & semesters
- Classroom allocation
- Course enrollment
- Academic year management

### 5. Attendance System
- Daily attendance marking
- QR code attendance
- Face recognition (AI)
- Monthly reports
- Attendance analytics
- Late/Absent tracking
- Parent notifications

### 6. Fee Management System
**Reflecting Internship Fee Payment Project:**
- Fee structure management
- Pending/Paid status tracking
- **Khalti Payment Gateway Integration**
- Server-side payment verification
- Payment email notifications (Django Signals)
- Receipt generation (PDF)
- Due date reminders
- Financial analytics dashboard
- Payment history
- Multi-fee categories

### 7. Result & Examination System
- Marks entry & management
- GPA calculation
- Result publishing
- PDF report cards
- Result analytics
- Performance graphs
- Grade management
- Exam scheduling

### 8. Timetable System
- Weekly schedule generation
- Teacher timetable
- Student timetable
- Conflict detection
- Period management
- Room allocation

### 9. Assignment & Homework
- Assignment upload
- Submission tracking
- Deadline reminders
- File upload support
- Grading system
- Feedback mechanism

### 10. Communication System
- Real-time chat
- Announcements
- Push notifications
- Emergency alerts
- Group messaging
- Email integration

### 11. Analytics Dashboard
**Admin Dashboard Features:**
- Total students & staff count
- Attendance analytics (charts)
- Fee collection graphs
- Top performers list
- Revenue analytics
- Department statistics
- Interactive charts (Recharts)
- Export reports (PDF/Excel)

### 12. Library Management
- Book inventory
- Borrow/Return system
- Due date reminders
- Fine calculation
- Book search
- Availability tracking

### 13. Event & Calendar
- School events
- Holiday calendar
- Exam schedules
- Academic calendar
- Event notifications

### 14. Leave Management
- Student leave requests
- Staff leave requests
- Approval workflow
- Leave balance tracking
- Leave history

---

## 🤖 AI-Powered Features

1. **AI Chatbot Assistant** - Student query handling
2. **AI Attendance Prediction** - Predict student attendance patterns
3. **AI Performance Analysis** - Analyze student performance trends
4. **AI Study Recommendations** - Personalized study suggestions
5. **AI Report Summaries** - Auto-generate report summaries
6. **AI Notice Summarizer** - Summarize long notices
7. **Smart Timetable Optimization** - AI-optimized scheduling

---

## 🎨 UI/UX Features

- Modern premium ERP design
- Mobile-first responsive layout
- Dark/Light mode toggle
- Smooth animations (Framer Motion)
- Professional dashboard cards
- Interactive charts & analytics
- Beautiful login screens
- Reusable React components
- Loading states & skeletons
- Error handling & validation
- Toast notifications
- Material-style professional layout
- Real-world SaaS appearance

---

## 🔐 Security Features

- JWT Authentication
- Token blacklisting
- Role-based access control (RBAC)
- Protected API routes
- CORS configuration
- Environment variable security
- SQL injection prevention
- XSS protection
- CSRF protection
- Secure password hashing
- Rate limiting
- Audit logs

---

## 📊 Database Schema

### Core Tables
- **Users** - Authentication & user management
- **Students** - Student information
- **Staff** - Staff/Teacher information
- **Courses** - Course catalog
- **Subjects** - Subject management
- **Classes** - Class sections
- **Attendance** - Attendance records
- **Fees** - Fee structure
- **Payments** - Payment transactions
- **Results** - Exam results
- **Assignments** - Homework assignments
- **Messages** - Communication
- **Notifications** - System notifications
- **Events** - School events
- **Timetables** - Schedule management
- **LeaveRequests** - Leave applications
- **LibraryBooks** - Library inventory

**Database Design:**
- Optimized ForeignKey relationships
- ManyToMany relationships
- Indexed fields for performance
- select_related & prefetch_related optimization
- Database-level constraints

---

## 🚀 Installation Guide

### Prerequisites
- Python 3.10+
- Node.js 16+
- PostgreSQL 13+
- Git

### Backend Setup

```bash
# Clone repository
git clone https://github.com/yourusername/smart-school-erp.git
cd smart-school-erp

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
cd backend
pip install -r requirements.txt

# Setup environment variables
cp .env.example .env
# Edit .env with your configuration

# Database setup
python manage.py makemigrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Load sample data (optional)
python manage.py loaddata sample_data.json

# Collect static files
python manage.py collectstatic --noinput

# Run development server
python manage.py runserver
```

### Frontend Setup

```bash
# Navigate to frontend
cd frontend

# Install dependencies
npm install

# Setup environment variables
cp .env.example .env
# Edit .env with your API URL

# Run development server
npm start

# Build for production
npm run build
```

---

## 🌐 API Documentation

### Authentication Endpoints
```
POST /api/auth/register/          - User registration
POST /api/auth/login/             - User login
POST /api/auth/logout/            - User logout
POST /api/auth/token/refresh/     - Refresh JWT token
POST /api/auth/password/reset/    - Password reset request
POST /api/auth/password/confirm/  - Password reset confirm
POST /api/auth/verify-email/      - Email verification
```

### Student Endpoints
```
GET    /api/students/             - List all students
POST   /api/students/             - Create student
GET    /api/students/{id}/        - Get student details
PUT    /api/students/{id}/        - Update student
DELETE /api/students/{id}/        - Delete student
POST   /api/students/bulk-import/ - CSV bulk import
GET    /api/students/export/      - Export students
```

### Attendance Endpoints
```
GET    /api/attendance/           - List attendance
POST   /api/attendance/           - Mark attendance
GET    /api/attendance/report/    - Attendance report
POST   /api/attendance/qr/        - QR attendance
GET    /api/attendance/analytics/ - Attendance analytics
```

### Fee & Payment Endpoints
```
GET    /api/fees/                 - List fees
POST   /api/fees/                 - Create fee
GET    /api/payments/             - Payment history
POST   /api/payments/khalti/      - Khalti payment
POST   /api/payments/verify/      - Verify payment
GET    /api/payments/receipt/{id}/- Download receipt
```

### Results Endpoints
```
GET    /api/results/              - List results
POST   /api/results/              - Create result
GET    /api/results/{id}/pdf/     - Download report card
GET    /api/results/analytics/    - Result analytics
```

**Full API documentation available in `/docs/api/` directory**

---

## 📱 Deployment Guide

### PythonAnywhere Deployment

1. **Create PythonAnywhere Account**
   - Sign up at pythonanywhere.com
   - Choose appropriate plan

2. **Upload Code**
   ```bash
   git clone https://github.com/yourusername/smart-school-erp.git
   cd smart-school-erp/backend
   ```

3. **Setup Virtual Environment**
   ```bash
   mkvirtualenv --python=/usr/bin/python3.10 school-erp
   pip install -r requirements.txt
   ```

4. **Configure PostgreSQL**
   - Create database in PythonAnywhere
   - Update .env with database credentials

5. **WSGI Configuration**
   - Configure WSGI file (see deployment/wsgi.py)
   - Set static files path
   - Set media files path

6. **Environment Variables**
   ```bash
   export SECRET_KEY='your-secret-key'
   export DEBUG=False
   export ALLOWED_HOSTS='yourdomain.pythonanywhere.com'
   export DATABASE_URL='postgresql://...'
   ```

7. **Collect Static Files**
   ```bash
   python manage.py collectstatic --noinput
   ```

8. **Run Migrations**
   ```bash
   python manage.py migrate
   ```

9. **Reload Web App**
   - Click "Reload" button in PythonAnywhere dashboard

**Detailed deployment guide in `/docs/deployment.md`**

---

## 🧪 Testing

### Backend Testing
```bash
# Run all tests
python manage.py test

# Run specific app tests
python manage.py test apps.students

# Run with coverage
coverage run --source='.' manage.py test
coverage report
```

### API Testing with Postman
- Import Postman collection from `/docs/postman/`
- Configure environment variables
- Run test suites

### Frontend Testing
```bash
# Run tests
npm test

# Run with coverage
npm test -- --coverage
```

---

## 📁 Project Structure

```
smart-school-erp/
├── backend/
│   ├── apps/
│   │   ├── authentication/
│   │   ├── students/
│   │   ├── staff/
│   │   ├── courses/
│   │   ├── attendance/
│   │   ├── fees/
│   │   ├── results/
│   │   ├── timetable/
│   │   ├── assignments/
│   │   ├── communication/
│   │   ├── library/
│   │   ├── events/
│   │   └── leave/
│   ├── core/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── utils/
│   ├── media/
│   ├── static/
│   ├── manage.py
│   ├── requirements.txt
│   └── .env.example
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   │   ├── common/
│   │   │   ├── dashboard/
│   │   │   ├── students/
│   │   │   ├── staff/
│   │   │   ├── attendance/
│   │   │   ├── fees/
│   │   │   └── results/
│   │   ├── pages/
│   │   ├── services/
│   │   ├── utils/
│   │   ├── hooks/
│   │   ├── context/
│   │   ├── App.js
│   │   └── index.js
│   ├── package.json
│   ├── tailwind.config.js
│   └── .env.example
├── docs/
│   ├── api/
│   ├── deployment/
│   ├── erd/
│   └── postman/
├── deployment/
│   ├── wsgi.py
│   └── nginx.conf
├── .gitignore
├── README.md
└── LICENSE
```

---

## 🎯 Key Features Implemented

✅ JWT Authentication with refresh tokens  
✅ Role-based access control (Admin, Staff, Student)  
✅ Student management with CSV import  
✅ Staff management with department allocation  
✅ Attendance system with QR code  
✅ Fee management with Khalti payment gateway  
✅ Result management with PDF report cards  
✅ Timetable generation with conflict detection  
✅ Assignment submission system  
✅ Real-time communication  
✅ Analytics dashboard with charts  
✅ Library management  
✅ Event calendar  
✅ Leave management workflow  
✅ AI-powered features  
✅ Mobile-responsive design  
✅ Dark/Light mode  
✅ Email notifications  
✅ PDF/Excel export  
✅ Production-ready deployment  

---

## 🏆 Premium Features

- Face recognition attendance
- QR code student ID generation
- Parent portal access
- GPS-enabled bus tracking
- Digital ID cards
- Smart announcements
- Voice notifications
- Multi-language support
- Cloud backup system
- Comprehensive audit logs
- Activity tracking
- Biometric login integration

---

## 📈 Performance Optimization

- Database query optimization (select_related, prefetch_related)
- Redis caching for frequently accessed data
- Lazy loading for images
- Code splitting in React
- Gzip compression
- CDN for static files
- Database indexing
- API response pagination
- Debounced search inputs

---

## 🤝 Contributing

This project reflects real internship experience and follows professional development standards.

### Development Workflow
1. Create feature branch from `develop`
2. Follow coding standards
3. Write tests for new features
4. Update documentation
5. Submit pull request
6. Code review process
7. Merge to develop
8. Deploy to staging
9. Test in staging
10. Merge to main & deploy to production

---

## 📝 License

MIT License - See LICENSE file for details

---

## 👨‍💻 Developer

**Full-Stack Developer Intern**  
Code IT, Dharan, Nepal  
Django & React Specialist

---

## 📞 Support

For issues and questions:
- Create GitHub issue
- Email: support@smartschoolerp.com
- Documentation: /docs/

---

## 🎓 Acknowledgments

This project was developed during my internship at Code IT, Dharan, Nepal, where I gained hands-on experience in:
- Django REST Framework development
- React.js frontend development
- PostgreSQL database design
- JWT authentication implementation
- Payment gateway integration
- Production deployment on PythonAnywhere
- Agile development methodology
- Professional coding standards

---

**Built with ❤️ using Django REST Framework & React.js**
