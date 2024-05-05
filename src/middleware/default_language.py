from django.utils.translation import activate


class CustomLocaleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        language = request.headers.get('Accept-Language', None)
        if language:
            activate(language)
        return self.get_response(request)