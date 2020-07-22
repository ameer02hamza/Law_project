from django import forms
from . models import ChatBox


class ChatBoxForm(forms.ModelForm):

    message = forms.CharField(label="", widget=forms.TextInput(attrs={"placeholder":"Type Message here...",
                                                                      "class": "form-control", 'name': 'message'}))

    class Meta:
        model = ChatBox
        fields = [
            'message'
        ]
