from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework import permissions
from .models import DateData
from rest_framework.response import Response
from datetime import datetime
from .serializers import DateDataSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
# Create your views here.

class DateDataView(ListAPIView):
    serializer_class = DateDataSerializer
    permission_classes = (permissions.IsAuthenticated,)
    def get_queryset(self):
        start_date_arr =  self.request.query_params.get('start_date',None).split('-')
        end_date_arr = self.request.query_params.get('end_date',None).split('-')
        start_date = datetime(int(start_date_arr[0]),int(start_date_arr[1]),int(start_date_arr[2]))
        end_date = datetime(int(end_date_arr[0]),int(end_date_arr[1]),int(end_date_arr[2]))
        data = DateData.objects.filter(pub_date__range=(start_date,end_date))
        return data

    def list(self, request):
        queryset = self.get_queryset()
        serializer = DateDataSerializer(queryset, many=True)
        totalMessagesArr = list(map(lambda x: x["total_messages"], serializer.data))
        totalMessages = sum(totalMessagesArr)
        totalCustomersArr = list(map(lambda x: x["total_customers"], serializer.data))
        totalCustomers = sum(totalCustomersArr)
        return Response({
                "start_date": self.request.query_params.get('start_date',None),
                "end_date": self.request.query_params.get('end_date',None),
                "totalMessages": totalMessages,
                "totalCustomers": totalCustomers,
                "by_date": serializer.data
            })

class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })
