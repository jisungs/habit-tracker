from django.db import models

# Create your models here.
class Goal(models.Model):
    goal = models.CharField(max_length=250)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.goal