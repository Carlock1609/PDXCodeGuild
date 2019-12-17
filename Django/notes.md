The core of Django is the request-response cycle. A request is received by the server, it follows a route, actives a view, which then uses models and a template to generate a response, which is then rendered in the user's browser. The following docs will cover each of these topics in turn, but bear in mind that they're all interdependent.

    Route: a mapping between a URL and a view, uses regex
    View: a Python function which receives a request (url, parameters) and creates a response (html)
    Template: an html file with special syntax for filling in data
    Model: a Python class that parallels a database table

--
from django.urls import path
from . import views
app_name = 'todoapp'
urlpatterns = [
    # e.g. /detail/5, /detail/23
    path('detail/<int:todo_item_id>/', views.detail, name='detail')
]

def detail(request, todo_item_id):
    todo_item = get_object_or_404(TodoItem, pk=todo_item_id)
    return render(request, 'todoapp/detail.html', {'todo_item': todo_item})

Query Parameters

Query parameters are passed as part of the url and are turned into dictionary-like objects.

print(request.GET['todo_item_text'])

POST parameters

print(request.POST['todo_item_text'])
--

<form action="{% url 'todos:add' %}" method="post">
    // MUST HAVE TOKEN - csrf_token
    {% csrf_token %}
    <input type="text" name="todo_text"/>
    <button type="submit">+</button>
</form>



// HOW TO INSTALL PIPENV
get in desired fodler to have pipenv
- install pip env by py -3 -m install pipenv
- py -3 -m pipenv --version
- then initiate pip shell by py -3 -m pipenv shell 
- pip list for lsit of pip


// HOW TO INSTALL
- py -3 -m pip install django
-  specific version django===2.0

// CREATE ADMIN
 django-admin startproject hello_world .


 <!-- HOW TO START PROJECT -->
 django-admin startproject say_hello .
 python manage.py startapp say_hello

1. Go to settings.py
    1. install apps - adding say_hello to array
    2. On template array, add in "DIRS": [os.path.join(BASE_DIR, 'templates')]
2. Go to templates folder/ create outside apps
    1. add base.html and add index.html
    2. {% load static %} tells app too look for static folder
    3. edit base.html - add {% block content %} and {% endblock %} ** This helps you not have repeat yourself
    <!-- EXTENDS BASE.HTML means you don't have to write all the boilerplate again -->
    4. edit index.html - {% extends "base.html" %} and blockcontent/endblock
3. say_hello
    1. Create urls.py - import path, views, include - setup urlpatterns. and add say_hello urls to urlspattern, give it the route "/"
4. Go to views.py
    1. create function index(request): and have it render(request, "index.html")
5. create static folder and insert js and css folder outside of apps
    1. create site.css and main.js
    2. add bootstrap boilerplate, and axios cdn
    3. go to settings.py and add STATICFILES_DIRS array and add os.path.join to grab all static files
    4. link css and js to templates {% static 'css/site.css' %} for js as well.
6. Create Model

<!-- MODEL NOTES -->
1. ORM makes it easier to use a database rather than using SQL code
USING ORM - stuff.objects.all()
x = stuff.objects.all(id=1)
print(x.name)

2. lookup Field types

3. Nullable fields, if you a field is not required if field out, you must set params(null=True, blank=True) so it can be blank without errors


***
CLIENT
- browser

SERVER
- django framework
- python code
- database
- html templates

Client request to myapp.com/profile
Server reponds and sends html template back

URLS & VIEWS
# SERVER RECIEVES REQUEST TO /about
# THEN URL FIGURESOUT WHICH FUNCTION TO FIRE TO VIEWS
# IN THIS CASE INDEX
# VIEWS RECIEVES URL'S PICKED FUNCTION AND FIRES RESPONSE HTML TO BROWSER

# FROM . IMPORT VIEWS GETS THE PATH TO LOCAL VIEWS.py FILE

# DEPENDENCIES in migrations is tables that depend on other table data-- list will empty if the model does not use other DB for their data


** YOU ARE ABLE TO HAVE MULTIPLE APPS, IF YOU LIKE ONE APP YOU MADE SAY LIKE A BLOG, YOU CAN ADD THAT BLOG APP TO OTHER SITES


In project URLS it says "app.urls" which links to to the apps URL.py file

When setting the Base.html template. anything in the block content will happen to anything it extends to