import os
from dotenv import load_dotenv
import sentry_sdk

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# SECURITY WARNING: Modify this secret key if using in production!
SECRET_KEY = "6few3nci_q_o@l1dlbk81%wcxe!*6r29yu629&d97!hiqat9fa"

DEFAULT_AUTO_FIELD='django.db.models.AutoField'
load_dotenv()
db_name = os.getenv('db_name')
db_user = os.getenv('db_user')
password = os.getenv('password')
port = os.getenv('port')
host = os.getenv('host')
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': db_name,
        'USER': db_user,
        'PASSWORD': password,
        'HOST': host,
        'PORT': port,
    },
    'OPTIONS': {
        'options': '-c statement_timeout=5000' # Here
     }
}


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
