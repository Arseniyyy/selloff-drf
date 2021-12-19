from selloff_drf.config import (POSTGRES_HOST_PROD, POSTGRES_NAME_PROD,
                                POSTGRES_PASSWORD_PROD, POSTGRES_PORT_PROD,
                                POSTGRES_USER_PROD)


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': POSTGRES_NAME_PROD,
        'USER': POSTGRES_USER_PROD,
        'PASSWORD': POSTGRES_PASSWORD_PROD,
        'HOST': POSTGRES_HOST_PROD,
        'PORT': POSTGRES_PORT_PROD,
    }
}
