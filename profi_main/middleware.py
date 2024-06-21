from django.utils.deprecation import MiddlewareMixin

class CookieConsentMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        if not request.COOKIES.get('cookie_consent'):
            response.set_cookie('cookie_consent', 'false')
        return response
