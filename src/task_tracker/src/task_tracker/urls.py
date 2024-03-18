"""
URL configuration for task_tracker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from dashboard import views as dashboard_views
from task_tracker import views as tt_views


urlpatterns = [
    path("dashboard/", include("dashboard.urls", namespace="dashboard")),
    path("accounts/login/", tt_views.TTLoginView.as_view(), name="login"),
    path("admin/", admin.site.urls),
    path("", dashboard_views.TaskListView.as_view()),
    path("", include("social_django.urls", namespace="social")),
]
