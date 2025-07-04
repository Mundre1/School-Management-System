# 🔧 MANUAL SETUP - Step by Step

## Run These Commands ONE BY ONE

Copy and paste each command, wait for it to finish, then run the next one.

---

## Step 1: Navigate and Activate

```bash
cd "/Users/ayush/Desktop/School /smart-school-erp/backend"
source venv/bin/activate
```

---

## Step 2: Install setuptools

```bash
pip install setuptools
```

Wait for this to complete!

---

## Step 3: Install Django

```bash
pip install Django==4.2.7
```

---

## Step 4: Install DRF

```bash
pip install djangorestframework==3.14.0
```

---

## Step 5: Install python-decouple

```bash
pip install python-decouple==3.8
```

---

## Step 6: Install JWT

```bash
pip install djangorestframework-simplejwt==5.3.0
```

---

## Step 7: Install CORS

```bash
pip install django-cors-headers==4.3.1
```

---

## Step 8: Install WhiteNoise

```bash
pip install whitenoise==6.6.0
```

---

## Step 9: Install Pillow

```bash
pip install Pillow
```

---

## Step 10: Install django-filter

```bash
pip install django-filter==23.5
```

---

## Step 11: Install drf-yasg

```bash
pip install drf-yasg==1.21.7
```

---

## Step 12: Install utilities

```bash
pip install python-dateutil==2.8.2 pytz==2023.3
```

---

## Step 13: Create .env file

```bash
cp .env.example .env
echo "USE_SQLITE=True" >> .env
```

---

## Step 14: Run migrations

```bash
python manage.py migrate
```

---

## Step 15: Create admin user

```bash
python manage.py createsuperuser
```

Enter:
- Email: `admin@school.com`
- First name: `Admin`
- Last name: `User`
- Password: `admin123`

---

## Step 16: Start server

```bash
python manage.py runserver
```

---

## ✅ Open in Browser:

- **Admin:** http://localhost:8000/admin/
- **API Docs:** http://localhost:8000/swagger/
- **API:** http://localhost:8000/api/v1/

---

## 🎉 Done!

Your Smart School ERP is now running!
