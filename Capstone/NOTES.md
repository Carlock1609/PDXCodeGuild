**STRUCTURE**
DONT EDIT FILES OR EDIT NAMES - SHIT STORM

My_capstone - container
    my_project
    my_app1
    my_app2
    manage.py
    static
    templates
    pipfile

**IDEAS:**
- Should I make seperate apps for each function? 
    - Profile app
        - used for users visiting other users pages
        - for unauthenticated users
    - Users app
        - login
        - logout
        - register
        - profile page for authenticated users
    - Messages app
        - direct messaging
        - community board
    - Pages app
        - search page
        - about
- For django's default User_Auth -- Should I make a custome Auth to incorp unique social media accounts?

**RANDOM NOTES:**


**USER AUTH**
<!-- THIS IS HOW YOU REMOVE LOGIN/REGISTER IF LOGGED IN ON NAV -->
{% if user.is_authenticated %}
    <a class="nav-item nav-link" href="{% url 'logout' %}">Logout</a>
{% else %}
    <a class="nav-item nav-link" href="{% url 'login' %}">Login</a>
    <a class="nav-item nav-link" href="{% url 'register' %}">Register</a>
{% endif %}

COREY SCHAFER EPISODE 8 GOES OVER ONE TO ONE WITH USERS AND THEIR PROFILES



**USER PHOTOS** 


# MUST INSTALL PILLOW for photos

# THIS IMPORTS BUILTIN USER MODEL
from django.contrib.auth.models import User

  # The param gives it a one to one relationship, models.CASCADE means if user is deleted, then everything is gone.
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # user profile pic
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

# WHEN YOU MAKE MODELS YOU MUST REGISTER THEM IF YOU WANT TO SEE THEM ON /ADMIN



from django.contrib.auth.models import User - imports Model
user = User.objects.filter(username='carlock906').first()
user.profile - returns Profile object
user.profile.image - returns ImageFieldFile
user.profile.image.url - returns location

    <!-- THIS IS HOW YOU IMPORT PHOTO -->
        <img class="rounded-circle account-img" src="{{ user.profile.image.url }}">

        
settings.py
This is where we are trying to store our media pictures from profile model
Now whenever you create a profile and add picture, it goes to media/profile_pics/pic.jpg
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

THEN TO MAKE IT SO WHEN USER CREATES LOGIN THEY AUTO GET PROFILE
create signals.py in users app
