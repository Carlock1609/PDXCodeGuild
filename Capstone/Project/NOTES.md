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

