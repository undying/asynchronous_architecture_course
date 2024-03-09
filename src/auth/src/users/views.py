from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from oauth2_provider.views.mixins import ProtectedResourceMixin


# Create your views here.
class UserInfoView(ProtectedResourceMixin, View):
    def get(self, request, *args, **kwargs):
        user = request.user
        return JsonResponse({
            "id": user.id,
            "email": user.email,
        })
