from rest_framework import serializers
from .models import DateData
from rest_framework.response import Response


class DateDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = DateData
        fields = ('pub_date','total_messages','total_customers')

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid(raise_exception=False):
            return Response({"Fail": "blablal"})

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({"Success": "msb blablabla"})