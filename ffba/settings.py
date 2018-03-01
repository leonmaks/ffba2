"""
FFBA django settings.

Generated by 'django-admin startproject' using Django 2.0.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "1lv039s&v3-!a3b#*2&0^e%yi1yn6ar-7l!uz8x=jkuhmse+m#"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    # django apps
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # 3-rd party apps
    "widget_tweaks",
    "debug_toolbar",
    # my apps
    "misc",
    "org",
    "prod",
    "ae",
    "rpt",
]

# INSTALLED_APPS = [
#     # third party apps
#     "rest_framework",
# #     "betterforms",
#     "widget_tweaks",
#     "simple_history",
# #     "mptt",
#     "webpack_loader", # django-react integration
#     # my apps
#     "adm",
#     "misc",
#     "snippets",
#     "org",
#     "hr",
#     "acc",
#     "cashreg",
#     "prod",
#     "crm",
#     "pos",
#     "repl",
#     "djreact",
# ]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # 3rd party middleware
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    # my middleware
    "misc.middleware.RootMiddleware",
]


ROOT_URLCONF = "ffba.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(BASE_DIR, "ffba/templates"),
            os.path.join(BASE_DIR, "prod/templates"),
            os.path.join(BASE_DIR, "ae/templates"),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                # my context processors
                "ffba.context.site_settings",
            ],
        },
    },
]

# TEMPLATES = [
#     {
#         "OPTIONS": {
#             "debug": True,
#                 # my context processors
#                 # "prod.context_processors.messages",
#             ],
#         },
#     },
# ]

WSGI_APPLICATION = "wsgi.application"

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = "ru-RU"

TIME_ZONE = "Europe/Moscow"

USE_I18N = True

USE_L10N = True

USE_TZ = True

FORMAT_MODULE_PATH = [
    "ffba.formats",
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = "/static/"

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "ffba/static"),
]

STATIC_ROOT = "/usr/home/ffba/.wsp/ffba_test/ffba2/static_root"

LOGIN_URL = "/login/"
LOGIN_REDIRECT_URL = "/"
LOGOUT_URL = "/logout/"

DATE_FORMAT = "%d.%m.%Y"

# REST_FRAMEWORK = {
#     "DEFAULT_PERMISSION_CLASSES": [
#         "rest_framework.permissions.IsAdminUser",
#     ],
#     "PAGE_SIZE": 10
# }

# WEBPACK_LOADER = {
#     "DEFAULT": {
#         "BUNDLE_DIR_NAME": "bundles/local/",  # end with slash
#         "STATS_FILE": os.path.join(BASE_DIR, "webpack-stats-local.json"),
#     }
# }
