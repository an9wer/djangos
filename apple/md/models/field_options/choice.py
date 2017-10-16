# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Choice(models.Model):
    SHIRT_SIZES = (
        # the first element is the value that will be stored in database.
        # the second element will be displayed by the default form widget
        # or in a ModelChoiceField.
        ("S", "Small"),
        ("M", "Medium"),
        ("L", "Large"),
    )
    name = models.CharField(max_length=60)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)

if __name__ == "__main__":
    """
    using get_FOO_display() method can display the second element value 
    in choice.
    """
    c = Choice(name="an9wer", shirt_size="L")
    c.save()
    c.shirt_size                # return value "L"
    c.get_shirt_size_display()  # return value "Large"
