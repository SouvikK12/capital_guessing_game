from rest_framework import serializers
from core.models import Country_and_Capital


class CountryAndCapitalSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Country_and_Capital
        fields = '__all__'