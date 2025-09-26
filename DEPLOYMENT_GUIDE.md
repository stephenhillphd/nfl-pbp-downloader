# Deployment Guide for NFL Play-by-Play Data Downloader

## Option 1: Streamlit Community Cloud (Recommended)

### Prerequisites
1. GitHub account
2. Streamlit Community Cloud account (free)

### Steps

1. **Create a GitHub Repository**
   - Go to [GitHub](https://github.com) and create a new repository
   - Name it something like `nfl-pbp-downloader`
   - Make it public (required for free hosting)

2. **Upload Your Files**
   - Upload these files to your repository:
     - `nfl_pbp_downloader.py`
     - `requirements.txt`
     - `README.md`

3. **Sign up for Streamlit Community Cloud**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Sign in with your GitHub account
   - Authorize Streamlit to access your repositories

4. **Deploy Your App**
   - Click "New app"
   - Select your repository (`your-username/nfl-pbp-downloader`)
   - Select branch (usually `main`)
   - Main file path: `nfl_pbp_downloader.py`
   - Click "Deploy"

5. **Wait for Deployment**
   - The app will take 2-5 minutes to deploy
   - You'll get a URL like: `https://your-app-name.streamlit.app`

### Resource Limits
- 1 GB of RAM
- 1 GB of storage
- Apps sleep after 7 days of inactivity (automatically wake up when accessed)

---

## Option 2: Hugging Face Spaces

### Steps

1. **Create a Hugging Face Account**
   - Go to [huggingface.co](https://huggingface.co) and sign up

2. **Create a New Space**
   - Click on "Spaces" → "Create new Space"
   - Name your space (e.g., `nfl-pbp-downloader`)
   - Select "Streamlit" as the SDK
   - Choose "Public" for free hosting

3. **Upload Files**
   - Create these files in your Space:
     - `app.py` (rename `nfl_pbp_downloader.py` to `app.py`)
     - `requirements.txt`
     - `README.md`

4. **Your App URL**
   - `https://huggingface.co/spaces/your-username/nfl-pbp-downloader`

### Resource Limits
- 16 GB RAM (free tier)
- 50 GB storage
- No sleep time

---

## Option 3: Render (Limited Free Tier)

### Note
Render's free tier spins down after 15 minutes of inactivity and has limited monthly hours.

### Steps

1. **Prepare Your Repository**
   - Add a `render.yaml` file to your GitHub repo

2. **Sign up for Render**
   - Go to [render.com](https://render.com)
   - Connect your GitHub account

3. **Deploy**
   - New → Web Service
   - Connect your repository
   - Use these settings:
     - Build Command: `pip install -r requirements.txt`
     - Start Command: `streamlit run nfl_pbp_downloader.py --server.port $PORT`

---

## Preparation Checklist

Before deploying, ensure you have:
- [ ] `nfl_pbp_downloader.py` - Your main app file
- [ ] `requirements.txt` - Python dependencies
- [ ] `README.md` - Project documentation
- [ ] A GitHub account (for most platforms)

## Tips for Successful Deployment

1. **Keep requirements.txt minimal** - Only include necessary packages
2. **Test locally first** - Make sure the app runs without errors
3. **Consider data size** - NFL play-by-play data can be large; be mindful of memory limits
4. **Add error handling** - Help users understand when limits are reached

## Recommended: Streamlit Community Cloud

For this app, I recommend Streamlit Community Cloud because:
- It's specifically designed for Streamlit apps
- Completely free with generous limits
- Easy GitHub integration
- Automatic HTTPS
- Custom domains supported
- Built-in secrets management

Your app will be available at a URL like:
`https://nfl-pbp-downloader.streamlit.app`
