from django import forms

class FileForm(forms.Form):
    field = forms.FileField()

class MultipleFileForm(forms.Form):
    field = forms.FileField(widget=forms.ClearableFileInput(attrs={"multiple": True}))

class ClearFileForm(forms.Form):
    field = forms.FileField(required=False, widget=forms.ClearableFileInput)


"""
两点：

1.  需要在 form 标签中加上 enctype="multipart/form-data" 属性
2.  在 bind data 时，需要将 file data 作为参数传给 Form object

Firstly, in order to upload files, you’ll need to make sure that your <form> 
element correctly defines the enctype as "multipart/form-data":

    <form enctype="multipart/form-data" method="post" action="/foo/">

Secondly, when you use the form, you need to bind the file data. File data is 
handled separately to normal form data, so when your form contains a FileField 
and ImageField, you will need to specify a second argument when you bind your 
form. So if we extend our ContactForm to include an ImageField called mugshot, 
we need to bind the file data containing the mugshot image:

    # Bound form with an image field
    >>> from django.core.files.uploadedfile import SimpleUploadedFile
    >>> data = {'subject': 'hello',
            ...         'message': 'Hi there',
            ...         'sender': 'foo@example.com',
            ...         'cc_myself': True}
    >>> file_data = {'mugshot': SimpleUploadedFile('face.jpg', <file data>)}
    >>> f = ContactFormWithMugshot(data, file_data)

In practice, you will usually specify request.FILES as the source of file data 
(just like you use request.POST as the source of form data):

        # Bound form with an image field, data from the request
        >>> f = ContactFormWithMugshot(request.POST, request.FILES)

"""
