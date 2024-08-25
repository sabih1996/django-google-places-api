# Django Google Places API

Django project thats uses Googles places API to populate form fields

1) cd to development directory
2) mkvirtualenv django-google-places-api
3) mkdir ddjango-google-places-api
4) clone repository to new directory
5) pip install -r requirements.txt
6) Update settings.py with your email API information

    EMAIL_BACKEND = 'email url'
    EMAIL_HOST = ''
    EMAIL_PORT = ''
    EMAIL_USE_TLS = ''
    EMAIL_HOST_USER = ''
    DISPLAY_NAME = "Google places API demo email"
    DONOT_REPLY_EMAIL_PASSWORD = ''
    CURRENT_SITE = "XXX"

    GOOGLE_API_KEY = ""


7) python manage.py makemigrations
8) python manage.py migrate
9) python manage.py runserver
10) https://localhost:8000 

