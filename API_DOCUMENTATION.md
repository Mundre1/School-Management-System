# API Documentation

## Base URL
```
http://localhost:8000
```

## Authentication

All API endpoints (except login) require JWT authentication.

### Headers
```
Authorization: Bearer <access_token>
```

## Endpoints

### Authentication

#### Login
```http
POST /auth/login/
Content-Type: application/json

{
  "email": "admin@school.com",
  "password": "admin123"
}

Response:
{
  "access": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "user": {
    "id": 1,
    "email": "admin@school.com",
    "first_name": "Admin",
    "role": "admin"
  }
}
```

#### Refresh Token
```http
POST /auth/token/refresh/
Content-Type: application/json

{
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}

Response:
{
  "access": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}
```

### Students

#### List Students
```http
GET /students/students/
Authorization: Bearer <token>

Query Parameters:
- page: Page number (default: 1)
- search: Search by name, email, admission_number
- grade: Filter by grade

Response:
{
  "count": 100,
  "next": "http://localhost:8000/students/students/?page=2",
  "previous": null,
  "results": [...]
}
```

#### Create Student
```http
POST /students/students/
Authorization: Bearer <token>
Content-Type: application/json

{
  "admission_number": "2026001",
  "first_name": "John",
  "last_name": "Doe",
  "email": "john@example.com",
  "phone": "9812345678",
  "date_of_birth": "2010-05-15",
  "gender": "male",
  "grade": 10,
  "section": "A",
  "parent_name": "Jane Doe",
  "parent_phone": "9812345679"
}
```

#### Get Student
```http
GET /students/students/{id}/
Authorization: Bearer <token>
```

#### Update Student
```http
PUT /students/students/{id}/
Authorization: Bearer <token>
Content-Type: application/json

{
  "first_name": "John Updated",
  ...
}
```

#### Delete Student
```http
DELETE /students/students/{id}/
Authorization: Bearer <token>
```

### Staff

#### List Staff
```http
GET /staff/staff/
Authorization: Bearer <token>

Query Parameters:
- search: Search by name, email, employee_id
- department: Filter by department
- status: Filter by status
```

### Attendance

#### List Attendance
```http
GET /attendance/attendance/
Authorization: Bearer <token>

Query Parameters:
- date: Filter by date (YYYY-MM-DD)
- student: Filter by student ID
- status: Filter by status
```

#### Mark Attendance
```http
POST /attendance/attendance/
Authorization: Bearer <token>
Content-Type: application/json

{
  "student": 1,
  "date": "2026-05-27",
  "status": "present",
  "remarks": "On time"
}
```

#### Bulk Mark Attendance
```http
POST /attendance/attendance/bulk_mark/
Authorization: Bearer <token>
Content-Type: application/json

{
  "date": "2026-05-27",
  "attendances": [
    {"student_id": 1, "status": "present"},
    {"student_id": 2, "status": "absent", "remarks": "Sick"}
  ]
}
```

#### Get Statistics
```http
GET /attendance/attendance/statistics/
Authorization: Bearer <token>

Query Parameters:
- date_from: Start date
- date_to: End date

Response:
{
  "total": 500,
  "present": 450,
  "absent": 50,
  "present_percentage": 90.0
}
```

### Fees

#### List Payments
```http
GET /fees/payments/
Authorization: Bearer <token>

Query Parameters:
- payment_status: Filter by status
- student: Filter by student ID
```

#### Get Payment Statistics
```http
GET /fees/payments/statistics/
Authorization: Bearer <token>

Response:
{
  "total_due": 1000000,
  "total_paid": 800000,
  "total_remaining": 200000,
  "collection_percentage": 80.0
}
```

#### Make Payment
```http
POST /fees/payments/{id}/make_payment/
Authorization: Bearer <token>
Content-Type: application/json

{
  "amount": 5000,
  "payment_method": "khalti",
  "transaction_id": "TXN123456"
}
```

### Results

#### List Results
```http
GET /results/results/
Authorization: Bearer <token>

Query Parameters:
- exam: Filter by exam ID
- student: Filter by student ID
- subject: Filter by subject ID
```

#### Get Statistics
```http
GET /results/results/statistics/
Authorization: Bearer <token>

Query Parameters:
- exam: Exam ID
- grade: Grade number

Response:
{
  "total_results": 100,
  "average_percentage": 75.5,
  "pass_count": 85,
  "fail_count": 15,
  "pass_percentage": 85.0
}
```

#### Get Student Report
```http
GET /results/results/student_report/
Authorization: Bearer <token>

Query Parameters:
- student_id: Student ID (required)
- exam_id: Exam ID (optional)

Response:
{
  "results": [...],
  "total_subjects": 6,
  "total_marks_obtained": 450,
  "total_marks": 600,
  "overall_percentage": 75.0,
  "pass_count": 6,
  "fail_count": 0
}
```

## Error Responses

### 400 Bad Request
```json
{
  "field_name": ["Error message"]
}
```

### 401 Unauthorized
```json
{
  "detail": "Authentication credentials were not provided."
}
```

### 404 Not Found
```json
{
  "detail": "Not found."
}
```

### 500 Internal Server Error
```json
{
  "detail": "Internal server error."
}
```

## Rate Limiting

Currently no rate limiting is implemented. This will be added in future versions.

## Pagination

All list endpoints support pagination with the following parameters:
- `page`: Page number (default: 1)
- `page_size`: Items per page (default: 10)

## Filtering

Most list endpoints support filtering using query parameters. Check individual endpoint documentation for available filters.

## Ordering

Use the `ordering` query parameter to sort results:
```
GET /students/students/?ordering=-created_at
GET /students/students/?ordering=first_name
```

Use `-` prefix for descending order.
