wsgi_app = 'imdb.wsgi:application'
loglevel = 'debug'
workers = 2
bind = '0.0.0.0:8000'

accesslog = '/var/log/gunicorn/imdb.log'
errorlog = '/var/log/gunicorn/imdb.log'

capture_output = True