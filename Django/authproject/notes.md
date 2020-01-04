The format of our link is the same for other 3rd party auths. In other words, we’d basically swap out github for facebook to have the same effect. Check the django-allauth docs for any additional configuration you’d need but the overall approach is the same.

Finally update our urls.py to point to the new homepage.