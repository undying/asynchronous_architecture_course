from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from django.contrib.auth.models import User
from .models import Task


class UserTasksView(ListView):
    model = Task
    template_name = 'tasks/user_tasks.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        user_id = self.kwargs.get('user_id')
        user = get_object_or_404(User, pk=user_id)
        return Task.objects.filter(assignee=user)
