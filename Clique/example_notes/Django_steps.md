this document presents a high level overview of the steps i use to setup a django project. part 1 outlines how i setup the initial structure. part 2 outlines the specifics of setting up django for a specific project within the context of the todo list lab.

you should have an idea of the functionality you want in your app before you start working. this will help you organize your files and createa a plan to approach your project.

## part 1: django initial setup

0. create a directory for your project

1. `cd` into the directory you just created, then create your virtual environment using `pipenv`

    ```python

    pipenv shell

    ```

2. install django and ensure it was installed

    ```python

    pipenv install django

    pip list

    ```

    the output from the `pip list` command should be similar to the following (the output will depend on the version of django you installed):

    

    |Package  |  Version |

    ----------|----------|

    asgiref   | 3.2.3  

    Django    | 3.0    

    pip       | 19.3.1 

    pytz      | 2019.3 

    setuptools| 42.0.2 

    sqlparse  | 0.3.0  

    wheel     | 0.33.6 

3. create a django project with the command<br>

    ```django-admin startproject my_project_name .```

4. test to make sure the server runs<br>

    ```python manage.py runserver```<br>

    if everything was done correctly, you should see the default server page with the animated rocket.

    [](./django_scrnsht.png)

## part 2: todo list setup

there are many ways to approach a django project. this is just one version of how i do it. it's a general pattern i usually follow, but there are times when i deviate from this for no other reason than my thought process may not be the same from app to app. many of the steps are purely organizational and can be changed to fit whatever organizational scheme makes the most sense to you.

1. create an app with the command<br>

    ```python manage.py startapp todo_app``` <br>

        ```python manage.py startapp pages```

    go into your *my_project_name/settings.py* file and install your apps. add the name of your app to the list of installed apps like so:

    

    ```python

    INSTALLED_APPS = [

        'django.contrib.admin',

        'django.contrib.auth',

        'django.contrib.contenttypes',

        'django.contrib.sessions',

        'django.contrib.messages',

        'django.contrib.staticfiles',

        'pages',

        'todo_app',

    ]

    ```

2. create a template directory at the same level as the *to_do_app* and *my_project_name* directories. *templates* **should not** be nested inside another directory. inside of the templates folder create a folder called *pages* and another called *todos*. pages will hold basic pages that display a home page, an about page, etc. todos will hold pages that have something to do with our todo_list app.

3.  create a static directory at the same level as the *to_do_app*, *templates*, and *my_project_name* directories. *static* **should not** be nested inside another directory. inside of *static*, create two directories, *css* and *js*. inside of *css* create a **file** *site.css*. inside of *js* create a **file** *main.js*. inside of *site.css* add the following css:

    ```css

    h2 {

        color: firebrick;

    }

    ```

    inside *main.js* add the following:

    ```javascript

    console.log('hello from main.js')

    ```

4. we now need to tell django where to find our templates and static files. Open up *settings.py* in the *my_project_name* folder. modify the templates section to look like the following snippet. specifically you need to modify the 'DIRS' line by adding `os.path.join(BASE_DIR, 'templates')`.

    ```python

    TEMPLATES = [

        {

            'BACKEND': 'django.template.backends.django.DjangoTemplates',

            'DIRS': [os.path.join(BASE_DIR, 'templates')],

            'APP_DIRS': True,

            'OPTIONS': {

                'context_processors': [

                    'django.template.context_processors.debug',

                    'django.template.context_processors.request',

                    'django.contrib.auth.context_processors.auth',

                    'django.contrib.messages.context_processors.messages',

                ],

            },

        },

    ]

    ```

    next, add `STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]` to the bottom of the *settings.py* file below the line specifying `STATIC_URL`.

5. from here you can configure your urls if you have an idea of your applications overall structure, you could start programming views if you know what functionality you want, you could create your models, or you could start creating templates. any of those approaches would work here. i tend to think in terms of the data and its routing through a program, so i'll start by configuring the models, then the urls.

    open the *models.py* file inside of the todo_app folder. inspect the following snippet and make your *models.py* file match:

    ```python

    from django.db import models

    class Todo(models.Model):

        title = models.CharField(max_length = 200)

        text = models.TextField(max_length = 500)

        status = models.BooleanField(default = False)

        created_at = models.DateTimeField(auto_now_add = True)

        completed_at = models.DateTimeField(blank = True, null = True)

        task_duration = models.DecimalField(max_digits = 4, decimal_places = 2, blank = True, null = True)

        TODO_TYPE = (

            ('p', 'personal'),

            ('s', 'school'),

            ('w', 'work'),

            ('f', 'family'),

            ('m', 'misc'),

        )

        todo_type = models.CharField(max_length = 1, choices = TODO_TYPE, blank = True, default = 'm')

        def __str__(self):

            return self.title

        class Meta:

            ordering = ['title', 'created_at']

    ```

    once your *models.py* file matches, run `python manage.py makemigrations` and then `pythom manage.py migrate`.

    now you can setup your urls to route the data to the correct endpoints. open your *settings.py* file, compare it with the following snippet, and make your file match the snippet.

    ```python

    from django.contrib import admin

    from django.urls import path, include

    urlpatterns = [

        path('', include('pages.urls')),

        path('todos/', include('todo_app.urls')),

        path('admin/', admin.site.urls),

    ]

    ```

    create a *urls.py* file in both the *pages* and *todo_app* apps. your files should contain the following:

    

    *todo_app/urls.py*

    ```python

    from django.urls import path

    from . import views

    urlpatterns = [

        path('', views.todo_list, name = 'list'),

        path('details/<int:id>', views.details, name = 'details'),

        path('add/', views.add_todo, name = 'add'),

        path('remove/<int:id>', views.remove_todo, name = 'remove'),

        path('mark/<int:id>', views.mark_done, name = 'mark'),

        path('update/<int:id>', views.update, name = 'update'),

    ]

    ```

    *pages/urls.py*

    ```python

    from django.urls import path

    from . import views

    urlpatterns = [

        path('', views.index, name = 'home'),

        path('about/', views.about, name = 'about'),

    ]

    ```

6. with the urls in place, you need to stub out methods in your *views.py* file to silence django's related complaints. add the following code to your *views.py* files in todo_app and pages. 

    *todo_app/views.py*

    ```python

        from django.shortcuts import render, redirect

        from django.http import HttpResponse

        from .models import Todo

        def todo_list(request):

            return HttpResponse('hello from the todo_list view')

        def details(request, id):

            return HttpResponse('hello from the details view')

        def add_todo(request):

            return HttpResponse('hello from the add_todo view')

        def remove_todo(request, id):

            return HttpResponse('hello from the remove view')

        def update_todo(request, id):

            return HttpResponse('hello from the update_todo view')

        def update(request, id):

            return HttpResponse('hello from the update view')

    ```

    *pages/views.py*

    ```python

        from django.shortcuts import render

        from django.http import HttpResponse

        def index(request):

            return HttpResponse('hello from the index/home view')

        def about(request):

            return HttpResponse('hello from the about view')

    ```

    you can now test your urls to ensure they map the request to the correct view.

7. now you can add your templates to the templates directory. you'll need to think about how you want the user to interact with your app to determine what templates you'll need. since it depends on how you want your app laid out, i'll show you a simple setup for a base template called *base.html*, and how you can extend that base template with another template.

    *templates/base.html*

    ```python

        {% load static %}

        <!DOCTYPE html>

        <html lang="en">

        <head>

            <meta charset="UTF-8">

            <meta name="viewport" content="width=device-width, initial-scale=1.0">

            <meta http-equiv="X-UA-Compatible" content="ie=edge">

            <link rel="stylesheet" href="{% static 'css/site.css' %}">

            <title>welcome</title>

        </head>

        <body>

            {% block content %}

            {% endblock %}

            <script src="{% static 'js/main.js' %}"></script>

        </body>

        </html>

    ```

    *templates/pages/index.html*

    ```python

    {% extends 'base.html' %}

    {% block content %}

        <h2>hello from the index template</h2>

    {% endblock %}

    ```

    *templates/todos/list.index.html*

    ```python

    {% extends 'base.html' %}

    {% block content %}

        <h2>hello from the todo list template</h2>

    {% endblock %}

    ```

you're now setup to start working on your view logic, moving data between the templates and the views, and get your users task to display.

your directory structure may look something like this when you're done (note that the . in the listing below represents the directory containing all of your files).

```

    .

    ├── db.sqlite3

    ├── manage.py

    ├── pages

    │   ├── admin.py

    │   ├── apps.py

    │   ├── __init__.py

    │   ├── migrations

    │   │   └── __init__.py

    │   ├── models.py

    │   ├── tests.py

    │   ├── urls.py

    │   └── views.py

    ├── Pipfile

    ├── Pipfile.lock

    ├── static

    │   ├── css

    │   │   └── site.css

    │   └── js

    │       └── main.js

    ├── templates

    │   ├── base.html

    │   ├── pages

    │   │   ├── about.html

    │   │   └── index.html

    │   └── todos

    │       ├── add.html

    │       ├── detail.html

    │       ├── list.html

    │       └── update.html

    ├── todo_app

    │   ├── admin.py

    │   ├── apps.py

    │   ├── __init__.py

    │   ├── migrations

    │   │   ├── 0001_initial.py

    │   │   ├── 0002_auto_20191217_0523.py

    │   │   └── __init__.py

    │   ├── models.py

    │   ├── tests.py

    │   ├── urls.py

    │   └── views.py

    └── todo_project

        ├── asgi.py

        ├── __init__.py

        ├── settings.py

        ├── urls.py

        └── wsgi.py

```


Message #class-狸
