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

When setting the Base.html template. anything in the block content will happen to anything it extends to.

Do I make another USERS App specifically to signup/registration page

Make sub Template folders for different apps, but extend from the original BASE.html



**TODO LAB**
Start like regular

project todo_project
startapp todo_app and pages

make templates and static
- in pages make /pages and /todos sub dir AND add base.html to outer
    - add create, list, update .html files
- in static make /js and /css

ADD os.path.join to templates in Settings
ADD STATICFILES_DIRS os.path.join static

ON DATABASES in SETTINGs you are able to switch out the naming sqlite3 to postgresql or whatever DB your using.

on project URLS add path

add urls.py onto pages app and add route to index
on views pages, add functions to render html pages.

eventually makemigrations - migrate
make manage.py createsuperuser

START HERE*

create Todo model in todo_app to get DB
attributes
    - title max 200
    - text max 500
    - status booleanfield default False - checks true or false
    - create_at datetimefield auto_now_add = True, adds date and time
    - completed_at datetimefield blank = true and null = true
    - task_duration SAME as last

    add TODO_TYPE - tuple (
        - ('p', 'personal'),
        - ('f', 'family'),
        - ('h', 'house'),
        - ('m', 'misc'),
        - ('s', 'school'),
    )

    ** choices method ONLY LETS YOU CHOOSE FROM TODO_TYPE TUPLE
    todo_type = models.CharField(max_length=1, choices=TODO_TYPE, blank=True, default = 'm')

    Then add str and return self.title

    <!-- SETS ORDER -->
    add class Meta:
        - ordering = ['title', 'created_at']

AFTER finished models for app
you can specifiecally add makemigrations appname

then on app admin.py register app.


HEERERE-
then for list template, go to the views and import Todo model.
on list_todos function add 
    - todos = Todo.objects.all()
    - context = {
        'todos': todos,
    }
    return render(request, 'todos/list.html', context)
then on todos add jinja in a ul tag, 
    - forloop todo in todos 
        - make li's jinja todo.title
    - empty 
        -add p tag you have nothing
    - endfor


ON list template
    add add task button
    and li's with text below

On urls.py add - THESE ARE FUNCTIONS SPECIFICALLY TO THE APP NOT PROJECT
    - path('add/' views.add_todo
    - path('remove/' views.remove_todo
    - path('update/<int:id>' views.update
    - path('mark/>int:id>' views.mark
    - path('detail.<int:id>',views.detail
GO TO VIEWS AND ADD THESE
on views

add_todo
    -
remove_todo
    -
update(request, id)
    -
mark(request, id)
    -
details(request, id)
    - a_todo = Todo.onjects.get(id = id)
    - context = {
        'todo': a_todo - variable
    }

START HERE - 12/18

FOR add_todo go to create.html
    - create form action= http://localhost:8000/todos/add/ and post
    - add crsf_token
    <!-- title matches model att -->
    - add input title
    - add text area
    - Status and description | select button
    - add options true or false
    - add submit input
then render on views
AND on add_todos add 
    - if (request.method == 'GET):
        return render create.html
    elif (request.method == 'POST'):
        new_todo = Todo.objects.create( - THIS CREATES NEW POST, THIS IS LIKE USING save()
            title = request.POST['title'] - THIS IS GRABBING INFO FROM THE POST FORM
            text = request.POST['text']
            status = request.POST['status']
        )
        return redirect list page


ON todos base page add anchor   - also for anchor tag add http://localhost:8000/todos/add/ - to add to list

add detail.html template
    - add the four att from model, and anchors to each urls.py - mark done, remove, update, back to list

on list.html
- make the titles anchortags to go to todos/details when clicked that shows details of the model att


- OVERVIEW OF DETAIL 
    - when someone goes to id 1
        which the object will grab that id Todo.objects.get(id = id)


When path('todos/', include('todo_app.urls')) points-> to todo_app/urls.py it looks at which path('url/' was put into link, when action href was pushed. and depending on that, then looks at the views and looks at what function you set, views.add_todo, and does that function add_todo()
User request -> url.py -> views.py(selects function/template sends) -> Responds to User

<!-- When the form action happens it goes to the add/ function and it has a if elif statement. The if statement checks for the post method, then redirects to list page, and if it has get method then it adds to the model-->