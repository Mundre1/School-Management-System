# Smart School ERP System - API Documentation

## 📡 RESTful API Reference

**Base URL:** `http://localhost:8000/api/v1`  
**Production URL:** `https://yourdomain.com/api/v1`

**Authentication:** JWT Bearer Token  
**Content-Type:** `application/json`

---

## 🔐 Authentication

### Register User
**POST** `/auth/register/`

**Request Body:**
```json
{
  "email": "user@example.com",
  "password": "SecurePass123!",
  "password_confirm": "SecurePass123!",
  "first_name": "John",
  "last_name": "Doe",
  "phone": "+9779812345678",
  "role": "STUDENT",
  "date_of_birth": "2005-01-15",
  "gender": "M"
}
```

**Response (201 Created):**
```json
{
  "success": true,
  "message": "User registered successfully. Please verify your email.",
  "data": {
    "user": {
      "id": "uuid",
      "email": "user@example.com",
      "first_name": "John",
      "last_name": "Doe",
      "role": "STUDENT",
      "email_verified": false
    },
    "tokens": {
      "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc...",
      "access": "eyJ0eXAiOiJKV1QiLCJhbGc..."
    }
  }
}
```

---

### Login
**POST** `/auth/login/`

**Request Body:**
```json
{
  "email": "user@example.com",
  "password": "SecurePass123!"
}
```

**Response (200 OK):**
```json
{
  "success": true,
  "message": "Login successful",
  "data": {
    "user": {
      "id": "uuid",
      "email": "user@example.com",
      "first_name": "John",
      "last_name": "Doe",
      "full_name": "John Doe",
      "role": "STUDENT",
      "profile_picture": "http://example.com/media/profiles/user.jpg"
    },
    "tokens": {
      "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc...",
      "access": "eyJ0eXAiOiJKV1QiLCJhbGc..."
    }
  }
}
```

---

### Logout
**POST** `/auth/logout/`

**Headers:**
```
Authorization: Bearer <access_token>
```

**Request Body:**
```json
{
  "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}
```

**Response (200 OK):**
```json
{
  "success": true,
  "message": "Logout successful"
}
```

---

### Refresh Token
**POST** `/auth/token/refresh/`

**Request Body:**
```json
{
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}
```

**Response (200 OK):**
```json
{
  "access": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}
```

---

### Get Profile
**GET** `/auth/profile/`

**Headers:**
```
Authorization: Bearer <access_token>
```

**Response (200 OK):**
```json
{
  "success": true,
  "data": {
    "id": "uuid",
    "email": "user@example.com",
    "phone": "+9779812345678",
    "first_name": "John",
    "last_name": "Doe",
    "full_name": "John Doe",
    "date_of_birth": "2005-01-15",
    "gender": "M",
    "profile_picture": "http://example.com/media/profiles/user.jpg",
    "address": "Kathmandu, Nepal",
    "role": "STUDENT",
    "email_verified": true,
    "date_joined": "2024-01-01T10:00:00Z"
  }
}
```

---

### Update Profile
**PUT** `/auth/profile/`

**Headers:**
```
Authorization: Bearer <access_token>
```

**Request Body:**
```json
{
  "first_name": "John",
  "last_name": "Doe",
  "phone": "+9779812345678",
  "address": "Kathmandu, Nepal",
  "bio": "Student at XYZ School"
}
```

**Response (200 OK):**
```json
{
  "success": true,
  "message": "Profile updated successfully",
  "data": { /* updated user object */ }
}
```

---

### Change Password
**POST** `/auth/change-password/`

**Headers:**
```
Authorization: Bearer <access_token>
```

**Request Body:**
```json
{
  "old_password": "OldPass123!",
  "new_password": "NewPass123!",
  "new_password_confirm": "NewPass123!"
}
```

**Response (200 OK):**
```json
{
  "success": true,
  "message": "Password changed successfully"
}
```

---

### Send OTP
**POST** `/auth/send-otp/`

**Request Body:**
```json
{
  "phone": "+9779812345678"
}
```

**Response (200 OK):**
```json
{
  "success": true,
  "message": "OTP sent successfully",
  "data": {
    "phone": "+9779812345678",
    "expires_at": "2024-01-01T10:10:00Z"
  }
}
```

---

### OTP Login
**POST** `/auth/otp-login/`

**Request Body:**
```json
{
  "phone": "+9779812345678",
  "otp_code": "123456"
}
```

**Response (200 OK):**
```json
{
  "success": true,
  "message": "Login successful",
  "data": {
    "user": { /* user object */ },
    "tokens": {
      "refresh": "...",
      "access": "..."
    }
  }
}
```

---

### Password Reset Request
**POST** `/auth/password-reset/`

**Request Body:**
```json
{
  "email": "user@example.com"
}
```

**Response (200 OK):**
```json
{
  "success": true,
  "message": "Password reset email sent successfully",
  "data": {
    "email": "user@example.com"
  }
}
```

---

### Password Reset Confirm
**POST** `/auth/password-reset-confirm/`

**Request Body:**
```json
{
  "token": "reset-token-from-email",
  "password": "NewPass123!",
  "password_confirm": "NewPass123!"
}
```

**Response (200 OK):**
```json
{
  "success": true,
  "message": "Password reset successful",
  "data": {
    "email": "user@example.com"
  }
}
```

---

### Verify Email
**POST** `/auth/verify-email/`

**Request Body:**
```json
{
  "token": "verification-token-from-email"
}
```

**Response (200 OK):**
```json
{
  "success": true,
  "message": "Email verified successfully",
  "data": {
    "email": "user@example.com"
  }
}
```

---

## 👨‍🎓 Students

### List Students
**GET** `/students/`

**Headers:**
```
Authorization: Bearer <access_token>
```

**Query Parameters:**
- `page` (int): Page number (default: 1)
- `page_size` (int): Items per page (default: 20)
- `search` (string): Search by name or email
- `class` (uuid): Filter by class ID
- `gender` (string): Filter by gender (M/F/O)
- `ordering` (string): Sort by field (e.g., `-date_joined`)

**Example:**
```
GET /students/?page=1&page_size=20&search=john&ordering=-date_joined
```

**Response (200 OK):**
```json
{
  "count": 100,
  "next": "http://api.example.com/students/?page=2",
  "previous": null,
  "results": [
    {
      "id": "uuid",
      "user": {
        "id": "uuid",
        "email": "student@example.com",
        "first_name": "John",
        "last_name": "Doe",
        "full_name": "John Doe",
        "profile_picture": "http://example.com/media/profiles/student.jpg"
      },
      "admission_number": "STU2024001",
      "class": {
        "id": "uuid",
        "name": "Class 10 A",
        "section": "A"
      },
      "roll_number": "10",
      "date_of_admission": "2024-01-01",
      "parent_name": "Jane Doe",
      "parent_phone": "+9779812345678",
      "parent_email": "parent@example.com",
      "blood_group": "O+",
      "is_active": true
    }
  ]
}
```

---

### Create Student
**POST** `/students/`

**Headers:**
```
Authorization: Bearer <access_token>
Content-Type: multipart/form-data
```

**Request Body (Form Data):**
```
email: student@example.com
password: SecurePass123!
first_name: John
last_name: Doe
phone: +9779812345678
date_of_birth: 2005-01-15
gender: M
profile_picture: <file>
admission_number: STU2024001
class: <class_uuid>
roll_number: 10
parent_name: Jane Doe
parent_phone: +9779812345678
parent_email: parent@example.com
blood_group: O+
```

**Response (201 Created):**
```json
{
  "success": true,
  "message": "Student created successfully",
  "data": { /* student object */ }
}
```

---

### Get Student Details
**GET** `/students/{id}/`

**Headers:**
```
Authorization: Bearer <access_token>
```

**Response (200 OK):**
```json
{
  "success": true,
  "data": {
    "id": "uuid",
    "user": { /* user object */ },
    "admission_number": "STU2024001",
    "class": { /* class object */ },
    "roll_number": "10",
    "attendance_percentage": 95.5,
    "total_fees": 50000,
    "paid_fees": 30000,
    "pending_fees": 20000,
    "academic_performance": {
      "gpa": 3.8,
      "rank": 5,
      "total_students": 50
    }
  }
}
```

---

### Update Student
**PUT** `/students/{id}/`

**Headers:**
```
Authorization: Bearer <access_token>
```

**Request Body:**
```json
{
  "first_name": "John",
  "last_name": "Doe",
  "phone": "+9779812345678",
  "class": "class_uuid",
  "roll_number": "10"
}
```

**Response (200 OK):**
```json
{
  "success": true,
  "message": "Student updated successfully",
  "data": { /* updated student object */ }
}
```

---

### Delete Student
**DELETE** `/students/{id}/`

**Headers:**
```
Authorization: Bearer <access_token>
```

**Response (204 No Content)**

---

### Bulk Import Students
**POST** `/students/bulk-import/`

**Headers:**
```
Authorization: Bearer <access_token>
Content-Type: multipart/form-data
```

**Request Body:**
```
file: <csv_file>
```

**CSV Format:**
```csv
email,first_name,last_name,phone,date_of_birth,gender,admission_number,class_id,roll_number
student1@example.com,John,Doe,+9779812345678,2005-01-15,M,STU2024001,class_uuid,10
student2@example.com,Jane,Smith,+9779812345679,2005-02-20,F,STU2024002,class_uuid,11
```

**Response (200 OK):**
```json
{
  "success": true,
  "message": "Students imported successfully",
  "data": {
    "total": 100,
    "success": 95,
    "failed": 5,
    "errors": [
      {
        "row": 10,
        "error": "Email already exists"
      }
    ]
  }
}
```

---

## 📊 Attendance

### List Attendance
**GET** `/attendance/`

**Headers:**
```
Authorization: Bearer <access_token>
```

**Query Parameters:**
- `date` (date): Filter by date (YYYY-MM-DD)
- `student` (uuid): Filter by student ID
- `class` (uuid): Filter by class ID
- `status` (string): Filter by status (PRESENT/ABSENT/LATE/LEAVE)

**Response (200 OK):**
```json
{
  "count": 50,
  "results": [
    {
      "id": "uuid",
      "student": {
        "id": "uuid",
        "name": "John Doe",
        "admission_number": "STU2024001"
      },
      "date": "2024-01-15",
      "status": "PRESENT",
      "marked_by": {
        "id": "uuid",
        "name": "Teacher Name"
      },
      "marked_at": "2024-01-15T09:00:00Z",
      "remarks": ""
    }
  ]
}
```

---

### Mark Attendance
**POST** `/attendance/`

**Headers:**
```
Authorization: Bearer <access_token>
```

**Request Body:**
```json
{
  "class": "class_uuid",
  "date": "2024-01-15",
  "attendance": [
    {
      "student": "student_uuid_1",
      "status": "PRESENT"
    },
    {
      "student": "student_uuid_2",
      "status": "ABSENT",
      "remarks": "Sick leave"
    }
  ]
}
```

**Response (201 Created):**
```json
{
  "success": true,
  "message": "Attendance marked successfully",
  "data": {
    "total": 50,
    "present": 45,
    "absent": 3,
    "late": 2,
    "leave": 0
  }
}
```

---

### QR Code Attendance
**POST** `/attendance/qr/`

**Headers:**
```
Authorization: Bearer <access_token>
```

**Request Body:**
```json
{
  "qr_code": "encrypted_student_data",
  "location": {
    "latitude": 27.7172,
    "longitude": 85.3240
  }
}
```

**Response (200 OK):**
```json
{
  "success": true,
  "message": "Attendance marked successfully",
  "data": {
    "student": "John Doe",
    "status": "PRESENT",
    "time": "2024-01-15T09:00:00Z"
  }
}
```

---

### Attendance Report
**GET** `/attendance/report/`

**Headers:**
```
Authorization: Bearer <access_token>
```

**Query Parameters:**
- `student` (uuid): Student ID
- `class` (uuid): Class ID
- `start_date` (date): Start date
- `end_date` (date): End date
- `format` (string): Response format (json/pdf/excel)

**Response (200 OK):**
```json
{
  "success": true,
  "data": {
    "student": {
      "id": "uuid",
      "name": "John Doe",
      "admission_number": "STU2024001"
    },
    "period": {
      "start_date": "2024-01-01",
      "end_date": "2024-01-31"
    },
    "summary": {
      "total_days": 22,
      "present": 20,
      "absent": 1,
      "late": 1,
      "leave": 0,
      "percentage": 90.9
    },
    "details": [
      {
        "date": "2024-01-15",
        "status": "PRESENT"
      }
    ]
  }
}
```

---

## 💰 Fees & Payments

### List Fees
**GET** `/fees/`

**Headers:**
```
Authorization: Bearer <access_token>
```

**Response (200 OK):**
```json
{
  "count": 10,
  "results": [
    {
      "id": "uuid",
      "student": {
        "id": "uuid",
        "name": "John Doe",
        "admission_number": "STU2024001"
      },
      "fee_type": "TUITION",
      "amount": 50000,
      "paid_amount": 30000,
      "pending_amount": 20000,
      "due_date": "2024-02-01",
      "status": "PARTIAL",
      "is_overdue": false
    }
  ]
}
```

---

### Create Fee
**POST** `/fees/`

**Headers:**
```
Authorization: Bearer <access_token>
```

**Request Body:**
```json
{
  "student": "student_uuid",
  "fee_type": "TUITION",
  "amount": 50000,
  "due_date": "2024-02-01",
  "description": "Tuition fee for Term 1"
}
```

**Response (201 Created):**
```json
{
  "success": true,
  "message": "Fee created successfully",
  "data": { /* fee object */ }
}
```

---

### Khalti Payment
**POST** `/payments/khalti/`

**Headers:**
```
Authorization: Bearer <access_token>
```

**Request Body:**
```json
{
  "fee": "fee_uuid",
  "amount": 20000,
  "token": "khalti_payment_token",
  "mobile": "+9779812345678"
}
```

**Response (200 OK):**
```json
{
  "success": true,
  "message": "Payment successful",
  "data": {
    "payment_id": "uuid",
    "transaction_id": "khalti_transaction_id",
    "amount": 20000,
    "status": "COMPLETED",
    "receipt_url": "http://example.com/receipts/payment_uuid.pdf"
  }
}
```

---

### Payment History
**GET** `/payments/`

**Headers:**
```
Authorization: Bearer <access_token>
```

**Query Parameters:**
- `student` (uuid): Filter by student
- `status` (string): Filter by status (PENDING/COMPLETED/FAILED)
- `start_date` (date): Start date
- `end_date` (date): End date

**Response (200 OK):**
```json
{
  "count": 5,
  "results": [
    {
      "id": "uuid",
      "fee": {
        "fee_type": "TUITION",
        "amount": 50000
      },
      "amount": 20000,
      "payment_method": "KHALTI",
      "transaction_id": "khalti_transaction_id",
      "status": "COMPLETED",
      "payment_date": "2024-01-15T10:00:00Z",
      "receipt_url": "http://example.com/receipts/payment_uuid.pdf"
    }
  ]
}
```

---

### Download Receipt
**GET** `/payments/receipt/{id}/`

**Headers:**
```
Authorization: Bearer <access_token>
```

**Response:** PDF file download

---

## 📝 Results

### List Results
**GET** `/results/`

**Headers:**
```
Authorization: Bearer <access_token>
```

**Query Parameters:**
- `student` (uuid): Filter by student
- `exam` (uuid): Filter by exam
- `class` (uuid): Filter by class

**Response (200 OK):**
```json
{
  "count": 10,
  "results": [
    {
      "id": "uuid",
      "student": {
        "id": "uuid",
        "name": "John Doe"
      },
      "exam": {
        "id": "uuid",
        "name": "Final Exam 2024",
        "term": "Term 1"
      },
      "subjects": [
        {
          "subject": "Mathematics",
          "marks_obtained": 85,
          "total_marks": 100,
          "grade": "A",
          "remarks": "Excellent"
        }
      ],
      "total_marks": 500,
      "marks_obtained": 425,
      "percentage": 85.0,
      "gpa": 3.8,
      "grade": "A",
      "rank": 5,
      "published": true
    }
  ]
}
```

---

### Create Result
**POST** `/results/`

**Headers:**
```
Authorization: Bearer <access_token>
```

**Request Body:**
```json
{
  "student": "student_uuid",
  "exam": "exam_uuid",
  "subjects": [
    {
      "subject": "subject_uuid",
      "marks_obtained": 85,
      "total_marks": 100
    }
  ]
}
```

**Response (201 Created):**
```json
{
  "success": true,
  "message": "Result created successfully",
  "data": { /* result object */ }
}
```

---

### Download Report Card
**GET** `/results/{id}/pdf/`

**Headers:**
```
Authorization: Bearer <access_token>
```

**Response:** PDF file download

---

## 📅 Timetable

### Get Timetable
**GET** `/timetable/`

**Headers:**
```
Authorization: Bearer <access_token>
```

**Query Parameters:**
- `class` (uuid): Class ID
- `teacher` (uuid): Teacher ID
- `day` (string): Day of week (MONDAY/TUESDAY/etc.)

**Response (200 OK):**
```json
{
  "success": true,
  "data": {
    "class": {
      "id": "uuid",
      "name": "Class 10 A"
    },
    "schedule": [
      {
        "day": "MONDAY",
        "periods": [
          {
            "period": 1,
            "start_time": "09:00:00",
            "end_time": "09:45:00",
            "subject": {
              "id": "uuid",
              "name": "Mathematics"
            },
            "teacher": {
              "id": "uuid",
              "name": "Teacher Name"
            },
            "room": "Room 101"
          }
        ]
      }
    ]
  }
}
```

---

## 📚 Assignments

### List Assignments
**GET** `/assignments/`

**Headers:**
```
Authorization: Bearer <access_token>
```

**Query Parameters:**
- `class` (uuid): Filter by class
- `subject` (uuid): Filter by subject
- `status` (string): Filter by status (PENDING/SUBMITTED/GRADED)

**Response (200 OK):**
```json
{
  "count": 10,
  "results": [
    {
      "id": "uuid",
      "title": "Math Assignment 1",
      "description": "Solve problems from chapter 5",
      "subject": {
        "id": "uuid",
        "name": "Mathematics"
      },
      "class": {
        "id": "uuid",
        "name": "Class 10 A"
      },
      "teacher": {
        "id": "uuid",
        "name": "Teacher Name"
      },
      "due_date": "2024-01-20",
      "total_marks": 20,
      "attachments": [
        "http://example.com/media/assignments/file.pdf"
      ],
      "submission_status": "PENDING"
    }
  ]
}
```

---

### Submit Assignment
**POST** `/assignments/{id}/submit/`

**Headers:**
```
Authorization: Bearer <access_token>
Content-Type: multipart/form-data
```

**Request Body:**
```
file: <file>
remarks: "Completed assignment"
```

**Response (200 OK):**
```json
{
  "success": true,
  "message": "Assignment submitted successfully",
  "data": {
    "submission_id": "uuid",
    "submitted_at": "2024-01-18T10:00:00Z",
    "status": "SUBMITTED"
  }
}
```

---

## 💬 Communication

### List Messages
**GET** `/communication/messages/`

**Headers:**
```
Authorization: Bearer <access_token>
```

**Response (200 OK):**
```json
{
  "count": 20,
  "results": [
    {
      "id": "uuid",
      "sender": {
        "id": "uuid",
        "name": "Teacher Name"
      },
      "receiver": {
        "id": "uuid",
        "name": "Student Name"
      },
      "subject": "Regarding assignment",
      "message": "Please submit your assignment by tomorrow",
      "is_read": false,
      "sent_at": "2024-01-15T10:00:00Z"
    }
  ]
}
```

---

### Send Message
**POST** `/communication/messages/`

**Headers:**
```
Authorization: Bearer <access_token>
```

**Request Body:**
```json
{
  "receiver": "user_uuid",
  "subject": "Regarding assignment",
  "message": "Please submit your assignment by tomorrow"
}
```

**Response (201 Created):**
```json
{
  "success": true,
  "message": "Message sent successfully",
  "data": { /* message object */ }
}
```

---

### List Notifications
**GET** `/communication/notifications/`

**Headers:**
```
Authorization: Bearer <access_token>
```

**Response (200 OK):**
```json
{
  "count": 15,
  "results": [
    {
      "id": "uuid",
      "title": "Fee Due Reminder",
      "message": "Your fee payment is due on 2024-02-01",
      "type": "FEE_REMINDER",
      "is_read": false,
      "created_at": "2024-01-15T10:00:00Z"
    }
  ]
}
```

---

## 📊 Analytics

### Dashboard Analytics
**GET** `/analytics/dashboard/`

**Headers:**
```
Authorization: Bearer <access_token>
```

**Response (200 OK):**
```json
{
  "success": true,
  "data": {
    "overview": {
      "total_students": 500,
      "total_staff": 50,
      "total_classes": 20,
      "total_courses": 15
    },
    "attendance": {
      "today": {
        "present": 450,
        "absent": 30,
        "late": 15,
        "leave": 5,
        "percentage": 90.0
      },
      "this_month": {
        "average_percentage": 92.5
      }
    },
    "fees": {
      "total_fees": 25000000,
      "collected": 20000000,
      "pending": 5000000,
      "collection_percentage": 80.0
    },
    "results": {
      "average_gpa": 3.5,
      "top_performers": [
        {
          "student": "John Doe",
          "gpa": 4.0
        }
      ]
    },
    "charts": {
      "attendance_trend": [
        {
          "date": "2024-01-01",
          "percentage": 92.0
        }
      ],
      "fee_collection": [
        {
          "month": "January",
          "collected": 2000000
        }
      ]
    }
  }
}
```

---

## 🔍 Error Responses

### 400 Bad Request
```json
{
  "success": false,
  "message": "Validation error",
  "errors": {
    "email": ["This field is required."],
    "password": ["Password must be at least 8 characters."]
  }
}
```

### 401 Unauthorized
```json
{
  "success": false,
  "message": "Authentication credentials were not provided.",
  "code": "not_authenticated"
}
```

### 403 Forbidden
```json
{
  "success": false,
  "message": "You do not have permission to perform this action.",
  "code": "permission_denied"
}
```

### 404 Not Found
```json
{
  "success": false,
  "message": "Resource not found.",
  "code": "not_found"
}
```

### 500 Internal Server Error
```json
{
  "success": false,
  "message": "An unexpected error occurred. Please try again later.",
  "code": "server_error"
}
```

---

## 📝 Notes

1. **Authentication:** All endpoints except `/auth/register/`, `/auth/login/`, `/auth/send-otp/`, and `/auth/otp-login/` require JWT authentication.

2. **Pagination:** List endpoints support pagination with `page` and `page_size` parameters.

3. **Filtering:** Most list endpoints support filtering via query parameters.

4. **File Uploads:** Use `multipart/form-data` content type for file uploads.

5. **Date Format:** Use ISO 8601 format (YYYY-MM-DD) for dates.

6. **Time Format:** Use ISO 8601 format (YYYY-MM-DDTHH:MM:SSZ) for timestamps.

---

## 🔗 Interactive Documentation

Visit these URLs for interactive API documentation:

- **Swagger UI:** http://localhost:8000/swagger/
- **ReDoc:** http://localhost:8000/redoc/

---

**Built with ❤️ using Django REST Framework**
