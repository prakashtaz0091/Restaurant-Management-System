import os
from celery import Celery

django_env = os.getenv("DJANGO_ENV", 'development')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', f'config.settings.{django_env}')

app = Celery('config')
app.config_from_object('django.conf:settings', namespace='CELERY')

# Auto-discover tasks.py in all installed apps
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')