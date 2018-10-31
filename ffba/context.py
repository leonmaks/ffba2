from django.conf import settings


# Site settings

SITE_TITLE = "FFBA"


def site_settings(request):
    return {
        "SITE_TITLE": SITE_TITLE,
    }
