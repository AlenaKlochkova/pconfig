from rest_framework import serializers

from .models import Processor


class ComponentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Processor
        fields = '__all__'
