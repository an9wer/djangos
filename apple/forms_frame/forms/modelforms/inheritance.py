from django import forms

from forms_frame.models import OTTModel


class InheritanceFatherForm(forms.ModelForm):

    class Meta:
        model = OTTModel
        fields = ["one", "two"]


class EnhancedInheritanceSonForm(InheritanceFatherForm):

    def some_func(self):
        pass


class RestrictedInheritanceSonForm(InheritanceFatherForm):

    class Meta(InheritanceFatherForm.Meta):
        exclude = ["one"]


class ExpandedInheritanceSonForm(InheritanceFatherForm):

    class Meta(InheritanceFatherForm.Meta):
        fields = "__all__"
        # or use:
        # fields = InheritanceFatherForm.Meta.fields + ["three"]


"""
Note:

-   Normal Python name resolution rules apply. If you have multiple base classes
    that declare a Meta inner class, only the first one will be used. This means
    the child’s Meta, if it exists, otherwise the Meta of the first parent, etc.

-   It’s possible to inherit from both Form and ModelForm simultaneously, however,
    you must ensure that ModelForm appears first in the MRO. This is because these
    classes rely on different metaclasses and a class can only have one metaclass.

-   It’s possible to declaratively remove a Field inherited from a parent class
    by setting the name to be None on the subclass.

"""
