# coding: utf-8
import os

DEBUG = True

MEDIA_ROOT = 'media/'

from unipath import Path

PROJECT_DIR = Path(__file__).parent

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_DIR, 'database.db'),
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}
