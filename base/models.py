from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.


class Task(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    priority = models.IntegerField(default=1)
    dueDate = models.DateTimeField(default=timezone.now, blank=True, null=True)
    assignUser = models.ForeignKey(User, related_name='%(class)s_requests_created', on_delete=models.CASCADE,default="Admin")

    def __str__(self):
        return self.title

    class Meta:
        order_with_respect_to = 'user'
