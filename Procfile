web: gunicorn core.wsgi --preload --log-file -
web: daphne chat.asgi --port $PORT --bind 0.0.0.0 -v2