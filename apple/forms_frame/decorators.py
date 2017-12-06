from .forms import *

url_form = {
    "/forms_frame/modelforms/partfields/": PartFieldsForm,
    "/forms_frame/modelforms/allfields/": AllFieldsForm,
    "/forms_frame/modelforms/excludefields/": ExcludeFieldsForm,
    "/forms_frame/modelforms/overridefields/": OverrideFieldsFrom,
}


def get_form_cls(func):
    def wrapper(request, *args, **kwargs):
        request.form = url_form[request.path]
        return func(request, *args, **kwargs)
    return wrapper

