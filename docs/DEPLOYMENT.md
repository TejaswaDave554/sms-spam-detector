# Deployment Guide

## Prerequisites

1. Train the model first:
   ```bash
   python train_model.py
   ```

2. Set environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your values
   ```

## Heroku Deployment

```bash
heroku login
heroku create your-app-name
heroku config:set FLASK_ENV=production
heroku config:set SECRET_KEY=$(python -c 'import os; print(os.urandom(32).hex())')
git push heroku main
```

## Docker Deployment

```bash
docker-compose up -d
```

## AWS Elastic Beanstalk

```bash
eb init -p python-3.11 sms-spam-detector
eb create sms-spam-env
eb deploy
```

## Railway

1. Connect your GitHub repository
2. Add environment variables in dashboard
3. Deploy automatically on push

## Render

1. Create new Web Service
2. Connect repository
3. Set build command: `pip install -r requirements.txt`
4. Set start command: `gunicorn wsgi:app`
5. Add environment variables

## Health Check

All deployments expose `/health` endpoint for monitoring.
