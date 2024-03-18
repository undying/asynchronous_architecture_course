from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import View
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, DeleteView
from django.db.models.functions import Now

from dashboard import forms as dashboard_forms
from dashboard import models as dashboard_models


# Create your views here.
class TaskListView(LoginRequiredMixin, View):
    def get(self, request):
        authored_tasks = dashboard_models.Task.objects.filter(author_id=request.user)
        assigned_tasks = dashboard_models.Task.objects.filter(assignee_id=request.user)
        return render(
            request,
            "task_list.html",
            {"authored_tasks": authored_tasks, "assigned_tasks": assigned_tasks},
        )


class TaskCreateView(LoginRequiredMixin, View):
    def get(self, request):
        form = dashboard_forms.TaskForm()
        return render(request, "task_create.html", {'form': form})

    def post(self, request):
        form = dashboard_forms.TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.author = request.user
            task.save()
            return redirect("dashboard:task_list")
        else:
            form = dashboard_forms.TaskForm(request.POST)
            return render(request, "task_create.html", {'form': form})


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = dashboard_models.Task
    success_url = reverse_lazy("dashboard:task_list")
    template_name = "task_list.html"
    context_object_name = "task"
    # def get(self, request, task_id):
    #     task = dashboard_models.Task.objects.get(id=task_id)
    #     task.delete()
    #     return redirect("dashboard:task_list")


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = dashboard_models.Task
    form_class = dashboard_forms.TaskForm
    template_name = "task_update.html"
    context_object_name = "task"
    success_url = reverse_lazy("dashboard:task_list")

    # def get(self, request, task_id):
    #     task = dashboard_models.Task.objects.get(id=task_id)
    #     form = dashboard_forms.TaskForm(instance=task)
    #     return render(request, "task_update.html", {'form': form})

    # def post(self, request, task_id):
    #     task = dashboard_models.Task.objects.get(id=task_id)
    #     form = dashboard_forms.TaskForm(request.POST, instance=task)
    #     if form.is_valid():
    #         form.save()
    #         return redirect("dashboard:task_list")
    #     else:
    #         form = dashboard_forms.TaskForm(request.POST, instance=task)
    #     return render(request, "task_update.html", {'form': form})


class TaskCompleteView(LoginRequiredMixin, View):
    # model = dashboard_models.Task
    # fields = ["is_completed"]
    # template_name = "task_list.html"
    # success_url = reverse_lazy("dashboard:task_list")
    def post(self, *args, **kwargs):
        task_id = kwargs.get("pk")
        task = dashboard_models.Task.objects.get(id=task_id)

        task.is_completed = True
        task.completed_at = Now()
        task.save()

        return redirect("dashboard:task_list")
