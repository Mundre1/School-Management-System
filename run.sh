#!/bin/bash

echo "🚀 Starting Smart School ERP System..."
echo ""

# Start Backend
echo "📦 Starting Backend Server..."
cd backend
source venv/bin/activate
python manage.py runserver &
BACKEND_PID=$!
cd ..

# Wait for backend to start
sleep 3

# Start Frontend
echo "⚛️  Starting Frontend Server..."
cd frontend
PORT=3001 npm start &
FRONTEND_PID=$!
cd ..

echo ""
echo "✅ Both servers are starting..."
echo ""
echo "📍 Access URLs:"
echo "   Frontend: http://localhost:3001"
echo "   Backend:  http://localhost:8000"
echo "   Admin:    http://localhost:8000/admin"
echo ""
echo "🔑 Login Credentials:"
echo "   Email:    admin@school.com"
echo "   Password: admin123"
echo ""
echo "Press Ctrl+C to stop both servers"

# Wait for user interrupt
wait
