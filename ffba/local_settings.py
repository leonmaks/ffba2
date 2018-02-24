from .settings import *

DEBUG = True

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "ffba_empty",
        "USER": "ffba_empty",
        "PASSWORD": "e__",
        "HOST": "localhost",
        "PORT": "5432",
    },
}


def show_toolbar(request):
    return True


DEBUG_TOOLBAR_CONFIG = {
    "SHOW_TOOLBAR_CALLBACK" : show_toolbar,
}
