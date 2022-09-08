from django.db import models
from django.utils import timezone
# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=30)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now, null=True)
    last_updated = models.DateTimeField(default=timezone.now, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def delete(self, using=None, keep_parents=False):
        self.is_active = False
        self.save()