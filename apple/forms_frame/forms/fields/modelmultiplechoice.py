from django import forms
from forms_frame.models import CharModel

class ModelMultipleChoiceForm(forms.Form):
    field = forms.ModelMultipleChoiceField(queryset=CharModel.objects.all(),
                                           to_field_name="field")


"""
与 ModelChoiceField 不同，ModelMultipleChoiceField 没有 empty_label 参数。

"""
