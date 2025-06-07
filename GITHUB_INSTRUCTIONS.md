# GitHub and Streamlit Deployment Instructions

## Setup GitHub Repository

1. Create a new repository on GitHub:
   - Go to https://github.com/new
   - Name your repository (e.g., "network-traffic-analyzer")
   - Select whether it should be public or private
   - Do not initialize with README, .gitignore, or license (we already have these)
   - Click "Create repository"

2. Fix permission issues (if you encountered them):
   - Close any applications that might be using the files
   - Try running PowerShell as Administrator
   - Check folder permissions in Windows Explorer (right-click → Properties → Security)
   - Alternative: Create a new folder elsewhere and copy all files there before initializing Git

3. Push to GitHub:
   ```
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/yourusername/your-repo-name.git
   git push -u origin main
   ```

## Deploying to Streamlit Cloud

1. Sign up for Streamlit Cloud:
   - Go to https://streamlit.io/cloud
   - Sign in with your GitHub account

2. Deploy your app:
   - Click "New app"
   - Select your repository, branch (main), and file path (app.py)
   - Click "Deploy"

3. Your app will be deployed and available at a URL like:
   https://yourusername-your-repo-name-app-xxxx.streamlit.app

## Running Locally

If you prefer to run locally before deploying:

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Run the Streamlit app:
   ```
   streamlit run app.py
   ```

3. Access in your browser at http://localhost:8501

## Project Structure

Your project should have these files:
- `tool.html` - Main HTML analyzer code
- `app.py` - Streamlit wrapper
- `requirements.txt` - Dependencies
- `README.md` - Project documentation
- `.gitignore` - Files to exclude from Git

## Troubleshooting Git Issues

If you continue to have permission issues with Git:

1. Try GitHub Desktop:
   - Download from https://desktop.github.com/
   - Add your local repository
   - Commit and push without command line

2. Or use GitHub web interface:
   - Create repository
   - Upload files directly
   - This is less ideal but works in a pinch 