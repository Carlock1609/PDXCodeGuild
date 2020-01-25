from django import forms
from .models import UserMessages

class SendUserMessageForm(forms.ModelForm):

    class Meta:
        model = UserMessages
        fields = [
            'sender',
            'receiver',
            'conversation_name',
            'subject',
            'body',
            'user_inbox',
        ]
    