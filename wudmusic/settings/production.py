from .base import *
import dj_database_url
import django_heroku

DEBUG = True
SECRET_KEY = os.getenv('SECRET_KEY')
ALLOWED_HOSTS = ['wudmusic.herokuapp.com', 'wudmusic-bee92661c8ff.herokuapp.com', 'wudmusic.com', 'www.wudmusic.com',]

DATABASES = {
    'default': dj_database_url.config(conn_max_age=600, ssl_require=True)
}

django_heroku.settings(locals())
