from rest_framework import serializers
from .models import Tariff, UserSubscription

class TariffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tariff
        fields = ['id', 'name', 'price', 'description']

class UserSubscriptionSerializer(serializers.ModelSerializer):
    tariff = TariffSerializer(read_only=True)
    tariff_id = serializers.PrimaryKeyRelatedField(queryset=Tariff.objects.all(), source='tariff', write_only=True)

    class Meta:
        model = UserSubscription
        fields = ['id', 'user', 'tariff', 'tariff_id', 'start_date', 'end_date']
        read_only_fields = ['user', 'start_date']