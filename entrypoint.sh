exec gunicorn wsgi:app --name bot_service --workers 1 -b 0.0.0.0:5000 --log-level=debug --reload