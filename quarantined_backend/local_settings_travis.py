# SECURITY WARNING: keep the secret key used in production secret!
import os

from quarantined_backend.settings import BASE_DIR

SECRET_KEY = "%5r@$^)+$$#$%ˆˆ%ˆˆˆˆ%$%%$&ˆˆFFDFDSFSDF@$@#DSSFDZzzzSAe3n%fm_"

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
# We do not support sqlite anymore
DATABASES = {
    "default": {
        "ENGINE": "django.contrib.gis.db.backends.postgis",
        "NAME": "travis_ci_test",
        "USER": "postgres",
        "PASSWORD": "",
        "HOST": "localhost",
        "PORT": "5432",
    }
}
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static/")

ALLOWED_HOSTS = []
