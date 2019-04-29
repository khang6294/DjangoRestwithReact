from django.contrib import admin
from .models import DateData
# Register your models here.


class DateDataAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'total_customers', 'total_messages']

admin.site.register(DateData,DateDataAdmin)