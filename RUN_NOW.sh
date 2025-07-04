#!/bin/bash

# Smart School ERP - Quick Setup with SQLite
# No PostgreSQL installation required!

echo "🎓 Smart School ERP - Quick Setup (SQLite)"
echo "=========================================="
echo ""

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m'

# Navigate to backend
cd backend

# Check if venv exists
if [ ! -d "venv" ]; then
    echo -e "${BLUE}Creating virtual environment...${NC}"
    python3 -m venv venv
fi

# Activate venv
echo -e "${BLUE}Activating virtual environment...${NC}"
source venv/bin/activate

# Upgrade pip
echo -e "${BLUE}Upgrading pip...${NC}"
pip install --upgrade pip

# Install dependencies (SQLite version - no PostgreSQL needed)
echo -e "${BLUE}Installing dependencies...${NC}"
pip install -r requirements-sqlite.txt

# Create .env if it doesn't exist
if [ ! -f .env ]; then
    echo -e "${BLUE}Creating .env file...${NC}"
    cp .env.example .env
    # Set SQLite mode
    echo "USE_SQLITE=True" >> .env
fi

# Run migrations
echo -e "${BLUE}Running database migrations...${NC}"
python manage.py migrate

# Check if superuser exists
echo -e "${BLUE}Creating superuser...${NC}"
echo "Please enter superuser details:"
python manage.py createsuperuser

# Start server
echo -e "${GREEN}✓ Setup complete!${NC}"
echo ""
echo "=========================================="
echo "Starting Django development server..."
echo "=========================================="
echo ""
echo "Access your application at:"
echo "  - Admin Panel: http://localhost:8000/admin/"
echo "  - API Docs: http://localhost:8000/swagger/"
echo "  - API Root: http://localhost:8000/api/v1/"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

python manage.py runserver
