

import os
from store.settings_verifcacar.base import  *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# DEBUG = False


# Application
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}





SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
SECURE_SSL_REDIRECT = False
