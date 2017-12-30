from .multiplechoice import MultipleChoiceForm
from .file import FileForm, MultipleFileForm, ClearFileForm
from .modelchoice import ModelChoiceForm
from .modelmultiplechoice import ModelMultipleChoiceForm
from .multivalue import NameMultiValueForm, NameMultivaleWidget

"""
Although the primary way you’ll use Field classes is in Form classes, you can
also instantiate them and use them directly to get a better idea of how they
work. Each Field instance has a clean() method, which takes a single argument
and either raises a django.forms.ValidationError exception or returns the
clean value:

    >>> from django import forms
    >>> f = forms.EmailField()
    >>> f.clean('foo@example.com')
    'foo@example.com'
    >>> f.clean('invalid email address')
    Traceback (most recent call last):
    ...
    ValidationError: ['Enter a valid email address.']

"""


"""
### Core field arguments

Each Field class constructor takes at least these arguments. Some Field
classes take additional, field-specific arguments, but the following should
always be accepted:

-   required: 

    Boolean that specifies whether the field is required. True by default.

-   widget:

    A Widget class, or instance of a Widget class, that should be used for
    this Field when displaying it. Each Field has a default Widget that it'll
    use if you don't specify this. In most cases, the default widget is 
    TextInput.

-   label:

    A verbose name for this field, for use in displaying this field in a form.
    By default, Django will use a "pretty" version of the form field name, if
    the Field is part of a Form.

-   initial:

    A value to use in this Field's initial display. This value is *not* used
    as a fallback if data isn't given.
    
-   help_text:

    An optional string to use as "help text" for this Field.
    

#### error_messages:

An optional dictionary to override the default messages that the field
will raise.

    不使用 error_message 参数：

    >>> from django import forms
    >>> generic = forms.CharField()
    >>> generic.clean('')
    Traceback (most recent call last):
      ...
    ValidationError: ['This field is required.']

    使用 error_message 参数：

    >>> name = forms.CharField(error_messages={'required': 'Please enter your name'})
    >>> name.clean('')
    Traceback (most recent call last):
      ...
    ValidationError: ['Please enter your name']


#### show_hidden_initial:

Boolean that specifies if it is needed to render a hidden widget with initial
value after widget.


#### validators

List of additional validators to use


#### localize

Boolean that specifies if the field should be localized.


#### disabled

Boolean that specifies whether the field is disabled, that is its widget is
shown in the form but not editable.
    

#### label_suffix:

Suffix to be added to the label. Overrides form's label_suffix.

"""
