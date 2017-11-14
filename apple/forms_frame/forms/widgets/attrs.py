from django import forms


class AttrsForm(forms.Form):
    size_field = forms.CharField(widget=forms.TextInput(attrs={"size": 100}))
    id_field = forms.CharField(widget=forms.TextInput(attrs={"id": "something"}))
    none_field = forms.CharField(required=False, widget=forms.TextInput(attrs={"style": "display:none"}))


"""
在 html 中：

    {{ form.size_field }}

    将转化成：

    <input type="text" name="size_field" size="100" required id="id_size_field" />

在 html 中：

    {{ form.id_field }}

    将转化成：

    <input type="text" name="id_field" id="something" required />

在 html 中：

    {{ form.none_field }}

    将转化成：

    <input type="text" name="none_field" style="display:none" id="id_none_field" />

"""
