from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
import dotenv

dotenv.read_dotenv(
    os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env'))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')

app = Celery('app')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks()
