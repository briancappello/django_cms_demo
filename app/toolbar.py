from django_cms_demo import settings


def show_toolbar(request):
    return settings.DEBUG
