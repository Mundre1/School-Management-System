#!/bin/bash

echo "🎓 Smart School ERP - Simple Setup"
echo "==================================="
echo ""

# Activate venv
source venv/bin/activate

# Install setuptools first (required for pkg_resources)
echo "Installing setuptools..."
pip install -q setuptools

# Install packages one by one
echo "Installing Django..."
pip install -q Django==4.2.7

echo "Installing DRF..."
pip install -q djangorestframework==3.14.0

echo "Installing python-decouple..."
pip install -q python-decouple==3.8

echo "Installing JWT..."
pip install -q djangorestframework-simplejwt==5.3.0

echo "Installing CORS headers..."
pip install -q django-cors-headers==4.3.1

echo "Installing WhiteNoise..."
pip install -q whitenoise==6.6.0

echo "Installing Pillow..."
pip install -q Pillow

echo "Installing django-filter..."
pip install -q django-filter==23.5

echo "Installing drf-yasg..."
pip install -q drf-yasg==1.21.7

echo "Installing utilities..."
pip install -q python-dateutil==2.8.2 pytz==2023.3

echo ""
echo "✓ All packages installed!"
echo ""

# Create .env
if [ ! -f .env ]; then
    cp .env.example .env
    echo "USE_SQLITE=True" >> .env
    echo "✓ Created .env file"
fi

# Run migrations
echo "Creating database..."
python manage.py migrate

echo ""
echo "==================================="
echo "Create Admin User"
echo "==================================="
python manage.py createsuperuser

echo ""
echo "✓ Setup Complete!"
echo ""
echo "Starting server..."
python manage.py runserver
