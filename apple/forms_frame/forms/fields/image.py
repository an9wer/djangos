from django import forms


class ImageForm(forms.Form):
    field = forms.ImageField()


"""
Using an ImageField requires that Pillow is installed with support for the image
formats you use. If you encounter a corrupt image error when you upload an image,
it usually means that Pillow doesn’t understand its format. To fix this, install
the appropriate library and reinstall Pillow.

When you use an ImageField on a form, you must also remember to bind the file
data to the form (详见 ./file.py 中的相关内容).

After the field has been cleaned and validated, the UploadedFile object will
have an additional image attribute containing the Pillow Image instance used
to check if the file was a valid image. Also, UploadedFile.content_type will
be updated with the image’s content type if Pillow can determine it, otherwise
it will be set to None.
"""
