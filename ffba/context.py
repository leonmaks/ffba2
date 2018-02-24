from django.conf import settings # import the settings file


# Site settings

SITE_TITLE = "FFBA"


def site_settings(request): # pylint: disable-msg=W0613
    return {
        "SITE_TITLE": SITE_TITLE,
    }
