from django.contrib import admin
from .models import Goal
# Register your models here.

class GoalAdmin(admin.ModelAdmin):
    list_display = ('goal', 'is_completed', 'updated_at')
    search_fields = ('goal', )

admin.site.register(Goal, GoalAdmin)

