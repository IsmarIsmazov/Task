ALLOWED_HOSTS = ["*"]

CREATE_APPS = [
    "apps.users",
    "apps.task",
]

INSTALLED_LIBRARY = [
    'django_filters',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_simplejwt',
    'jazzmin'
]
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
INSTALLED_APPS = INSTALLED_LIBRARY + CREATE_APPS + DJANGO_APPS
