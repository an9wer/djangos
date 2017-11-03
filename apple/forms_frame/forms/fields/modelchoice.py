from django import forms
from forms_frame.models import CharModel

class ModelChoiceForm(forms.Form):
    field = forms.ModelChoiceField(queryset=CharModel.objects.all(),
                                   to_field_name="field",
                                   empty_label=None)


"""
1.  empty_label:

By default the <select> widget used by ModelChoiceField will have an empty 
choice at the top of the list. You can change the text of this label 
(which is "---------" by default) with the empty_label attribute, or you can 
disable the empty label entirely by setting empty_label to None:

    # A custom empty label
    field1 = forms.ModelChoiceField(queryset=..., empty_label="(Nothing)")

    # No empty label
    field2 = forms.ModelChoiceField(queryset=..., empty_label=None)

Note that if a ModelChoiceField is required and has a default initial value, 
no empty choice is created (regardless of the value of empty_label).


2.  to_field_name:

This optional argument is used to specify the field to use as the value of the 
choices in the field’s widget. Be sure it’s a unique field for the model, 
otherwise the selected value could match more than one object. By default it is 
set to None, in which case the primary key of each object will be used. For example:

    # No custom to_field_name
    field1 = forms.ModelChoiceField(queryset=...)

would yield:

    <select id="id_field1" name="field1">
    <option value="obj1.pk">Object1</option>
    <option value="obj2.pk">Object2</option>
    ...
    </select>
    and:

    # to_field_name provided
    field2 = forms.ModelChoiceField(queryset=..., to_field_name="name")

would yield:

    <select id="id_field2" name="field2">
    <option value="obj1.name">Object1</option>
    <option value="obj2.name">Object2</option>
    ...
    </select>


在页面上 <select> 中的 <option> 中的值使用的是 model.__str__（在 python2 中是
model.__unicode__）的返回值，我们可以对其进行修改，改变 <option> 中展示的值。

或者也可以定义 field 的子类，修改 field 中的 label_from_instance 方法。

The __str__ (__unicode__ on Python 2) method of the model will be called to 
generate string representations of the objects for use in the field’s choices; 
to provide customized representations, subclass ModelChoiceField and override 
label_from_instance. This method will receive a model object, and should return 
a string suitable for representing it. For example:

    from django.forms import ModelChoiceField

    class MyModelChoiceField(ModelChoiceField):
        def label_from_instance(self, obj):
                return "My Object #%i" % obj.id

"""
