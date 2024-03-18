from django import forms
from django.contrib.auth.models import User

from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description", "is_completed", "assignee"]
        widgets = {
            "assignee": forms.Select(attrs={"placeholder": "Choose assignee"}),
            "is_completed": forms.CheckboxInput(),
            "title": forms.TextInput(
                attrs={"placeholder": "Title", "size": "40", "maxlength": "100"}
            ),
        }

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields["assignee"].queryset = User.objects.filter(is_active=True)
        self.fields["assignee"].label_from_instance = lambda obj: obj.email
