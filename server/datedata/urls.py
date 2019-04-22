from django.urls import path

from .views import DateDataView

app_names = 'datedata'

urlpatterns = [
    path('daily/', DateDataView.as_view())
]