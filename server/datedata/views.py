from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import DateData
from rest_framework.response import Response
from datetime import datetime
from .serializers import DateDataSerializer
# Create your views here.

class DateDataView(ListAPIView):
    serializer_class = DateDataSerializer
    
    def get_queryset(self):
        start_date_arr =  self.request.query_params.get('start_date',None).split('-')
        end_date_arr = self.request.query_params.get('end_date',None).split('-')
        start_date = datetime(int(start_date_arr[0]),int(start_date_arr[1]),int(start_date_arr[2]))
        end_date = datetime(int(end_date_arr[0]),int(end_date_arr[1]),int(end_date_arr[2]))
        data = DateData.objects.filter(pub_date__range=(start_date,end_date))
        return data

