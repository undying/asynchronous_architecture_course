from dashboard import views as dashboard_views
from django.urls import path


app_name = "dashboard"
urlpatterns = [
    path("task/create/", dashboard_views.CreateTaskView.as_view(), name="task_create"),
]
