from django import forms
from .models import Question


class QuesForm(forms.ModelForm):
    title = forms.CharField(label="", widget=forms.TextInput(attrs={"placeholder": "Question Title",
                                                                    "class": "form-control"}))
    question = forms.CharField(label="", widget=forms.Textarea(attrs={"placeholder":" Your question here.....",
                                                                      "class":"form-control"}))

    class Meta:
        model = Question
        fields = [
            'title',
            'question',
        ]