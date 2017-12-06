from django import forms

from ..models import OTTModel


class InheritanceFatherForm(forms.ModelForm):
    pass

    class Meta:
        include = ()


class InheritanceSonForm(forms.ModelForm):
    pass
