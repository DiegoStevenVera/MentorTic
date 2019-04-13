from .base import *
from .base import env

SECRET_KEY = env('DJANGO_SECRET_KEY', default='j@o-u_c_%3e$c@6xfa&35vabv!3%*pehu+$^#s5xfsrbdvrx+o')
ALLOWED_HOSTS = ['167.99.110.46', ]
DEBUG = True
DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'mentortic',
        'USER': 'db_user',
        'PASSWORD': '72923854',
        'HOST': 'localhost',
        'PORT': '',
    }
}
