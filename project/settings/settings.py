from .base import *

SECRET_KEY = os.environ['SECRET_KEY']

DEBUG = os.environ.get('DEBUG', 'True') == 'True'
INTERNAL = os.environ.get('INTERNAL') == 'True'

LANGUAGE_CODE = os.environ.get('LANGUAGE_CODE', 'en-us')
TIME_ZONE = os.environ.get('TIME_ZONE', 'UTC')

SCHEME = os.environ.get('SERVER_SCHEME', 'https')
HOSTS = os.environ['SERVER_HOSTS'].split(';')
CLIENTS = os.environ.get('SERVER_CLIENTS', '')
CLIENTS = CLIENTS.split(';') if CLIENTS else []
REGEX_CLIENTS = os.environ.get('SERVER_REGEX_CLIENTS')
REGEX_CLIENTS = REGEX_CLIENTS.split(';') if REGEX_CLIENTS else []

ALLOWED_HOSTS = HOSTS
CORS_ORIGIN_WHITELIST = (
        ['{}://{}'.format(SCHEME, host) for host in HOSTS]
        + [client if '://' in client else '{}://{}'.format(SCHEME, client) for client in HOSTS]
)
CORS_ORIGIN_REGEX_WHITELIST = REGEX_CLIENTS

ADMIN_PREFIX = os.environ.get('ADMIN_PREFIX')


if DEBUG:
    REST_FRAMEWORK = {
        'DEFAULT_AUTHENTICATION_CLASSES': (
            'rest_base.authentication.CsrfExemptSessionAuthentication',
            'rest_base.authentication.TokenAuthentication',
        ),
    }
else:
    REST_FRAMEWORK = {
        'DEFAULT_AUTHENTICATION_CLASSES': (
            'rest_base.authentication.TokenAuthentication',
        ),
        'DEFAULT_RENDERER_CLASSES': (
            'rest_framework.renderers.JSONRenderer',
        )
    }


if os.environ.get('VERBOSE') == 'True':
    LOGGING = {
        'version': 1,
        'handlers': {
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
            },
        },
        'loggers': {
            'django.db.backends': {
                'handlers': ['console'],
                'level': 'DEBUG',
            }
        }
    }


CONN_MAX_AGE = os.environ.get('POSTGRES_CONN_MAX_AGE', None)
try:
    CONN_MAX_AGE = int(CONN_MAX_AGE)
except TypeError:
    pass
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': os.environ['POSTGRES_HOST'],
        'NAME': os.environ['POSTGRES_NAME'],
        'USER': os.environ.get('POSTGRES_USER', ''),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD', ''),
        'PORT': os.environ.get('POSTGRES_PORT', ''),
        'CONN_MAX_AGE': CONN_MAX_AGE,
        'OPTIONS': {
            'sslmode': os.environ.get('POSTGRES_SSL', 'allow'),
        },
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '{}:{}'.format(os.environ.get('CACHE_HOST', 'localhost'), os.environ.get('CACHE_PORT', 11211)),
    }
}

SENTRY_HOST = os.environ.get('SENTRY_HOST')
SENTRY_VERBOSE = os.environ.get('SENTRY_VERBOSE') == 'True'
