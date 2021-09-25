from auctionms.celery import celery_app
import os


__all__ = ('celery_app',)

settings_module = os.environ.get('FLAVOUR', 'dev')

if settings_module in ['prod', 'production']:
    from .production import *
elif settings_module in ['stag', 'staging']:
    from .staging import *
else:
    from .development import *

