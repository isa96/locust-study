echo "gunicorn --bind localhost:8080 -w $1 wsgi:app"
gunicorn --bind localhost:8080 -w $1 wsgi:app