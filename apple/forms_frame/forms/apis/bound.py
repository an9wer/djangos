from django import forms

class BoundForm(forms.Form):
    field_unbound = forms.CharField()
    field_bound = forms.CharField()


"""
bound form 会在 validate 之后 render
unbound form 会直接 render

-   If it’s bound to a set of data, it’s capable of validating that data and 
    rendering the form as HTML with the data displayed in the HTML.
-   If it’s unbound, it cannot do validation (because there’s no data to 
    validate!), but it can still render the blank form as HTML.
"""
