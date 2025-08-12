from django.shortcuts import redirect
from django.urls import reverse


class LoginRequiredMiddleware:
    """Redirect anonymous users to the login page."""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        login_url = reverse('login')
        if not request.user.is_authenticated and request.path != login_url:
            return redirect(login_url)
        return self.get_response(request)
