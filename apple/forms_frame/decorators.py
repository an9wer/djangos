from .forms import *

form_and_html = {
    "/forms_frame/fields/multivalue/": (NameMultiValueForm, "common_form.html"),
    "/forms_frame/fields/dynamic/": (DynamicForm, "common_form.html"),
    "/forms_frame/fields/image/": (ImageForm, "multipart_form.html"),

    "/forms_frame/modelforms/partfields/": (PartFieldsForm, "common_form.html"),
    "/forms_frame/modelforms/allfields/": (AllFieldsForm, "common_form.html"),
    "/forms_frame/modelforms/excludefields/": (ExcludeFieldsForm, "common_form.html"),
    "/forms_frame/modelforms/overridefields/": (OverrideFieldsFrom, "common_form.html"),
    "/forms_frame/modelforms/restricted-inheritanceson/": (RestrictedInheritanceSonForm, "common_form.html"),
    "/forms_frame/modelforms/expanded-inheritanceson/": (ExpandedInheritanceSonForm, "common_form.html"),
}


def get_form_and_html(func):
    def wrapper(request, *args, **kwargs):
        request.form, request.html = form_and_html[request.path]
        return func(request, *args, **kwargs)
    return wrapper
