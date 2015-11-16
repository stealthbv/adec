from .base import *  # flake8: NOQA

DEBUG = True

try:
    from .local_settings import *
except ImportError:
    pass
