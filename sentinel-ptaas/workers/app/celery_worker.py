from app.services.tasks import celery_app

# Expose celery app for worker entrypoint:
# celery -A workers.app.celery_worker worker --loglevel=info
app = celery_app
