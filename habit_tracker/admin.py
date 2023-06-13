from django.contrib import admin
from .models import Goal, Task, WorkOut
# Register your models here.

class GoalAdmin(admin.ModelAdmin):
    list_display = ('goal', 'is_completed', 'updated_at')
    search_fields = ('goal', )

class TaskAdmin(admin.ModelAdmin):
    list_display = ('day_id','subject', 'is_completed', 'updated_at')
    search_fields=('subject',)

class WorkOutAdmin(admin.ModelAdmin):
    list_display = ('title','created_at')
    search_fields = ('title',)

admin.site.register(Goal, GoalAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(WorkOut, WorkOutAdmin)