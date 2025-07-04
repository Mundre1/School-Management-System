# ⚡ QUICK FIX - Get Running in 2 Minutes!

## 🎯 Use SQLite Instead of PostgreSQL (Easier for Development)

You can use SQLite for now and switch to PostgreSQL later!

---

## Step 1: Update Database Settings

Edit the settings file:
```bash
nano backend/core/settings.py
```

Find this section (around line 90):
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME', default='school_erp_db'),
        'USER': config('DB_USER', default='postgres'),
        'PASSWORD': config('DB_PASSWORD', default='password'),
        'HOST': config('DB_HOST', default='localhost'),
        'PORT': config('DB_PORT', default='5432'),
    }
}
```

Replace it with:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

Save and exit (Ctrl+X, then Y, then Enter)

---

## Step 2: Update Requirements

Remove psycopg2 from requirements temporarily:
```bash
cd "/Users/ayush/Desktop/School /smart-school-erp/backend"
source venv/bin/activate
```

Install dependencies without psycopg2:
```bash
pip install Django==4.2.7
pip install djangorestframework==3.14.0
pip install python-decouple==3.8
pip install djangorestframework-simplejwt==5.3.0
pip install django-cors-headers==4.3.1
pip install whitenoise==6.6.0
pip install Pillow==10.1.0
pip install drf-yasg==1.21.7
pip install django-filter==23.5
```

---

## Step 3: Run Migrations
```bash
python manage.py migrate
```

---

## Step 4: Create Superuser
```bash
python manage.py createsuperuser
```

Enter:
- Email: admin@school.com
- First name: Admin
- Last name: User
- Password: admin123

---

## Step 5: Start Server
```bash
python manage.py runserver
```

---

## ✅ Success!

Open in browser:
- **Admin Panel:** http://localhost:8000/admin/
- **API Docs:** http://localhost:8000/swagger/
- **API Root:** http://localhost:8000/api/v1/

Login: admin@school.com / admin123

---

## 🔄 Switch to PostgreSQL Later

When you're ready to use PostgreSQL:

1. Install PostgreSQL:
   ```bash
   brew install postgresql@15
   brew services start postgresql@15
   ```

2. Revert the database settings in `settings.py`

3. Install psycopg2:
   ```bash
   pip install psycopg2-binary
   ```

4. Create database and migrate:
   ```bash
   createdb school_erp_db
   python manage.py migrate
   ```

---

## 📝 Why SQLite for Now?

**Advantages:**
- ✅ No installation needed
- ✅ Works immediately
- ✅ Perfect for development
- ✅ Easy to test

**When to switch to PostgreSQL:**
- When deploying to production
- When you need advanced features
- When working with large datasets

---

**This gets you running immediately! 🚀**
