from selloff_drf.config import (POSTGRES_HOST_DEV, POSTGRES_NAME_DEV,
                                POSTGRES_PASSWORD_DEV, POSTGRES_USER_DEV)


DATABASES = {
  'default': {
      'ENGINE': 'django.db.backends.postgresql_psycopg2',
      'NAME': POSTGRES_NAME_DEV,
      'USER': POSTGRES_USER_DEV,
      'PASSWORD': POSTGRES_PASSWORD_DEV,
      'HOST': POSTGRES_HOST_DEV,
      'PORT': ''
  }
}
