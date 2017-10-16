from django import forms
from models import Age

class NameForm(forms.Form):
    name = forms.CharField(label='your name', max_length=5)

class AgeForm(forms.ModelForm):
    class Meta:
        model = Age
        fields = ['age']

