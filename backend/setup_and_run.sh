#!/bin/bash

echo "🎓 Smart School ERP - Setup & Run"
echo "=================================="
echo ""

# Activate virtual environment
echo "✓ Activating virtual environment..."
source venv/bin/activate

# Check if Django is installed
if python -c "import django" 2>/dev/null; then
    echo "✓ Django is already installed"
else
    echo "✓ Installing dependencies..."
    pip install -q --upgrade pip
    pip install -q Django==4.2.7
    pip install -q djangorestframework==3.14.0
    pip install -q python-decouple==3.8
    pip install -q djangorestframework-simplejwt==5.3.0
    pip install -q django-cors-headers==4.3.1
    pip install -q whitenoise==6.6.0
    pip install -q Pillow==10.1.0
    pip install -q drf-yasg==1.21.7
    pip install -q django-filter==23.5
    echo "✓ Dependencies installed"
fi

# Create .env if doesn't exist
if [ ! -f .env ]; then
    echo "✓ Creating .env file..."
    cp .env.example .env
    echo "USE_SQLITE=True" >> .env
fi

# Check if database exists
if [ ! -f db.sqlite3 ]; then
    echo "✓ Creating database..."
    python manage.py migrate
    
    echo ""
    echo "=================================="
    echo "Create Admin User"
    echo "=================================="
    echo "Please enter admin details:"
    echo "(Suggested: admin@school.com / admin123)"
    echo ""
    python manage.py createsuperuser
else
    echo "✓ Database already exists"
fi

echo ""
echo "=================================="
echo "✓ Setup Complete!"
echo "=================================="
echo ""
echo "Starting server..."
echo ""
echo "Access your application at:"
echo "  • Admin Panel: http://localhost:8000/admin/"
echo "  • API Docs: http://localhost:8000/swagger/"
echo "  • API Root: http://localhost:8000/api/v1/"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

python manage.py runserver
