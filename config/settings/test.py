from .base import *  # noqa

DEBUG = False
DATABASES["default"]["NAME"] = env("POSTGRES_DB", default="paa_test")  # noqa: F405
