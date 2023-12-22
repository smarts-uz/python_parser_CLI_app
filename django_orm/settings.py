import os
from dotenv import load_dotenv
import sentry_sdk

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# SECURITY WARNING: Modify this secret key if using in production!
SECRET_KEY = "6few3nci_q_o@l1dlbk81%wcxe!*6r29yu629&d97!hiqat9fa"

DEFAULT_AUTO_FIELD='django.db.models.AutoField'
load_dotenv()
name = os.getenv('name')
password = os.getenv('password')
port = os.getenv('port')
host = os.getenv('host')
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': name,
        'USER': name,
        'PASSWORD': password,
        'HOST': host,
        'PORT': port,
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'postgres',
#         'USER': 'postgres',
#         'PASSWORD': '2308',
#         'HOST': 'localhost',
#         'PORT': '5433'}
# }


"""
To connect to an existing postgres database, first:
pip install psycopg2
then overwrite the settings above with:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'YOURDB',
        'USER': 'postgres',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '',
    }
}
"""
sentry_dsn = os.getenv('dsn')
sentry_sdk.init(
    dsn=sentry_dsn,
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    traces_sample_rate=1.0,
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.
    profiles_sample_rate=1.0,
)

INSTALLED_APPS = ("django_orm.db",)
# INSTALLED_APPS = ("db",)
