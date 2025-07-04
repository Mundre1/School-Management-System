# 🎓 Smart School ERP System - Complete Production Plan

## 📋 Project Overview

**Type:** Full-Stack Web Application (React + Django)  
**Purpose:** Production-level School Management ERP System  
**Internship:** Django & React Full-Stack Intern at Code IT, Dharan, Nepal

---

## 🏗️ Architecture

### Backend: Django + DRF
- Python 3.13
- Django 4.2.7
- Django REST Framework
- PostgreSQL (Production) / SQLite (Development)
- JWT Authentication
- Django Signals
- WhiteNoise
- CORS Headers

### Frontend: React + Tailwind
- React.js 18
- Tailwind CSS
- Axios
- React Router v6
- Recharts (Analytics)
- Hero Icons
- Headless UI

---

## 👥 User Roles & Permissions

### 1. Head of School (Admin)
**Full System Access:**
- ✅ Manage Students, Staff, Courses
- ✅ Attendance Management
- ✅ Fee Management & Payments
- ✅ Results & Grades
- ✅ Timetable Management
- ✅ Analytics Dashboard
- ✅ Library Management
- ✅ Events & Calendar
- ✅ Leave Approvals
- ✅ User Account Management
- ✅ System Settings

### 2. Staff / Teacher
**Limited Access:**
- ✅ View Students & Staff
- ✅ Mark Attendance (QR/One-tap)
- ✅ Upload Results/Marks
- ✅ Manage Assigned Classes
- ✅ Upload Assignments
- ✅ Send Notices/Messages
- ✅ View Timetable
- ✅ Track Student Performance
- ✅ Approve Leave Requests

### 3. Student
**Self-Service Portal:**
- ✅ View Profile
- ✅ View Courses/Classes
- ✅ View Attendance
- ✅ View Fee/Payment History
- ✅ View Results/Grades
- ✅ View & Submit Assignments
- ✅ View Timetable
- ✅ Receive Notices
- ✅ Chat with Teachers
- ✅ Submit Leave Requests
- ✅ Download Reports/PDFs

---

## 🗄️ Database Schema (PostgreSQL)

### Core Tables

#### 1. Authentication & Users
```sql
- users (Custom User Model)
  - id (UUID, PK)
  - email (unique)
  - phone
  - password (hashed)
  - role (ADMIN/STAFF/STUDENT)
  - is_active
  - email_verified
  - created_at, updated_at

- otps
  - user_id (FK)
  - otp_code
  - expires_at
  - is_verified

- password_reset_tokens
  - user_id (FK)
  - token
  - expires_at
  - is_used

- login_history
  - user_id (FK)
  - ip_address
  - user_agent
  - login_time
  - is_successful
```

#### 2. Students Management
```sql
- students
  - id (UUID, PK)
  - user_id (FK, OneToOne)
  - admission_number (unique)
  - roll_number
  - class_id (FK)
  - section
  - academic_year
  - admission_date
  - status (ACTIVE/INACTIVE/GRADUATED)
  - father_name, mother_name
  - guardian_phone, guardian_email
  - medical_conditions
  - blood_group
  - photo
  - documents (JSON)

- guardians
  - id (UUID, PK)
  - student_id (FK)
  - name
  - relation
  - phone, email
  - occupation
  - is_primary
  - is_emergency_contact

- student_documents
  - id (UUID, PK)
  - student_id (FK)
  - document_type
  - document_file
  - uploaded_at

- student_achievements
  - id (UUID, PK)
  - student_id (FK)
  - title
  - description
  - date_achieved
  - certificate
```

#### 3. Staff Management
```sql
- staff
  - id (UUID, PK)
  - user_id (FK, OneToOne)
  - employee_id (unique)
  - department_id (FK)
  - designation
  - join_date
  - salary
  - qualification
  - experience
  - subjects (ManyToMany)
  - photo

- departments
  - id (UUID, PK)
  - name
  - head_id (FK to staff)
  - description
```

#### 4. Academic Management
```sql
- courses
  - id (UUID, PK)
  - name
  - code (unique)
  - description
  - duration
  - fees

- subjects
  - id (UUID, PK)
  - name
  - code (unique)
  - course_id (FK)
  - credits
  - description

- classes
  - id (UUID, PK)
  - name (e.g., "Grade 10 - A")
  - course_id (FK)
  - section
  - academic_year
  - class_teacher_id (FK to staff)
  - room_number
  - capacity

- class_subjects
  - id (UUID, PK)
  - class_id (FK)
  - subject_id (FK)
  - teacher_id (FK to staff)
```

#### 5. Attendance System
```sql
- attendance
  - id (UUID, PK)
  - student_id (FK)
  - class_id (FK)
  - date
  - status (PRESENT/ABSENT/LATE/EXCUSED)
  - marked_by (FK to staff)
  - marked_at
  - method (MANUAL/QR/FACE)
  - remarks

- attendance_summary
  - id (UUID, PK)
  - student_id (FK)
  - month, year
  - total_days
  - present_days
  - absent_days
  - late_days
  - percentage
```

#### 6. Fees Management (Khalti Integration)
```sql
- fee_structures
  - id (UUID, PK)
  - class_id (FK)
  - academic_year
  - tuition_fee
  - admission_fee
  - exam_fee
  - library_fee
  - transport_fee
  - other_fees (JSON)
  - total_amount

- fee_payments
  - id (UUID, PK)
  - student_id (FK)
  - fee_structure_id (FK)
  - amount
  - payment_method (CASH/ONLINE/KHALTI)
  - payment_status (PENDING/PAID/FAILED)
  - transaction_id
  - khalti_idx
  - paid_at
  - due_date
  - receipt_number

- payment_receipts
  - id (UUID, PK)
  - payment_id (FK)
  - receipt_pdf
  - generated_at
```

#### 7. Results & Exams
```sql
- exams
  - id (UUID, PK)
  - name
  - exam_type (MIDTERM/FINAL/UNIT)
  - class_id (FK)
  - start_date, end_date
  - academic_year

- exam_subjects
  - id (UUID, PK)
  - exam_id (FK)
  - subject_id (FK)
  - full_marks
  - pass_marks
  - exam_date, exam_time

- results
  - id (UUID, PK)
  - student_id (FK)
  - exam_subject_id (FK)
  - obtained_marks
  - grade
  - remarks
  - entered_by (FK to staff)
  - entered_at

- report_cards
  - id (UUID, PK)
  - student_id (FK)
  - exam_id (FK)
  - total_marks
  - obtained_marks
  - percentage
  - gpa
  - rank
  - pdf_file
```

#### 8. Timetable System
```sql
- timetables
  - id (UUID, PK)
  - class_id (FK)
  - day_of_week
  - period_number
  - subject_id (FK)
  - teacher_id (FK to staff)
  - start_time, end_time
  - room_number
  - academic_year

- periods
  - id (UUID, PK)
  - period_number
  - start_time
  - end_time
  - duration
```

#### 9. Assignments & Homework
```sql
- assignments
  - id (UUID, PK)
  - title
  - description
  - class_id (FK)
  - subject_id (FK)
  - teacher_id (FK to staff)
  - due_date
  - max_marks
  - attachment
  - created_at

- submissions
  - id (UUID, PK)
  - assignment_id (FK)
  - student_id (FK)
  - submission_file
  - submission_text
  - submitted_at
  - marks_obtained
  - feedback
  - graded_by (FK to staff)
  - graded_at
```

#### 10. Communication System
```sql
- messages
  - id (UUID, PK)
  - sender_id (FK to users)
  - receiver_id (FK to users)
  - subject
  - body
  - is_read
  - sent_at

- announcements
  - id (UUID, PK)
  - title
  - content
  - posted_by (FK to users)
  - target_role (ALL/STAFF/STUDENT)
  - priority (LOW/MEDIUM/HIGH)
  - posted_at
  - expires_at

- notifications
  - id (UUID, PK)
  - user_id (FK)
  - title
  - message
  - type
  - is_read
  - created_at
```

#### 11. Library Management
```sql
- books
  - id (UUID, PK)
  - title
  - author
  - isbn (unique)
  - category
  - publisher
  - quantity
  - available_quantity
  - rack_number

- book_issues
  - id (UUID, PK)
  - book_id (FK)
  - student_id (FK)
  - issue_date
  - due_date
  - return_date
  - fine_amount
  - status (ISSUED/RETURNED/OVERDUE)
```

#### 12. Events & Calendar
```sql
- events
  - id (UUID, PK)
  - title
  - description
  - event_type (HOLIDAY/EXAM/SPORTS/CULTURAL)
  - start_date, end_date
  - location
  - created_by (FK to users)
  - created_at
```

#### 13. Leave Management
```sql
- leave_requests
  - id (UUID, PK)
  - user_id (FK)
  - leave_type (SICK/CASUAL/EMERGENCY)
  - start_date, end_date
  - reason
  - status (PENDING/APPROVED/REJECTED)
  - approved_by (FK to users)
  - approved_at
  - created_at
```

---

## 🎨 Frontend Structure

```
frontend/
├── public/
│   ├── index.html
│   └── favicon.ico
├── src/
│   ├── components/
│   │   ├── common/
│   │   │   ├── Navbar.jsx
│   │   │   ├── Sidebar.jsx
│   │   │   ├── Footer.jsx
│   │   │   ├── Loading.jsx
│   │   │   ├── ErrorBoundary.jsx
│   │   │   └── Toast.jsx
│   │   ├── dashboard/
│   │   │   ├── AdminDashboard.jsx
│   │   │   ├── StaffDashboard.jsx
│   │   │   ├── StudentDashboard.jsx
│   │   │   ├── StatsCard.jsx
│   │   │   └── Charts.jsx
│   │   ├── students/
│   │   │   ├── StudentList.jsx
│   │   │   ├── StudentForm.jsx
│   │   │   ├── StudentProfile.jsx
│   │   │   └── StudentCard.jsx
│   │   ├── staff/
│   │   │   ├── StaffList.jsx
│   │   │   ├── StaffForm.jsx
│   │   │   └── StaffProfile.jsx
│   │   ├── attendance/
│   │   │   ├── AttendanceSheet.jsx
│   │   │   ├── QRScanner.jsx
│   │   │   └── AttendanceReport.jsx
│   │   ├── fees/
│   │   │   ├── FeeStructure.jsx
│   │   │   ├── PaymentForm.jsx
│   │   │   ├── KhaltiPayment.jsx
│   │   │   └── Receipt.jsx
│   │   ├── results/
│   │   │   ├── ResultEntry.jsx
│   │   │   ├── ReportCard.jsx
│   │   │   └── PerformanceChart.jsx
│   │   ├── timetable/
│   │   │   ├── TimetableView.jsx
│   │   │   └── TimetableEditor.jsx
│   │   ├── assignments/
│   │   │   ├── AssignmentList.jsx
│   │   │   ├── AssignmentForm.jsx
│   │   │   └── SubmissionView.jsx
│   │   ├── library/
│   │   │   ├── BookList.jsx
│   │   │   ├── IssueBook.jsx
│   │   │   └── ReturnBook.jsx
│   │   └── auth/
│   │       ├── Login.jsx
│   │       ├── Register.jsx
│   │       ├── ForgotPassword.jsx
│   │       └── OTPLogin.jsx
│   ├── pages/
│   │   ├── Dashboard.jsx
│   │   ├── Students.jsx
│   │   ├── Staff.jsx
│   │   ├── Attendance.jsx
│   │   ├── Fees.jsx
│   │   ├── Results.jsx
│   │   ├── Timetable.jsx
│   │   ├── Assignments.jsx
│   │   ├── Library.jsx
│   │   ├── Events.jsx
│   │   ├── Messages.jsx
│   │   ├── Profile.jsx
│   │   └── Settings.jsx
│   ├── services/
│   │   ├── api.js
│   │   ├── auth.service.js
│   │   ├── student.service.js
│   │   ├── staff.service.js
│   │   ├── attendance.service.js
│   │   ├── fee.service.js
│   │   ├── result.service.js
│   │   └── khalti.service.js
│   ├── utils/
│   │   ├── constants.js
│   │   ├── helpers.js
│   │   ├── validators.js
│   │   └── formatters.js
│   ├── context/
│   │   ├── AuthContext.jsx
│   │   └── ThemeContext.jsx
│   ├── hooks/
│   │   ├── useAuth.js
│   │   ├── useApi.js
│   │   └── useToast.js
│   ├── routes/
│   │   ├── PrivateRoute.jsx
│   │   └── RoleRoute.jsx
│   ├── App.jsx
│   ├── index.js
│   └── index.css
├── tailwind.config.js
├── package.json
└── .env
```

---

## 🔧 Backend Structure

```
backend/
├── core/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── apps/
│   ├── authentication/
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── views.py
│   │   ├── permissions.py
│   │   ├── signals.py
│   │   └── urls.py
│   ├── students/
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── views.py
│   │   ├── admin.py
│   │   └── urls.py
│   ├── staff/
│   ├── courses/
│   ├── attendance/
│   ├── fees/
│   ├── results/
│   ├── timetable/
│   ├── assignments/
│   ├── communication/
│   ├── library/
│   ├── events/
│   └── leave/
├── utils/
│   ├── exceptions.py
│   ├── permissions.py
│   ├── pagination.py
│   └── validators.py
├── media/
├── static/
├── logs/
├── requirements.txt
├── .env
└── manage.py
```

---

## 🚀 Implementation Status

### ✅ Completed (Current):
1. **Authentication System** - 100%
2. **Students Management** - 100%

### 🔄 In Progress:
3. **Staff Management** - 0%
4. **Courses & Classes** - 0%
5. **Attendance System** - 0%
6. **Fees Management** - 0%
7. **Results & Exams** - 0%
8. **Timetable** - 0%
9. **Assignments** - 0%
10. **Communication** - 0%
11. **Library** - 0%
12. **Events** - 0%
13. **Leave Management** - 0%
14. **Analytics Dashboard** - 0%

### 📱 Frontend:
- React App Created - ✅
- Tailwind CSS Setup - ⏳
- Components - 0%
- Pages - 0%
- Services - 0%
- Routing - 0%

---

## 📦 Next Implementation Steps

### Phase 1: Complete Backend (Week 1-2)
1. Staff Management Module
2. Courses & Classes Module
3. Attendance System with QR
4. Fees Management with Khalti
5. Results & Exams Module

### Phase 2: Core Frontend (Week 3-4)
1. Authentication UI
2. Dashboard Layouts
3. Student Management UI
4. Staff Management UI
5. Attendance UI

### Phase 3: Advanced Features (Week 5-6)
1. Timetable System
2. Assignment Module
3. Communication System
4. Library Management
5. Analytics Dashboard

### Phase 4: Premium Features (Week 7-8)
1. Face Recognition Attendance
2. QR Code Generation
3. PDF Report Generation
4. Email Notifications
5. Push Notifications

### Phase 5: Deployment (Week 9)
1. PythonAnywhere Setup
2. PostgreSQL Configuration
3. Static Files Setup
4. Domain Configuration
5. SSL Certificate

---

## 🎯 Current Focus

**Building the complete backend first, then frontend.**

The system is being built module by module with production-quality code, following your internship experience at Code IT, Dharan, Nepal.

---

**Status:** Backend 15% Complete | Frontend 5% Complete  
**Next:** Complete all backend modules, then build React frontend

