mkdir exampleDjango
cd exampleDjango

pipenv shell
pipenv install django
django-admin startproject mysite .

python3 manage.py createsuperuser

python3 manage.py startapp pages
touch pages/urls.py

mkdir templates
touch templates/base.html
mkdir static
mkdir static/css
mkdir static/js
touch static/css/styles.css
touch static/js/app.js

make changes in settings
INSTALLED APPS
add 'pages',

TEMPLATES
os.path.join(BASE_DIR, 'templates')

STATIC
STATICFILES_DIRS = [(os.path.join(BASE_DIR, 'static'))]

python3 manage.py makemigrations
python3 manage.py migrate