import os
from .base import *

DEBUG = False

AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = 'bqj5bm'

MEDIA_URL = 'http://' + AWS_STORAGE_BUCKET_NAME + '.s3.amazonaws.com/'

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

try:
    from .local_settings import *
except ImportError:
    pass
