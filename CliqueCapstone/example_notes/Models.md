CharField - small amount of text
TextField - large amount of text

<!-- This is how you add to a model -->
<!-- You must fill out each attribute before saving, Question has question_text and pub_date, fill both those out and you can add -->
question = Question()
question.question_text = "New question"
question.pub_date = datetime.datetime.now()
question.save()

<!-- gets specific data -->
Question.objects.all()[0].question_text

<!-- This returns actual text instead of object -->
def __str__(self):
    return self.question_text



from django.db import models

<!-- Defining model -->
class User(models.Model):
    <!-- Attributes below -->
    name = models.CharField(max_length=128)
    email = models.CharField(max_length=128)

python3 manage.py shell 
>>> from usermodel.models import USEr
^^ This will fail in a regular python shell
using manage.py sets django libraries around it

<!-- CONSTRUCTOR CALL -->
u = User(name='Kristen', email='kf@umich.edu)
u.save()
print(u.id)
print(u.email)


<!-- FIGURE out how to store images on another server, and keep app seperate -->
<!-- That’s what django.contrib.staticfiles is for: it collects static files from each of your applications (and any other places you specify) into a single location that can easily be served in production. -->