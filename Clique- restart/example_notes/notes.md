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




**STARTING POSTMAN MESSENGER TEST**


<!-- 
class PostDetailView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post -->



**THIS IS USER POST AND SECURITY EXAMPLES**
**ALSO LIST AND CLASS BASED VIEWS**

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView): # This template only has two fields for the form.
model = Post  
fields = ['title', 'content']

 This sets the post form to have the current logged in user. OVERRIDE
def form_valid(self, form):
    form.instance.author = self.request.user
    return super().form_valid(form)

def test_func(self):
    post = self.get_object()
    # Checking to see if person making post is author logged in
    if self.request.user == post.author:
        return True
    return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
model = Post

def test_func(self):
    post = self.get_object()
    # Checking to see if person making post is author logged in
    if self.request.user == post.author:
        return True
    return False -->

 {% if object.author == user  %}
        <div>
            <a class="btn btn-secondary btn-sm mt-1 mb-1" href="{% url 'post-update' object.id %}">Update</a>
            <a class="btn btn-danger btn-sm mt-1 mb-1" href="{% url 'post-delete' object.id %}">Delete</a>
        </div>
    {% endif %}
</div>
<h2 class="article-title">{{ object.title }}</h2>
<p class="article-content">{{ object.content }}</p>
</div> -->


**JSON FAKE DATA**
>>> import json
>>> from blog.models import Post

 with open('posts.json') as f:
...     posts_json = json.load(f)

>>> for post in posts_json:
...     post = Post(title=post['title'], content =post['content'], author_id=post['user_id'])
...     post.save()
...
>>> exit()

**PAGINATION SHELL CODES**
>>> from django.core.paginator import Paginator
>>> posts = ['1', '2', '3', '4', '5']
>>> p = Paginator(posts, 2)
>>> p.num_pages
3
>>> for page in p.page_range:
...     print(page)
...
1
2
3
>>> p1 = p.page(1)
>>>
>>> p1
<Page 1 of 3>
>>> p1.number
1
>>> p1.object_list
['1', '2']
>>> p1.has_previous()
False
>>> p1.has_next()
True
>>> p1.next_page_number()
2
>>>

**PAGINATION TEMPLATE EXAMPLES**

{% if is_paginated %}
  {% if page_obj.has_previous %}
      <a class="btn btn-outline-info mb-4" href="?page=1">First</a>
      <a class="btn btn-outline-info mb-4" href="?page={{ page_obj.previous_page_number }}">Previous</a>
  {% endif %}

  {% for num in page_obj.paginator.page_range %}
      {% if page_obj.number == num %}
          <a class="btn btn-info mb-4" href="?page={{ num }}">{{ num }}</a>
      {% elif num > page_obj.number|add:'-3' and num < page_obj.number|add:'3' %}
          <a class="btn btn-outline-info mb-4" href="?page={{ num }}">{{ num }}</a>  
      {% endif %}
  {% endfor %}

  {% if page_obj.has_next %}
      <a class="btn btn-outline-info mb-4" href="?page={{ page_obj.next_page_number }}">Next</a>
      <a class="btn btn-outline-info mb-4" href="?page={{ page_obj.paginator.num_pages }}">Last</a>
  {% endif %}

{% endif %}