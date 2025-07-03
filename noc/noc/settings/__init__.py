from .base import *  # noqa
try:
    # override any setting by creating a local_settings.py
    from .local_settings import *  # noqa
except ImportError:
    pass

