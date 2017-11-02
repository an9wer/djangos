from django import forms

from forms_frame.models import Father, Son

class FatherForm(forms.ModelForm):

    class Meta:
        model = Father
        fields = ["name"]


class SonForm(forms.ModelForm):
    book = forms.FileField(required=False, widget=forms.ClearableFileInput)
    book = forms.FileField(required=False, widget=forms.ClearableFileInput(attrs={"multiple": True}))
    #book = forms.FileField(widget=forms.ClearableFileInput(attrs={"multiple": True}))

    class Meta:
        model = Son
        #fields = ["name", "father__name"]
        fields = "__all__"

