# 🔧 Fix Setup Issues

## Issues Found:
1. ❌ PostgreSQL not installed (`pg_config` not found)
2. ❌ psycopg2-binary failed to install
3. ❌ Django not installed (because pip install failed)

## ✅ Solution (Follow These Steps)

### Step 1: Install PostgreSQL
```bash
brew install postgresql@15
```

Wait for installation to complete, then start the service:
```bash
brew services start postgresql@15
```

Add PostgreSQL to your PATH:
```bash
echo 'export PATH="/opt/homebrew/opt/postgresql@15/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

Verify installation:
```bash
psql --version
pg_config --version
```

---

### Step 2: Reinstall Python Dependencies

Make sure you're in the backend directory with virtual environment activated:
```bash
cd "/Users/ayush/Desktop/School /smart-school-erp/backend"
source venv/bin/activate
```

You should see `(venv)` in your prompt.

Now install dependencies again:
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

This should work now that PostgreSQL is installed!

---

### Step 3: Create Database
```bash
createdb school_erp_db
```

---

### Step 4: Run Migrations
```bash
python manage.py migrate
```

---

### Step 5: Create Superuser
```bash
python manage.py createsuperuser
```

Enter:
- Email: admin@school.com
- First name: Admin
- Last name: User
- Password: admin123

---

### Step 6: Start Server
```bash
python manage.py runserver
```

**✅ Backend should now be running at http://localhost:8000**

---

## 🎯 Quick Copy-Paste Commands

Run these commands one by one:

```bash
# 1. Install PostgreSQL
brew install postgresql@15
brew services start postgresql@15
echo 'export PATH="/opt/homebrew/opt/postgresql@15/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc

# 2. Navigate to backend and activate venv
cd "/Users/ayush/Desktop/School /smart-school-erp/backend"
source venv/bin/activate

# 3. Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# 4. Create database
createdb school_erp_db

# 5. Setup environment
cp .env.example .env

# 6. Run migrations
python manage.py migrate

# 7. Create superuser
python manage.py createsuperuser

# 8. Start server
python manage.py runserver
```

---

## 🐛 If Still Having Issues

### Issue: "brew: command not found"
Install Homebrew first:
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

### Issue: "psycopg2 still fails"
Try installing PostgreSQL development files:
```bash
brew install libpq
export LDFLAGS="-L/opt/homebrew/opt/libpq/lib"
export CPPFLAGS="-I/opt/homebrew/opt/libpq/include"
pip install psycopg2-binary
```

### Issue: "createdb: database already exists"
That's fine! Skip to the next step.

### Issue: "Django still not found"
Make sure virtual environment is activated:
```bash
source venv/bin/activate
# You should see (venv) in your prompt
pip list | grep Django
```

---

## ✅ Verification

After setup, verify everything works:

```bash
# Check Django is installed
python -c "import django; print(django.get_version())"

# Check database connection
python manage.py check

# Check migrations
python manage.py showmigrations
```

All should work without errors!

---

## 🎉 Success!

Once the server is running, open:
- **Admin Panel:** http://localhost:8000/admin/
- **API Docs:** http://localhost:8000/swagger/
- **API Root:** http://localhost:8000/api/v1/

Login with: admin@school.com / admin123

---

**Need more help? Check SETUP_NOW.md or INSTALLATION_GUIDE.md**
