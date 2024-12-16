from rest_framework import generics  
from .models import Apartment, Inquiry  
from .serializers import ApartmentSerializer, InquirySerializer  
from django_filters import rest_framework as filters  

# Define a filter set for filtering Apartment objects  
class ApartmentFilter(filters.FilterSet):  
    property_type = filters.ChoiceFilter(choices=Apartment.PROPERTY_TYPE_CHOICES)  
    search = filters.CharFilter(field_name='title', lookup_expr='icontains', label='Search')  # New search filter  

    class Meta:  
        model = Apartment  
        fields = ['property_type', 'search']  # Expose property_type and search for filtering  

# View for listing and creating Apartment objects with filtering capabilities  
class ApartmentListCreateAPIView(generics.ListCreateAPIView):  
    queryset = Apartment.objects.all()  
    serializer_class = ApartmentSerializer  
    filter_backends = (filters.DjangoFilterBackend,)  # Enable filtering  
    filterset_class = ApartmentFilter  # Link the filter set to the view  

# View for retrieving, updating, or deleting a specific Apartment object  
class ApartmentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):  
    queryset = Apartment.objects.all()  
    serializer_class = ApartmentSerializer  

# Generic views for Inquiry  
class InquiryListCreateAPIView(generics.ListCreateAPIView):  
    queryset = Inquiry.objects.all()  
    serializer_class = InquirySerializer  

class InquiryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):  
    queryset = Inquiry.objects.all()  
    serializer_class = InquirySerializer
    
    
from django.shortcuts import render  

def apartment_search_view(request):  
    return render(request, 'apartment_search.html')


def apartment_list(request):  
    apartments = Apartment.objects.all()  # Fetch all apartments  
    return render(request, 'apartment_list.html', {'apartments': apartments})  