from django.http import HttpResponseBadRequest

def ajax_required(f):
    """
    Decorator to ensure that a view only accepts AJAX requests.
    """
    def wrap(request, *args, **kwargs):
        if not request.is_ajax():
            return HttpResponseBadRequest("This view can only be accessed via AJAX.")
        return f(request, *args, **kwargs)
        wrap.__doc__ = f.__doc__
        wrap.__name__ = f.__name__
    return wrap

