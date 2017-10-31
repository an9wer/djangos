from django import forms

class MultipleChoiceForm(forms.Form):
    field = forms.MultipleChoiceField()

