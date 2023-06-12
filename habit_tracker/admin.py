from django.contrib import admin
from .models import Goal, Task
# Register your models here.

class GoalAdmin(admin.ModelAdmin):
    list_display = ('goal', 'is_completed', 'updated_at')
    search_fields = ('goal', )

class TaskAdmin(admin.ModelAdmin):
    list_display = ('subject', 'is_completed', 'updated_at')
    search_fields=('subject',)

admin.site.register(Goal, GoalAdmin)
admin.site.register(Task, TaskAdmin)