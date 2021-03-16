from django.db import models

class Todo(models.Model):
    description = models.CharField(max_length=255)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
