from django import forms


class NameMultivaleWidget(forms.MultiWidget):

    def __init__(self, attrs=None):

        widgets = (
            forms.TextInput,
            forms.TextInput,
        )
        super(NameMultivaleWidget, self).__init__(widgets, attrs)

    # decompress 会在 MultiWidget.get_context() 被调用，然后 render 到页面上
    def decompress(self, value):
        if value:
            return value
        return [None, None]


class NameMultivalueField(forms.MultiValueField):
    widget = NameMultivaleWidget()  # default widget

    def __init__(self, *args, **kwargs):

        fields = (
            forms.CharField(),  # first name
            forms.CharField(),  # last name
        )
        super(NameMultivalueField, self).__init__(fields=fields, *args, **kwargs)

    # compress 在 MultiValueField.clean() 中被调用，主要将 form 提交的 
    # value 拼起来，然后进行整体校验
    def compress(self, data_list):
        return " ".join(data_list)


class NameMultiValueForm(forms.Form):
    field = NameMultivalueField()


"""
MultiValueField is abstract and must be subclassed. In contrast with the
single value fields, subclasses of MultiValueField must not implement clean()
but instead - implement compress().

### fields

A tuple of fields whose values are cleaned and subsequently combined into a
single value. Each value of the field is cleaned by the corresponding field
in fields – the first value is cleaned by the first field, the second value
is cleaned by the second field, etc. Once all fields are cleaned, the list
of clean values is combined into a single value by compress().

### require_all_fields

Defaults to True, in which case a required validation error will be raised if
no value is supplied for any field.

When set to False, the Field.required attribute can be set to False for
individual fields to make them optional. If no value is supplied for a
required field, an incomplete validation error will be raised.

A default incomplete error message can be defined on the MultiValueField
subclass, or different messages can be defined on each individual field.

### widget

Must be a subclass of django.forms.MultiWidget. Default value is TextInput,
which probably is not very useful in this case.

### compress(data_list)

Takes a list of valid values and returns a “compressed” version of those
values – in a single value. For example, SplitDateTimeField is a subclass
which combines a time field and a date field into a datetime object.

"""
