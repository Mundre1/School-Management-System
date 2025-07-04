#!/bin/bash

# Smart School ERP System - Quick Setup Script
# This script will help you set up the project quickly

echo "🎓 Smart School ERP System - Setup Script"
echo "=========================================="
echo ""

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check if Python is installed
echo -e "${BLUE}Checking Python installation...${NC}"
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version)
    echo -e "${GREEN}✓ Python found: $PYTHON_VERSION${NC}"
else
    echo -e "${RED}✗ Python 3 is not installed${NC}"
    echo "Please install Python 3.10 or higher from https://www.python.org/"
    exit 1
fi

# Check if Node.js is installed
echo -e "${BLUE}Checking Node.js installation...${NC}"
if command -v node &> /dev/null; then
    NODE_VERSION=$(node --version)
    echo -e "${GREEN}✓ Node.js found: $NODE_VERSION${NC}"
else
    echo -e "${RED}✗ Node.js is not installed${NC}"
    echo "Please install Node.js 16+ from https://nodejs.org/"
    exit 1
fi

# Check if PostgreSQL is installed
echo -e "${BLUE}Checking PostgreSQL installation...${NC}"
if command -v psql &> /dev/null; then
    PSQL_VERSION=$(psql --version)
    echo -e "${GREEN}✓ PostgreSQL found: $PSQL_VERSION${NC}"
else
    echo -e "${YELLOW}⚠ PostgreSQL is not installed${NC}"
    echo "Install with: brew install postgresql"
fi

echo ""
echo "=========================================="
echo "What would you like to set up?"
echo "=========================================="
echo "1) Backend only (Django REST Framework)"
echo "2) Mobile app only (React Native)"
echo "3) Both backend and mobile app"
echo "4) Exit"
echo ""
read -p "Enter your choice (1-4): " choice

case $choice in
    1)
        echo -e "${BLUE}Setting up Backend...${NC}"
        cd backend
        
        # Create virtual environment
        echo -e "${BLUE}Creating virtual environment...${NC}"
        python3 -m venv venv
        
        # Activate virtual environment
        echo -e "${BLUE}Activating virtual environment...${NC}"
        source venv/bin/activate
        
        # Upgrade pip
        echo -e "${BLUE}Upgrading pip...${NC}"
        pip install --upgrade pip
        
        # Install dependencies
        echo -e "${BLUE}Installing Python dependencies...${NC}"
        pip install -r requirements.txt
        
        # Copy environment file
        if [ ! -f .env ]; then
            echo -e "${BLUE}Creating .env file...${NC}"
            cp .env.example .env
            echo -e "${YELLOW}⚠ Please edit backend/.env with your configuration${NC}"
        fi
        
        echo -e "${GREEN}✓ Backend setup complete!${NC}"
        echo ""
        echo "Next steps:"
        echo "1. Edit backend/.env with your database credentials"
        echo "2. Create PostgreSQL database: createdb school_erp_db"
        echo "3. Run migrations: python manage.py migrate"
        echo "4. Create superuser: python manage.py createsuperuser"
        echo "5. Start server: python manage.py runserver"
        ;;
        
    2)
        echo -e "${BLUE}Setting up Mobile App...${NC}"
        cd mobile-app
        
        # Install dependencies
        echo -e "${BLUE}Installing Node.js dependencies...${NC}"
        npm install
        
        # Copy environment file
        if [ ! -f .env ]; then
            echo -e "${BLUE}Creating .env file...${NC}"
            cp .env.example .env
            echo -e "${YELLOW}⚠ Please edit mobile-app/.env with your API URL${NC}"
        fi
        
        # iOS setup (if on macOS)
        if [[ "$OSTYPE" == "darwin"* ]]; then
            echo -e "${BLUE}Setting up iOS dependencies...${NC}"
            cd ios
            pod install
            cd ..
        fi
        
        echo -e "${GREEN}✓ Mobile app setup complete!${NC}"
        echo ""
        echo "Next steps:"
        echo "1. Edit mobile-app/.env with your API URL"
        echo "2. Start Metro: npm start"
        echo "3. Run on Android: npm run android"
        echo "4. Run on iOS: npm run ios (macOS only)"
        ;;
        
    3)
        echo -e "${BLUE}Setting up both Backend and Mobile App...${NC}"
        
        # Backend setup
        echo -e "${BLUE}Setting up Backend...${NC}"
        cd backend
        python3 -m venv venv
        source venv/bin/activate
        pip install --upgrade pip
        pip install -r requirements.txt
        if [ ! -f .env ]; then
            cp .env.example .env
        fi
        cd ..
        
        # Mobile app setup
        echo -e "${BLUE}Setting up Mobile App...${NC}"
        cd mobile-app
        npm install
        if [ ! -f .env ]; then
            cp .env.example .env
        fi
        if [[ "$OSTYPE" == "darwin"* ]]; then
            cd ios
            pod install
            cd ..
        fi
        cd ..
        
        echo -e "${GREEN}✓ Complete setup finished!${NC}"
        echo ""
        echo "Next steps:"
        echo "1. Edit backend/.env with your database credentials"
        echo "2. Edit mobile-app/.env with your API URL"
        echo "3. Create database: createdb school_erp_db"
        echo "4. Run backend migrations: cd backend && python manage.py migrate"
        echo "5. Create superuser: python manage.py createsuperuser"
        echo "6. Start backend: python manage.py runserver"
        echo "7. Start mobile app: cd mobile-app && npm start"
        ;;
        
    4)
        echo "Exiting..."
        exit 0
        ;;
        
    *)
        echo -e "${RED}Invalid choice${NC}"
        exit 1
        ;;
esac

echo ""
echo -e "${GREEN}=========================================="
echo "Setup Complete! 🎉"
echo "==========================================${NC}"
echo ""
echo "For detailed instructions, see:"
echo "- QUICK_START.md"
echo "- INSTALLATION_GUIDE.md"
echo ""
