# Deployment Guide

## Production Deployment

### Prerequisites
- Python 3.13+
- PostgreSQL 13+
- Node.js 14+
- nginx (recommended)
- SSL certificate

### Backend Deployment

#### 1. Server Setup
```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install Python and dependencies
sudo apt install python3.13 python3-pip python3-venv postgresql nginx -y
```

#### 2. Database Setup
```bash
# Create PostgreSQL database
sudo -u postgres psql
CREATE DATABASE school_erp;
CREATE USER school_admin WITH PASSWORD 'your_secure_password';
GRANT ALL PRIVILEGES ON DATABASE school_erp TO school_admin;
\q
```

#### 3. Application Setup
```bash
# Clone repository
git clone https://github.com/Mundre1/School-Management-System.git
cd School-Management-System/backend

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create .env file
cp .env.example .env
nano .env
```

#### 4. Environment Variables (.env)
```env
SECRET_KEY=your-secret-key-here
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com

# Database
DB_NAME=school_erp
DB_USER=school_admin
DB_PASSWORD=your_secure_password
DB_HOST=localhost
DB_PORT=5432

# CORS
CORS_ALLOWED_ORIGINS=https://yourdomain.com

# JWT
JWT_SECRET_KEY=your-jwt-secret-key
```

#### 5. Run Migrations
```bash
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py createsuperuser
```

#### 6. Gunicorn Setup
```bash
# Install gunicorn
pip install gunicorn

# Test gunicorn
gunicorn core.wsgi:application --bind 0.0.0.0:8000
```

#### 7. Systemd Service
Create `/etc/systemd/system/school-erp.service`:
```ini
[Unit]
Description=School ERP Django Application
After=network.target

[Service]
User=www-data
Group=www-data
WorkingDirectory=/path/to/School-Management-System/backend
Environment="PATH=/path/to/venv/bin"
ExecStart=/path/to/venv/bin/gunicorn --workers 3 --bind unix:/tmp/school-erp.sock core.wsgi:application

[Install]
WantedBy=multi-user.target
```

```bash
# Enable and start service
sudo systemctl enable school-erp
sudo systemctl start school-erp
sudo systemctl status school-erp
```

### Frontend Deployment

#### 1. Build React App
```bash
cd frontend
npm install
npm run build
```

#### 2. Nginx Configuration
Create `/etc/nginx/sites-available/school-erp`:
```nginx
server {
    listen 80;
    server_name yourdomain.com www.yourdomain.com;

    # Frontend
    location / {
        root /path/to/School-Management-System/frontend/build;
        try_files $uri $uri/ /index.html;
    }

    # Backend API
    location /api {
        proxy_pass http://unix:/tmp/school-erp.sock;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    # Static files
    location /static {
        alias /path/to/School-Management-System/backend/staticfiles;
    }

    # Media files
    location /media {
        alias /path/to/School-Management-System/backend/media;
    }
}
```

```bash
# Enable site
sudo ln -s /etc/nginx/sites-available/school-erp /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

#### 3. SSL Certificate (Let's Encrypt)
```bash
sudo apt install certbot python3-certbot-nginx -y
sudo certbot --nginx -d yourdomain.com -d www.yourdomain.com
```

### Docker Deployment (Alternative)

#### 1. Create Dockerfile (Backend)
```dockerfile
FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["gunicorn", "core.wsgi:application", "--bind", "0.0.0.0:8000"]
```

#### 2. Create docker-compose.yml
```yaml
version: '3.8'

services:
  db:
    image: postgres:13
    environment:
      POSTGRES_DB: school_erp
      POSTGRES_USER: school_admin
      POSTGRES_PASSWORD: your_password
    volumes:
      - postgres_data:/var/lib/postgresql/data

  backend:
    build: ./backend
    command: gunicorn core.wsgi:application --bind 0.0.0.0:8000
    volumes:
      - ./backend:/app
    ports:
      - "8000:8000"
    depends_on:
      - db
    environment:
      - DATABASE_URL=postgresql://school_admin:your_password@db:5432/school_erp

  frontend:
    build: ./frontend
    ports:
      - "3000:80"
    depends_on:
      - backend

volumes:
  postgres_data:
```

#### 3. Deploy with Docker
```bash
docker-compose up -d
docker-compose exec backend python manage.py migrate
docker-compose exec backend python manage.py createsuperuser
```

## Monitoring

### Setup Logging
```python
# settings.py
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': '/var/log/school-erp/error.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'ERROR',
            'propagate': True,
        },
    },
}
```

### Health Check Endpoint
Add to `urls.py`:
```python
from django.http import JsonResponse

def health_check(request):
    return JsonResponse({'status': 'healthy'})

urlpatterns = [
    path('health/', health_check),
    ...
]
```

## Backup

### Database Backup
```bash
# Create backup
pg_dump -U school_admin school_erp > backup_$(date +%Y%m%d).sql

# Restore backup
psql -U school_admin school_erp < backup_20260527.sql
```

### Automated Backups
Create cron job:
```bash
crontab -e

# Daily backup at 2 AM
0 2 * * * pg_dump -U school_admin school_erp > /backups/school_erp_$(date +\%Y\%m\%d).sql
```

## Security Checklist

- [ ] Change SECRET_KEY
- [ ] Set DEBUG=False
- [ ] Configure ALLOWED_HOSTS
- [ ] Use HTTPS
- [ ] Set secure cookies
- [ ] Configure CORS properly
- [ ] Use strong database password
- [ ] Enable firewall
- [ ] Regular security updates
- [ ] Setup monitoring
- [ ] Configure backups

## Performance Optimization

### Database
- Add indexes to frequently queried fields
- Use database connection pooling
- Enable query caching

### Static Files
- Use CDN for static files
- Enable gzip compression
- Set proper cache headers

### Application
- Use Redis for caching
- Enable Django's cache framework
- Optimize database queries

## Troubleshooting

### Common Issues

**502 Bad Gateway**
- Check if gunicorn is running
- Check nginx configuration
- Check socket file permissions

**Static files not loading**
- Run `collectstatic`
- Check nginx static file configuration
- Verify file permissions

**Database connection errors**
- Check PostgreSQL is running
- Verify database credentials
- Check firewall rules

## Support

For deployment issues, contact: gymnasticaayush123@gmail.com
