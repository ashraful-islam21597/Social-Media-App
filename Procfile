
web: daphne mybuddy.asgi:application --port $PORT --bind 0.0.0.0 -v2
python manage.py collectstatic --noinput
manage.py migrate
worker: python manage.py runworker channel_layer -v2
