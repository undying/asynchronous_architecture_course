
from django.shortcuts import render
from django.views import View

from django.contrib.auth.forms import AuthenticationForm

class IndexView(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'index.html', {'login_form': form})
