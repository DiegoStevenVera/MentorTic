from .base import *
from .base import env

SECRET_KEY = env('DJANGO_SECRET_KEY', default='j@o-u_c_%3e$c@6xfa&35vabv!3%*pehu+$^#s5xfsrbdvrx+o')
ALLOWED_HOSTS = ['159.203.180.100', 'profsotelobd2.indagostudio.pe']
DEBUG = False
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'profsotelodb',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost',
        'PORT': '',
    }
}
