# This is an example settings/local.py file.
# These settings overrides what's in settings/base.py

from . import base

# To extend any settings from settings/base.py here's an example:
#INSTALLED_APPS = base.INSTALLED_APPS + ['debug_toolbar']

if 'RDS_HOSTNAME' in os.environ:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': os.environ['RDS_DB_NAME'],
            'USER': os.environ['RDS_USERNAME'],
            'PASSWORD': os.environ['RDS_PASSWORD'],
            'HOST': os.environ['RDS_HOSTNAME'],
            'PORT': os.environ['RDS_PORT'],
            'OPTIONS': {
                'init_command': 'SET storage_engine=InnoDB',
                'charset' : 'utf8',
                'use_unicode' : True,
            },
            'TEST_CHARSET': 'utf8',
            'TEST_COLLATION': 'utf8_general_ci',
        },
        # 'slave': {
        #     ...
        # },
    }
}

# Uncomment this and set to all slave DBs in use on the site.
# SLAVE_DATABASES = ['slave']

# Recipients of traceback emails and other notifications.
ADMINS = (
    ('Corey', 'cshields@mozilla.com'),
    # ('Your Name', 'your_email@domain.com'),
)
MANAGERS = ADMINS

# Debugging displays nice error messages, but leaks memory. Set this to False
# on all server instances and True only for development.
DEBUG = TEMPLATE_DEBUG = True

# Is this a development instance? Set this to True on development/master
# instances and False on stage/prod.
DEV = False

# By default, BrowserID expects your app to use http://127.0.0.1:8000
# Uncomment the following line if you prefer to access your app via localhost
# SITE_URL = 'http://localhost:8000'

# Playdoh ships with Bcrypt+HMAC by default because it's the most secure.
# To use bcrypt, fill in a secret HMAC key. It cannot be blank.
HMAC_KEYS = {
    '2014-06-11': 'notsecretchangeme',
}

from django_sha2 import get_password_hashers
PASSWORD_HASHERS = get_password_hashers(base.BASE_PASSWORD_HASHERS, HMAC_KEYS)

# Make this unique, and don't share it with anybody.  It cannot be blank.
SECRET_KEY = 'notsecretchangeme'

# Should robots.txt allow web crawlers?  Set this to True for production
ENGAGE_ROBOTS = True

# Uncomment these to activate and customize Celery:
# CELERY_ALWAYS_EAGER = False  # required to activate celeryd
# BROKER_HOST = 'localhost'
# BROKER_PORT = 5672
# BROKER_USER = 'playdoh'
# BROKER_PASSWORD = 'playdoh'
# BROKER_VHOST = 'playdoh'
# CELERY_RESULT_BACKEND = 'amqp'

## Log settings

# SYSLOG_TAG = "http_app_playdoh"  # Make this unique to your project.
# LOGGING = dict(loggers=dict(playdoh={'level': logging.DEBUG}))

# Common Event Format logging parameters
#CEF_PRODUCT = 'Playdoh'
#CEF_VENDOR = 'Mozilla'

# Uncomment this line if you are running a local development install without
# HTTPS to disable HTTPS-only cookies.
#SESSION_COOKIE_SECURE = False

