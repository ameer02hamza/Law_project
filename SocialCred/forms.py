from django import forms
from SocialCred.models import UserInfo
class Imageform(forms.ModelForm):

    class Meta:UserInfo
    fields = ['profile_picture']
