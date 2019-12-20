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
