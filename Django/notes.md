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