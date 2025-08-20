# 🏔️ Yeti App

Simple Flask + static site that serves Yeti info and a small JSON API.

## Run locally
```bash
pip install -r requirements.txt
python app.py
# open http://localhost:5000
```

## Deploy to Render
- Connect this repo, choose **Instance Type: Starter** to keep it **always on**.
- Build: `pip install -r requirements.txt`
- Start: `gunicorn app:app`
- Health check: `/health`
