from rest_framework import serializers
from . models import TempModel



class TempModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = TempModel
        fields = ('url', 'date', 'temperature')

