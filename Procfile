web: gunicorn core.wsgi:application --log-file 
web : daphne core.asgi:application --port $PORT --bind 0.0.0.0 -v2 
worker: python manage.py runworker channels -v2