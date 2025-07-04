# 🐘 Install PostgreSQL - Step by Step

## Run These Commands in Your Terminal:

### Step 1: Install PostgreSQL
```bash
brew install postgresql@15
```

This will take 2-3 minutes. Wait for it to complete.

### Step 2: Start PostgreSQL Service
```bash
brew services start postgresql@15
```

### Step 3: Add PostgreSQL to PATH
```bash
echo 'export PATH="/opt/homebrew/opt/postgresql@15/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

### Step 4: Verify Installation
```bash
psql --version
pg_config --version
which pg_config
```

You should see version numbers for all three commands.

---

## ✅ After PostgreSQL is Installed

Now you can install Python dependencies:

```bash
# Make sure you're in backend directory with venv activated
cd "/Users/ayush/Desktop/School /smart-school-erp/backend"
source venv/bin/activate

# Install dependencies (this will work now!)
pip install -r requirements.txt
```

---

## 🎯 Complete Setup Commands

After PostgreSQL is installed, run these:

```bash
# Create database
createdb school_erp_db

# Copy environment file
cp .env.example .env

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Start server
python manage.py runserver
```

---

## 🐛 If PostgreSQL Installation Fails

Try these alternatives:

### Option 1: Install via Postgres.app (Easier)
1. Download from: https://postgresapp.com/
2. Install and run the app
3. Click "Initialize" to create a new server
4. Add to PATH:
```bash
echo 'export PATH="/Applications/Postgres.app/Contents/Versions/latest/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

### Option 2: Use SQLite Instead (Temporary)
If you just want to test the app quickly, you can use SQLite:

Edit `backend/core/settings.py` and change the database configuration:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

Then you don't need PostgreSQL for now!

---

## 📝 Quick Reference

**Check if PostgreSQL is running:**
```bash
brew services list | grep postgresql
```

**Start PostgreSQL:**
```bash
brew services start postgresql@15
```

**Stop PostgreSQL:**
```bash
brew services stop postgresql@15
```

**Restart PostgreSQL:**
```bash
brew services restart postgresql@15
```

---

**Once PostgreSQL is installed, go back to the main setup! 🚀**
