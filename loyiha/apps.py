import os
import sys

from django.apps import AppConfig


class LoyihaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'loyiha'

    def ready(self):
        argv = sys.argv
        is_runserver = len(argv) > 1 and argv[1] == 'runserver'
        is_wsgi = any('wsgi' in a or 'gunicorn' in a or 'uvicorn' in a for a in argv)
        if not (is_runserver or is_wsgi):
            return

        # runserver autoreload ikki marta ishga tushiradi — faqat asosiy jarayonda
        if is_runserver and os.environ.get('RUN_MAIN') != 'true':
            return

        from loyiha.telegram_runner import start_bot_in_background
        start_bot_in_background()
