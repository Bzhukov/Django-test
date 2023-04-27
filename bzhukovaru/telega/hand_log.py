import logging

logger = logging.getLogger('django')

class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        logger.info('Request: {method} {path}'.format(method=request.method, path=request.path))
        response = self.get_response(request)
        return response
