from django.db import models
from category.models import Category
from ckeditor.fields import RichTextField

# Create your models here.
class Goal(models.Model):
    goal = models.CharField(max_length=250)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.goal
    

class Task(models.Model):
    day_id = models.IntegerField()
    subject = models.CharField(max_length=250)
    desc = models.CharField(max_length=500)
    image = models.ImageField(upload_to='photos/task', blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.subject

class WorkOut(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
