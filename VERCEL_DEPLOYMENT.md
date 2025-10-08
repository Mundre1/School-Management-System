# Vercel Deployment Guide

## 🚀 Deploy to Vercel

### Prerequisites
- GitHub account
- Vercel account (sign up at https://vercel.com)
- Code pushed to GitHub repository

### Step-by-Step Deployment

#### 1. Install Vercel CLI (Optional)
```bash
npm install -g vercel
```

#### 2. Deploy via Vercel Dashboard (Recommended)

1. **Go to Vercel Dashboard**
   - Visit: https://vercel.com/dashboard
   - Click "Add New Project"

2. **Import Git Repository**
   - Click "Import Git Repository"
   - Select your GitHub account
   - Choose: `Mundre1/School-Management-System`
   - Click "Import"

3. **Configure Project**
   - **Framework Preset:** Create React App
   - **Root Directory:** `frontend`
   - **Build Command:** `npm run build`
   - **Output Directory:** `build`
   - **Install Command:** `npm install`

4. **Environment Variables**
   Add these in Vercel dashboard:
   ```
   REACT_APP_API_URL=http://localhost:8000
   ```
   (You'll update this with your backend URL later)

5. **Deploy**
   - Click "Deploy"
   - Wait for build to complete
   - Your site will be live at: `https://your-project.vercel.app`

#### 3. Deploy via Vercel CLI

```bash
# Login to Vercel
vercel login

# Navigate to project
cd /Users/ayush/Desktop/School\ /smart-school-erp

# Deploy
vercel

# Follow prompts:
# - Set up and deploy? Yes
# - Which scope? Your account
# - Link to existing project? No
# - Project name? school-management-system
# - Directory? ./frontend
# - Override settings? No

# Deploy to production
vercel --prod
```

### Backend Deployment Options

Since Vercel is primarily for frontend, you need to deploy the backend separately:

#### Option 1: Railway (Recommended - Free Tier)

1. **Go to Railway**
   - Visit: https://railway.app
   - Sign in with GitHub

2. **New Project**
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Choose your repository
   - Select "backend" as root directory

3. **Add PostgreSQL**
   - Click "New"
   - Select "Database"
   - Choose "PostgreSQL"

4. **Environment Variables**
   ```
   SECRET_KEY=your-secret-key
   DEBUG=False
   ALLOWED_HOSTS=.railway.app
   DATABASE_URL=${{Postgres.DATABASE_URL}}
   CORS_ALLOWED_ORIGINS=https://your-vercel-app.vercel.app
   ```

5. **Deploy**
   - Railway will auto-deploy
   - Get your backend URL: `https://your-app.railway.app`

#### Option 2: Render (Free Tier)

1. **Go to Render**
   - Visit: https://render.com
   - Sign in with GitHub

2. **New Web Service**
   - Click "New +"
   - Select "Web Service"
   - Connect your repository

3. **Configure**
   - **Name:** school-erp-backend
   - **Root Directory:** backend
   - **Environment:** Python 3
   - **Build Command:** 
     ```
     pip install -r requirements-sqlite.txt && python manage.py collectstatic --noinput && python manage.py migrate
     ```
   - **Start Command:** 
     ```
     gunicorn core.wsgi:application
     ```

4. **Environment Variables**
   Same as Railway above

#### Option 3: PythonAnywhere (Free Tier)

1. **Sign up at PythonAnywhere**
   - Visit: https://www.pythonanywhere.com
   - Create free account

2. **Upload Code**
   ```bash
   # Clone your repo in PythonAnywhere console
   git clone https://github.com/Mundre1/School-Management-System.git
   ```

3. **Setup Virtual Environment**
   ```bash
   cd School-Management-System/backend
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements-sqlite.txt
   ```

4. **Configure Web App**
   - Go to "Web" tab
   - Add new web app
   - Choose manual configuration
   - Python 3.10
   - Set source code: `/home/yourusername/School-Management-System/backend`
   - Set virtualenv: `/home/yourusername/School-Management-System/backend/venv`

5. **WSGI Configuration**
   Edit WSGI file:
   ```python
   import sys
   import os
   
   path = '/home/yourusername/School-Management-System/backend'
   if path not in sys.path:
       sys.path.append(path)
   
   os.environ['DJANGO_SETTINGS_MODULE'] = 'core.settings'
   
   from django.core.wsgi import get_wsgi_application
   application = get_wsgi_application()
   ```

### Update Frontend API URL

After deploying backend, update frontend:

1. **Update API URL in Vercel**
   - Go to Vercel Dashboard
   - Select your project
   - Go to Settings > Environment Variables
   - Update `REACT_APP_API_URL` to your backend URL
   - Redeploy

2. **Or update in code**
   Edit `frontend/src/services/api.js`:
   ```javascript
   const API_URL = process.env.REACT_APP_API_URL || 'https://your-backend.railway.app';
   ```

### Custom Domain (Optional)

1. **In Vercel Dashboard**
   - Go to your project
   - Click "Settings" > "Domains"
   - Add your custom domain
   - Follow DNS configuration instructions

### Automatic Deployments

Vercel automatically deploys when you push to GitHub:
- **Push to main branch** → Production deployment
- **Push to other branches** → Preview deployment
- **Pull requests** → Preview deployment

### Monitoring

- **Vercel Dashboard:** Monitor deployments, logs, analytics
- **Vercel CLI:** `vercel logs` to view logs

### Troubleshooting

**Build Fails:**
- Check build logs in Vercel dashboard
- Verify all dependencies in package.json
- Check Node.js version compatibility

**API Connection Issues:**
- Verify REACT_APP_API_URL is set correctly
- Check CORS settings in backend
- Ensure backend is running

**Environment Variables Not Working:**
- Redeploy after adding env vars
- Check variable names (must start with REACT_APP_)

### Quick Deploy Commands

```bash
# Deploy to preview
vercel

# Deploy to production
vercel --prod

# View logs
vercel logs

# List deployments
vercel ls

# Remove deployment
vercel rm [deployment-url]
```

### Cost

- **Vercel:** Free tier includes:
  - Unlimited deployments
  - 100GB bandwidth/month
  - Automatic HTTPS
  - Custom domains

- **Railway:** Free tier includes:
  - $5 credit/month
  - 500 hours runtime
  - 1GB RAM
  - PostgreSQL database

### Support

For deployment issues:
- Vercel Docs: https://vercel.com/docs
- Railway Docs: https://docs.railway.app
- Email: gymnasticaayush123@gmail.com

---

## 🎉 Your App is Live!

**Frontend:** https://your-project.vercel.app  
**Backend:** https://your-backend.railway.app  
**Admin:** https://your-backend.railway.app/admin

**Login:** admin@school.com / admin123

---

**Last Updated:** May 27, 2026
