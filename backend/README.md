# Itahari International School Management System

A complete, professional school management system built with Django REST Framework and React.

## 🚀 Quick Start

### Prerequisites
- Python 3.x
- Node.js & npm
- Git

### Installation & Running

#### Option 1: Run Both Servers Together (Recommended)
```bash
# From root directory
npm run dev
```
This will start both backend and frontend servers simultaneously!

#### Option 2: Run Servers Separately

**Terminal 1 - Backend:**
```bash
cd backend
npm run dev
```
Backend runs on: http://127.0.0.1:8000/

**Terminal 2 - Frontend:**
```bash
cd frontend
npm start
```
Frontend runs on: http://localhost:3001/

### First Time Setup

If running for the first time, install dependencies:

```bash
# Install all dependencies (backend + frontend)
npm run install-all

# Or install separately:
npm run install-backend  # Install Python packages
npm run install-frontend # Install Node packages
```

## 🎓 Access the System

- **URL**: http://localhost:3001
- **Email**: admin@school.com
- **Password**: admin123

## 📋 Available Commands

### Root Level Commands
```bash
npm run dev              # Run both backend and frontend
npm run backend          # Run only backend
npm run frontend         # Run only frontend
npm run install-all      # Install all dependencies
```

### Backend Commands
```bash
cd backend
npm run dev              # Start Django server
npm run migrate          # Run database migrations
npm run makemigrations   # Create new migrations
npm run createsuperuser  # Create admin user
npm run shell            # Open Django shell
```

### Frontend Commands
```bash
cd frontend
npm start                # Start React development server
npm run build            # Build for production
npm test                 # Run tests
```

## 🏗️ Project Structure

```
smart-school-erp/
├── backend/                 # Django REST API
│   ├── core/               # Project settings
│   ├── apps/               # Django apps
│   │   ├── authentication/ # User authentication
│   │   ├── students/       # Student management
│   │   ├── staff/          # Staff management
│   │   ├── attendance/     # Attendance tracking
│   │   ├── fees/           # Fee management
│   │   ├── results/        # Exam results
│   │   ├── timetable/      # Class schedules
│   │   ├── assignments/    # Homework & assignments
│   │   ├── communication/  # Notices & messages
│   │   ├── library/        # Library management
│   │   ├── events/         # School events
│   │   ├── leave/          # Leave applications
│   │   └── analytics/      # Dashboard analytics
│   ├── manage.py
│   ├── requirements.txt
│   └── package.json
│
├── frontend/               # React Application
│   ├── src/
│   │   ├── components/    # React components
│   │   │   ├── auth/      # Login/Register
│   │   │   ├── dashboard/ # Dashboard
│   │   │   ├── students/  # Student pages
│   │   │   ├── staff/     # Staff pages
│   │   │   ├── attendance/# Attendance pages
│   │   │   ├── fees/      # Fee pages
│   │   │   └── results/   # Results pages
│   │   ├── context/       # React Context
│   │   ├── services/      # API services
│   │   └── App.js
│   ├── package.json
│   └── public/
│
├── package.json            # Root package.json
└── README.md
```

## ✨ Features

### Core Modules
- ✅ **Dashboard** - Professional overview with stats, charts, and analytics
- ✅ **Student Management** - Complete CRUD operations
- ✅ **Staff Management** - Teacher and staff records
- ✅ **Attendance** - Daily attendance tracking
- ✅ **Fee Management** - Payment tracking and receipts
- ✅ **Results** - Exam results and grade management
- ✅ **Timetable** - Class schedules
- ✅ **Assignments** - Homework management
- ✅ **Communication** - Notices and announcements
- ✅ **Library** - Book management
- ✅ **Events** - School events calendar
- ✅ **Leave Management** - Leave applications

### Technical Features
- 🔐 JWT Authentication
- 📊 Real-time Analytics
- 📱 Responsive Design
- 🎨 Modern UI/UX
- 🔄 RESTful API
- 📈 Data Visualization with Charts
- 🔍 Search & Filter
- 📄 Pagination
- ✅ Form Validation

## 🛠️ Technology Stack

### Backend
- Django 4.2.7
- Django REST Framework
- SQLite Database
- JWT Authentication
- Django CORS Headers

### Frontend
- React 19.2.6
- React Router DOM
- Axios
- Recharts (Charts)
- React Icons
- Tailwind CSS

## 📝 Development Timeline

**Project Duration**: July 4, 2025 - October 12, 2025 (100 days)

## 👨‍💻 VS Code Setup

### Recommended Extensions
- Python
- ES7+ React/Redux/React-Native snippets
- Prettier - Code formatter
- ESLint
- GitLens

### Running in VS Code

1. Open project in VS Code:
```bash
code .
```

2. Open integrated terminal (`` Ctrl+` ``)

3. Run the project:
```bash
npm run dev
```

4. Both servers will start automatically!

## 🔧 Troubleshooting

### Backend Issues

**Module not found error:**
```bash
cd backend
pip3 install -r requirements.txt
```

**Database issues:**
```bash
cd backend
python3 manage.py migrate
```

### Frontend Issues

**Dependencies error:**
```bash
cd frontend
npm install
```

**Port already in use:**
```bash
# Kill process on port 3001
lsof -ti:3001 | xargs kill -9
```

## 📞 Support

For issues or questions, please contact the development team.

## 📄 License

MIT License - Itahari International School

---

**Built with ❤️ for Itahari International School**
