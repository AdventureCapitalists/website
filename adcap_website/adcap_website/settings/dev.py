from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

for template_engine in TEMPLATES:
    template_engine['OPTIONS']['debug'] = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'sb9fr%!hv&$0rnj8%4!k_sjzk$(l41%&jeii6^fjmq4)y(@m!0'


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


try:
    from .local import *
except ImportError:
    pass
