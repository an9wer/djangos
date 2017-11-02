from django import forms

class InitialForm(forms.Form):
    field = forms.CharField()
    field_init = forms.CharField(initial="initial field")


"""
如果 field 定义了 initial，在 form 中又对该 field 定义了 initial，则 form 中
定义的 initial 会覆盖 field 中定义的 initial。

If a Field defines initial and you include initial when instantiating the Form,
then the latter initial will have precedence. In this example, initial is 
provided both at the field level and at the form instance level, and the 
latter gets precedence:

    >>> from django import forms
    >>> class CommentForm(forms.Form):
        ...     name = forms.CharField(initial='class')
        ...     url = forms.URLField()
        ...     comment = forms.CharField()
        >>> f = CommentForm(initial={'name': 'instance'}, auto_id=False)
        >>> print(f)
        <tr><th>Name:</th><td><input type="text" name="name" value="instance" required /></td></tr>
        <tr><th>Url:</th><td><input type="url" name="url" required /></td></tr>
        <tr><th>Comment:</th><td><input type="text" name="comment" required /></td></tr>
"""
