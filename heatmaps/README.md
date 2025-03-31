# Stock Market Heatmap

A Django application for visualizing stock market data as heatmaps.

## Deployment to Render.com - Step by Step Guide

### Prerequisites
- A [Render.com](https://render.com) account
- A Git repository with your project code
- Your project code pushed to GitHub, GitLab, or Bitbucket

### Step 1: Connect Your Repository
1. Log in to your Render dashboard
2. Click the "New" button in the upper right
3. Select "Blueprint" from the dropdown menu
4. Connect your GitHub/GitLab/Bitbucket account if not already connected
5. Select the repository containing your Django project

### Step 2: Configure Your Blueprint
1. Render will detect the `render.yaml` file in your repository
2. Review the services that will be created based on this file
3. Click "Apply" to begin the deployment process

### Step 3: Monitor Deployment
1. Render will create two services:
   - PostgreSQL database (`heatmaps_db`)
   - Web service (`heatmaps`)
2. The initial build may take a few minutes
3. You can monitor the build progress in the logs

### Step 4: Configure Environment Variables (if needed)
1. If any additional environment variables are needed:
   - Navigate to your web service dashboard
   - Click on "Environment" in the left sidebar
   - Add any additional environment variables
   - Click "Save Changes" and this will trigger a new deployment

### Step 5: Access Your Deployed Application
1. Once deployment is complete, click on the URL provided by Render
2. Your Django application should now be live!

### Step 6: Set Up Custom Domain (Optional)
1. From your web service dashboard, click "Settings"
2. Scroll to "Custom Domain"
3. Click "Add Custom Domain" and follow the instructions

## Development Setup

1. Clone the repository
2. Set up a virtual environment:
   ```
   python -m venv venv
   venv\Scripts\activate  # Windows
   source venv/bin/activate  # macOS/Linux
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Create a `.env` file based on `.env.example`
5. Run migrations:
   ```
   python manage.py migrate
   ```
6. Start the development server:
   ```
   python manage.py runserver
   ```

## Project Structure

- `heatmaps/` - Project settings and configuration
  - `settings/` - Split settings for different environments
    - `base.py` - Base settings shared across environments
    - `dev.py` - Development-specific settings
    - `prod.py` - Production-specific settings
- `stock/` - Main application
- `templates/` - HTML templates
- `static/` - Static files (CSS, JS, images)
- `build.sh` - Build script for Render deployment
- `render.yaml` - Render service configuration
