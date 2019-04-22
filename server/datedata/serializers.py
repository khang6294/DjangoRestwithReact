from rest_framework import serializers
from .models import DateData

class DateDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = DateData
        fields = ('pub_date','total_messages','total_customers')