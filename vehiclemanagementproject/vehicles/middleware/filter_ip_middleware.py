
from django.http import HttpResponseForbidden

class FilterIPMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        allowed_ips = ['127.0.0.1']
        if request.META.get('REMOTE_ADDR') not in allowed_ips:
            return HttpResponseForbidden("Your IP address is not authorized to access this page")
        response = self.get_response(request)
        return response
