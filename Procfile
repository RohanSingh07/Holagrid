web: gunicorn core.wsgi --log-file 
web: daphne core.asgi:channel_layer --port $PORT --bind 0.0.0.0 -v2
