from dashboard import views as dashboard_views
from django.urls import path


app_name = "dashboard"
urlpatterns = [
    path("task/create/", dashboard_views.TaskCreateView.as_view(), name="task_create"),
    path("task/complete/<int:pk>/", dashboard_views.TaskCompleteView.as_view(), name="task_complete"),
    path("task/delete/<int:pk>/", dashboard_views.TaskDeleteView.as_view(), name="task_delete"),
    path("task/update/<int:pk>/", dashboard_views.TaskUpdateView.as_view(), name="task_update"),
    path("tasks/", dashboard_views.TaskListView.as_view(), name="task_list"),
]
