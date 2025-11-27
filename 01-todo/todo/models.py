from django.db import models
from django.urls import reverse

class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    due_date = models.DateField(null=True, blank=True)
    resolved = models.BooleanField(default=False, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=["due_date"]),
            models.Index(fields=["resolved"]),
        ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("todo_detail", args=[self.pk])
