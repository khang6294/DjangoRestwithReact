from django.contrib import admin
from .models import DateData
# Register your models here.


class DateDataAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'total_customers', 'total_messages']

    search_fields = ['pub_date','total_customers']

    list_filter = ['total_customers','total_messages']

    list_display = ['pub_date','total_customers','total_messages']

    list_editable = ['total_customers']

admin.site.register(DateData,DateDataAdmin)