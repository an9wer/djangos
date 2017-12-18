from .attrs import AttrsForm


"""
### Specifying widgets

Whenever you specify a field on a form, Django will use a default widget that
is appropriate to the type of data that is to be displayed.

However, if you want to use a different widget for a field, you can just use
the widget argument on the field definition.

    from django import forms

    class CommentForm(forms.Form):
        name = forms.CharField()
        url = forms.URLField()
        comment = forms.CharField(widget=forms.Textarea)   # 注意：这里没加括号

This would specify a form with a comment that uses a larger Textarea widget,
rather than the default TextInput widget.

"""


"""
### Customizing widget instances

When Django renders a widget as HTML, it only renders very minimal markup -
Django doesn’t add class names, or any other widget-specific attributes.
This means, for example, that all TextInput widgets will appear the same on
your Web pages.

There are two ways to customize widgets: per widget instance and per widget
class.


#### Sytling widget instances

If you want to make one widget instance look different from another, you will
need to specify additional attributes at the time when the widget object is
instantiated and assigned to a form field (and perhaps add some rules to
your CSS files).

You might want a larger input element for the comment, and you might want the
‘name’ widget to have some special CSS class. It is also possible to specify
the ‘type’ attribute to take advantage of the new HTML5 input types. To do
this, you use the Widget.attrs argument when creating the widget:

    class CommentForm(forms.Form):
        name = forms.CharField(widget=forms.TextInput(attrs={'class': 'special'}))
        comment = forms.CharField(widget=forms.TextInput(attrs={'size': '40'}))
        email = forms.CharField(widget=forms.EmailInput(attrs={'required': True}))

详见 apple/apple/forms_frame/widgets/attrs.py


#### Styling widget classes

With widgets, it is possible to add assets (css and javascript) and more deeply
customize their appearance and behavior.

In a nutshell, you will need to subclass the widget and either define a `Media`
inner class or create a `media` property.

详见 form assets

"""
