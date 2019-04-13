from django.contrib import admin
from todo.models import Todo,UserProfile

class TodoAdmin(admin.ModelAdmin):
    list_display = ('title','description','completed')

# Register your models here.

admin.site.register(Todo)
admin.site.register(UserProfile)
