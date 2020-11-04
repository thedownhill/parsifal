import os
from decouple import config, Csv
# from mendeley import Mendeley
# import dj_database_url
# from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
CSRF_COOKIE_SECURE = config('CSRF_COOKIE_SECURE', default=True, cast=bool)
SESSION_COOKIE_SECURE = config('SESSION_COOKIE_SECURE', default=True, cast=bool)

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(PROJECT_DIR)

DEBUG = config('DEBUG', default=False, cast=bool)
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

SESSION_ENGINE = "django.contrib.sessions.backends.file"
ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())

ADMINS = (
    ('Daniel Ginzburg', 'danilgin4@gmail.com'),
)

MANAGERS = ADMINS

TIME_ZONE = 'UTC'
LANGUAGE_CODE = 'en-us'

USE_I18N = True
USE_L10N = True
USE_TZ = True

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
FILE_UPLOAD_TEMP_DIR = '/tmp/'
FILE_UPLOAD_PERMISSIONS = 0o644
FILE_UPLOAD_MAX_MEMORY_SIZE = 33554432

STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'SciLRtool/static'),
    os.path.join(BASE_DIR, 'SciLRtool/account_settings/static'),
    os.path.join(BASE_DIR, 'SciLRtool/activities/static'),
    os.path.join(BASE_DIR, 'SciLRtool/library/static'),
    os.path.join(BASE_DIR, 'SciLRtool/reviews/static'),
    os.path.join(BASE_DIR, 'SciLRtool/reviews/conducting/static'),
    os.path.join(BASE_DIR, 'SciLRtool/reviews/planning/static'),
)

SECRET_KEY = config('SECRET_KEY')

MIDDLEWARE = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    # 'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
)

ROOT_URLCONF = 'SciLRtool.urls'

WSGI_APPLICATION = 'SciLRtool.wsgi.application'

# TEMPLATE_DIRS = (
#     PROJECT_DIR.child('templates'),
# )

# TEMPLATE_CONTEXT_PROCESSORS = TCP + (
#     'django.core.context_processors.request',
# )
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media'
            ],
        },
    },
]


INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.humanize',

    'SciLRtool.reviews',
    'SciLRtool.reviews.planning',
    'SciLRtool.reviews.conducting',
    'SciLRtool.reviews.reporting',
    'SciLRtool.reviews.settings',
    'SciLRtool.account_settings',
    'SciLRtool.activities',
    'SciLRtool.authentication',
    'SciLRtool.blog',
    'SciLRtool.core',
    'SciLRtool.help',
    'SciLRtool.library',
    'SciLRtool.search',
)

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LOGIN_URL = '/signin/'
LOGOUT_URL = '/signout/'

# EMAIL_BACKEND = config('EMAIL_BACKEND', default='django.core.mail.backends.smtp.EmailBackend')
# EMAIL_FILE_PATH = PROJECT_DIR.parent.child('maildumps')
# EMAIL_HOST = config('EMAIL_HOST')
# EMAIL_PORT = config('EMAIL_PORT', cast=int)
# EMAIL_HOST_USER = config('EMAIL_HOST_USER')
# EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
# EMAIL_USE_TLS = config('EMAIL_USE_TLS', cast=bool)
# DEFAULT_FROM_EMAIL = 'Parsifal Team <noreply@parsif.al>'
# EMAIL_SUBJECT_PREFIX = '[Parsifal] '
# SERVER_EMAIL = 'application@parsif.al'

# MENDELEY_ID = config('MENDELEY_ID', cast=int)
# MENDELEY_SECRET = config('MENDELEY_SECRET')
# MENDELEY_REDIRECT_URI = config('MENDELEY_REDIRECT_URI')
# MENDELEY = Mendeley(MENDELEY_ID, client_secret=MENDELEY_SECRET, redirect_uri=MENDELEY_REDIRECT_URI)
#
# DROPBOX_APP_KEY = config('DROPBOX_APP_KEY')
# DROPBOX_SECRET = config('DROPBOX_SECRET')
# DROPBOX_REDIRECT_URI = config('DROPBOX_REDIRECT_URI')

# ELSEVIER_API_KEY = config('ELSEVIER_API_KEY')

ABSOLUTE_URL_OVERRIDES = {
    'auth.user': lambda u: '/%s/' % u.username,
}
