from rest_framework import serializers  
from .models import Apartment, Inquiry  

class ApartmentSerializer(serializers.ModelSerializer):  
    class Meta:  
        model = Apartment  
        fields = '__all__'  

class InquirySerializer(serializers.ModelSerializer):  
    class Meta:  
        model = Inquiry  
        fields = '__all__'