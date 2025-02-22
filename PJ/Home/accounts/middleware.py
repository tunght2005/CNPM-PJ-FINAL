from django.contrib.auth import logout
class SessionCheckMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated and not request.session.get('UserID'):
            logout(request)
        return self.get_response(request)