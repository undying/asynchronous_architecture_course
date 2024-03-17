from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import View

from dashboard import forms as dashboard_forms
from dashboard import models as dashboard_models


# Create your views here.
class IndexView(LoginRequiredMixin, View):
    def get(self, request):
        authored_tasks = dashboard_models.Task.objects.filter(author_id=request.user)
        assigned_tasks = dashboard_models.Task.objects.filter(assignee_id=request.user)
        return render(
            request,
            "index.html",
            {"authored_tasks": authored_tasks, "assigned_tasks": assigned_tasks},
        )

class CreateTaskView(LoginRequiredMixin, View):
    def get(self, request):
        form = dashboard_forms.TaskForm()
        return render(request, "create_task.html", {'form': form})

    def post(self, request):
        form = dashboard_forms.TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "index.html")
