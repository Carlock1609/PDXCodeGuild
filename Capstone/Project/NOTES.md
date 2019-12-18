**IDEAS:**
- Should I make seperate apps for each function? 
    - Profile app
    - Users app
    - Messages app
    - Search app
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