from django import forms


class DynamicForm(forms.Form):
    field = forms.CharField()

    def __init__(self, *args, **kwargs):
        super(DynamicForm, self).__init__(*args, **kwargs)
        self.fields["dynamic_field"] = forms.BooleanField()

