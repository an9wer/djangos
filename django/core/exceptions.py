"""
Global Django exception and warning classes.
"""
from django.utils import six
from django.utils.encoding import force_text


class FieldDoesNotExist(Exception):
    """The requested model field does not exist"""
    pass


class DjangoRuntimeWarning(RuntimeWarning):
    pass


class AppRegistryNotReady(Exception):
    """The django.apps registry is not populated yet"""
    pass


class ObjectDoesNotExist(Exception):
    """The requested object does not exist"""
    silent_variable_failure = True


class MultipleObjectsReturned(Exception):
    """The query returned multiple objects when only one was expected."""
    pass


class SuspiciousOperation(Exception):
    """The user did something suspicious"""


class SuspiciousMultipartForm(SuspiciousOperation):
    """Suspect MIME request in multipart form data"""
    pass


class SuspiciousFileOperation(SuspiciousOperation):
    """A Suspicious filesystem operation was attempted"""
    pass


class DisallowedHost(SuspiciousOperation):
    """HTTP_HOST header contains invalid value"""
    pass


class DisallowedRedirect(SuspiciousOperation):
    """Redirect to scheme not in allowed list"""
    pass


class TooManyFieldsSent(SuspiciousOperation):
    """
    The number of fields in a GET or POST request exceeded
    settings.DATA_UPLOAD_MAX_NUMBER_FIELDS.
    """
    pass


class RequestDataTooBig(SuspiciousOperation):
    """
    The size of the request (excluding any file uploads) exceeded
    settings.DATA_UPLOAD_MAX_MEMORY_SIZE.
    """
    pass


class PermissionDenied(Exception):
    """The user did not have permission to do that"""
    pass


class ViewDoesNotExist(Exception):
    """The requested view does not exist"""
    pass


class MiddlewareNotUsed(Exception):
    """This middleware is not used in this server configuration"""
    pass


class ImproperlyConfigured(Exception):
    """Django is somehow improperly configured"""
    pass


class FieldError(Exception):
    """Some kind of problem with a model field."""
    pass


NON_FIELD_ERRORS = '__all__'


class ValidationError(Exception):
    """An error while validating data."""
    def __init__(self, message, code=None, params=None):
        """
        The `message` argument can be a single error, a list of errors, or a
        dictionary that maps field names to lists of errors. What we define as
        an "error" can be either a simple string or an instance of
        ValidationError with its message attribute set, and what we define as
        list or dictionary can be an actual `list` or `dict` or an instance
        of ValidationError with its `error_list` or `error_dict` attribute set.
        """
        ## 参数 message 可以是 ValidationError instance, list object, dict 
        ## object which maps field names to list of errors（也就是说 message
        ## 如果是 dict 对象，其 value 是一个 list），可以通过 ValidationError
        ## 的 error_dict 或者 error_list 属性分别得到 actual dict or list

        # PY2 can't pickle naive exception: http://bugs.python.org/issue1692335.
        super(ValidationError, self).__init__(message, code, params)

        ## message 如果是 ValidationError 的实例对象，则获取其 error_dict 属性
        ## 的值，如果其没有 error_dict 属性，则获取其 error_list 属性的值，如果
        ## 其没有 error_list 属性，则获取其 message 属性的值
        if isinstance(message, ValidationError):
            if hasattr(message, 'error_dict'):
                message = message.error_dict
            # PY2 has a `message` property which is always there so we can't
            # duck-type on it. It was introduced in Python 2.5 and already
            # deprecated in Python 2.6.
            elif not hasattr(message, 'message' if six.PY3 else 'code'):
                message = message.error_list
            else:
                message, code, params = message.message, message.code, message.params

        ## message 如果是 dict 对象，将其 item 逐个存入 self.error_dict 中，
        ## self.error_dict 的 key 是对应 message 的 key，value 是 message 的
        ## value 转化成 ValidationError 实例对象后的 error_list 属性的值
        if isinstance(message, dict):
            self.error_dict = {}
            for field, messages in message.items():
                if not isinstance(messages, ValidationError):
                    messages = ValidationError(messages)
                self.error_dict[field] = messages.error_list

        ## message 如果是 list 对象，将其 item 的逐个转化成 ValidationError 的
        ## 实例对象后添加到 self.error_list 中
        elif isinstance(message, list):
            self.error_list = []
            for message in message:
                # Normalize plain strings to instances of ValidationError.
                if not isinstance(message, ValidationError):
                    message = ValidationError(message)
                if hasattr(message, 'error_dict'):
                    ## TODO: 这里的 sum 的作用？
                    self.error_list.extend(sum(message.error_dict.values(), []))
                else:
                    self.error_list.extend(message.error_list)

        ## message 如果是 str 对象，注意：一定会有 error_list 属性，且是其自己
        else:
            self.message = message
            self.code = code
            self.params = params
            self.error_list = [self]

    @property
    def message_dict(self):
        # Trigger an AttributeError if this ValidationError
        # doesn't have an error_dict.
        getattr(self, 'error_dict')

        return dict(self)

    @property
    def messages(self):
        if hasattr(self, 'error_dict'):
            return sum(dict(self).values(), [])
        return list(self)

    def update_error_dict(self, error_dict):
        if hasattr(self, 'error_dict'):
            for field, error_list in self.error_dict.items():
                error_dict.setdefault(field, []).extend(error_list)
        else:
            error_dict.setdefault(NON_FIELD_ERRORS, []).extend(self.error_list)
        return error_dict

    def __iter__(self):
        if hasattr(self, 'error_dict'):
            for field, errors in self.error_dict.items():
                yield field, list(ValidationError(errors))
        else:
            for error in self.error_list:
                message = error.message
                if error.params:
                    message %= error.params
                yield force_text(message)

    def __str__(self):
        if hasattr(self, 'error_dict'):
            return repr(dict(self))
        return repr(list(self))

    def __repr__(self):
        return 'ValidationError(%s)' % self


class EmptyResultSet(Exception):
    """A database query predicate is impossible."""
    pass
