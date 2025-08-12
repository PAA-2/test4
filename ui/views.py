from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_protect

ROLE_REDIRECTS = {
    'admin': 'admin_dashboard',
    'manager': 'manager_dashboard',
}


@csrf_protect
def login_view(request):
    """Authenticate the user and redirect based on their role."""
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Connexion réussie.')
            role = getattr(user, 'role', '')
            target = ROLE_REDIRECTS.get(role, 'home')
            return redirect(target)
        messages.error(request, 'Identifiants invalides.')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


@csrf_protect
def logout_view(request):
    """Log the user out and return to the login page."""
    if request.method == 'POST':
        logout(request)
        messages.info(request, 'Déconnexion réussie.')
        return redirect('login')
    return render(request, 'logout.html')
