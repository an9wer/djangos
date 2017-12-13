from django import forms

from forms_frame.models import OTTModel


# --------------------- Selecting the fields to used ------------------------ #


class PartFieldsForm(forms.ModelForm):
    class Meta:
        model = OTTModel
        fields = ["one", "three"]


class AllFieldsForm(forms.ModelForm):
    """
    Set the fields attribute to the special value '__all__' to indicate
    that all fields in the model should be used.
    """
    class Meta:
        model = OTTModel
        fields = "__all__"


class ExcludeFieldsForm(forms.ModelForm):
    """
    Set the exclude attribute of the ModelForm’s inner Meta class to a list
    of fields to be excluded from the form.
    """
    class Meta:
        model = OTTModel
        exclude = ["one", "three"]


"""
In addition, Django applies the following rule: if you set editable=False on
the model field, any form created from the model via ModelForm will not include
that field.

"""


# --------------------- Overriding the default fields ----------------------- #


class OverrideFieldsFrom(forms.ModelForm):
    class Meta:
        model = OTTModel
        fields = ["one", "two", "three"]

        # customize field widgets
        # The widgets dictionary accepts either widget instances
        # (e.g., Textarea(...)) or classes (e.g., Textarea).
        widgets = {
            "one": forms.Textarea(attrs={"cols": 80, "row": 20}),
        }
        # customize field labels
        labels = {
            "two": 2,
        }
        # customize field help texts
        help_texts = {
            "three": "this is three",
        }
        # customize field error messages
        error_messages = {
        }
        # customize field type
        field_classes = {
            "two": forms.EmailField,
            "three": forms.FileField,
        }


"""
You can specify the `widgets`, `labels`, `help_texts`, `error_messages` and
`field_classes` attributes of the inner Meta class if you want to further
customize a field.

if you want complete control over of a field – including its type, validators,
required, etc. – you can do this by declaratively specifying fields like you
would in a regular Form:

    from django.forms import ModelForm, CharField
    from myapp.models import Article

    class ArticleForm(ModelForm):
        slug = CharField(validators=[validate_slug])

        class Meta:
            model = Article
            fields = ['pub_date', 'headline', 'content', 'reporter', 'slug']

"""
