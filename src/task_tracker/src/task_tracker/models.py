from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    public_id = models.UUIDField()


class Task(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='authored_tasks')
    assignee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assigned_tasks')
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    completed_at = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.is_completed and self.completed_at is None:
            self.completed_at = timezone.now()
        elif not self.is_completed:
            self.completed_at = None
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Task #{self.pk} by {self.author.username}"

    class Meta:
        ordering = ['-created_at']
