web: gunicorn core.wsgi --log-file 
web : daphne core.asgi --port $PORT --bind 0.0.0.0 -v2 
worker: python manage.py runworker channels -v2