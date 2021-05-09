web: gunicorn core.wsgi --log-file 
web : daphne core.asgi 
worker: python manage.py runworker channels -v2