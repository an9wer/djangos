from django import forms

class NameForm(forms.Form):
    name = forms.CharField(label='your name', max_length=5)
