from rest_framework import serializers
from .models import *


class ClientSerializer(serializers.ModelSerializer):
	# house = HouseNumberSerializer(read_only=True)
	class Meta:
		model = Client
		fields = '__all__'
