
Three-step guide making model changes
    -Change your models (in models.py).
    -Run python manage.py makemigrations to create migrations for those changes
    -Run python manage.py migrate to apply those changes to -the database.

# Goes into python shell
    python manage.py shell
    
    We’re using this instead of simply typing “python”, because manage.py sets the DJANGO_SETTINGS_MODULE environment variable, which gives Django the Python import path to your mysite/settings.py file.

*****
# How to explore API in shell
from polls.models import Choice, Question  # Import the model classes we just wrote.

#No questions are in the system yet.
>>> Question.objects.all()

# Create a new Question.
# Support for time zones is enabled in the default settings file, so
# Django expects a datetime with tzinfo for pub_date. Use timezone.now()
# instead of datetime.datetime.now() and it will do the right thing.
>>> from django.utils import timezone
>>> q = Question(question_text="What's new?", pub_date=timezone.now())

 Save the object into the database. You have to call save() explicitly.
>>> q.save()

# Now it has an ID.
>>> q.id

 Save the object into the database. You have to call save() explicitly.
>>> q.save()

# Now it has an ID.
>>> q.id
******

ADD __str__() methods to your models!



# Give the Question a couple of Choices. The create call constructs a new
# Choice object, does the INSERT statement, adds the choice to the set
# of available choices and returns the new Choice object. Django creates
# a set to hold the "other side" of a ForeignKey relation
# (e.g. a question's choice) which can be accessed via the API.

# The API automatically follows relationships as far as you need.
# Use double underscores to separate relationships.
# This works as many levels deep as you want; there's no limit.
# Find all Choices for any question whose pub_date is in this year
# (reusing the 'current_year' variable we created above).

# Let's delete one of the choices. Use delete() for that.
>>> c = q.choice_set.filter(choice_text__startswith='Just hacking')
>>> c.delete()


Make the poll app modifiable in the admin¶

But where’s our poll app? It’s not displayed on the admin index page.

Only one more thing to do: we need to tell the admin that Question objects have an admin interface. To do this, open the polls/admin.py file, and edit it to look like this:


Overview¶

A view is a “type” of Web page in your Django application that generally serves a specific function and has a specific template. For example, in a blog application, you might have the following views:

    Blog homepage – displays the latest few entries.
    Entry “detail” page – permalink page for a single entry.
    Year-based archive page – displays all months with entries in the given year.
    Month-based archive page – displays all days with entries in the given month.
    Day-based archive page – displays all entries in the given day.
    Comment action – handles posting comments to a given entry.

In our poll application, we’ll have the following four views:

    Question “index” page – displays the latest few questions.
    Question “detail” page – displays a question text, with no results but with a form to vote.
    Question “results” page – displays results for a particular question.
    Vote action – handles voting for a particular choice in a particular question.




Template namespacing

Now we might be able to get away with putting our templates directly in polls/templates (rather than creating another polls subdirectory), but it would actually be a bad idea. Django will choose the first template it finds whose name matches, and if you had a template with the same name in a different application, Django would be unable to distinguish between them. We need to be able to point Django at the right one, and the best way to ensure this is by namespacing them. That is, by putting those templates inside another directory named for the application itself.


Note that once we’ve done this in all these views, we no longer need to import loader and HttpResponse (you’ll want to keep HttpResponse if you still have the stub methods for detail, results, and vote).

The render() function takes the request object as its first argument, a template name as its second argument and a dictionary as its optional third argument. It returns an HttpResponse object of the given template rendered with the given context.