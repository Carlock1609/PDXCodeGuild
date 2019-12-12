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

