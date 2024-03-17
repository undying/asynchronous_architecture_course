from django.contrib.auth.views import LoginView


# Create your views here.
class TTLoginView(LoginView):
    template_name = 'users/login.html'
    success_url = '/'
