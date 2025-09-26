#!/bin/bash

# Quick Setup Script for NFL Play-by-Play Downloader Deployment

echo "🏈 NFL Play-by-Play Downloader - Deployment Setup"
echo "================================================"
echo ""

# Check if git is installed
if ! command -v git &> /dev/null; then
    echo "❌ Git is not installed. Please install git first."
    exit 1
fi

# Check if files exist
if [ ! -f "nfl_pbp_downloader.py" ]; then
    echo "❌ nfl_pbp_downloader.py not found in current directory"
    exit 1
fi

echo "✅ Found required files"
echo ""

# Initialize git repository if not already initialized
if [ ! -d ".git" ]; then
    echo "📁 Initializing git repository..."
    git init
    git add .
    git commit -m "Initial commit: NFL Play-by-Play Downloader"
    echo "✅ Git repository initialized"
else
    echo "✅ Git repository already exists"
fi

echo ""
echo "Next steps:"
echo "1. Create a new repository on GitHub:"
echo "   https://github.com/new"
echo ""
echo "2. Run these commands to push your code:"
echo "   git remote add origin https://github.com/YOUR_USERNAME/nfl-pbp-downloader.git"
echo "   git branch -M main"
echo "   git push -u origin main"
echo ""
echo "3. Deploy on Streamlit Community Cloud:"
echo "   - Go to https://share.streamlit.io"
echo "   - Sign in with GitHub"
echo "   - Click 'New app' and select your repository"
echo ""
echo "Happy deploying! 🚀"
