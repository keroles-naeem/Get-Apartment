from rest_framework import generics  
from .models import Apartment, Inquiry  
from .serializers import ApartmentSerializer, InquirySerializer  
from django_filters import rest_framework as filters  
from django.shortcuts import render  
from django.core.paginator import Paginator  


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
    
    

def apartment_search_view(request):  
    return render(request, 'apartment_search.html')


def apartment_list(request):  
    apartment_list = Apartment.objects.all()  # Get all apartments  
    paginator = Paginator(apartment_list, 4)  # Show 10 apartments per page  

    page_number = request.GET.get('page')  # Get the page number from the URL  
    apartments = paginator.get_page(page_number)  # Get the apartments for that page  

    return render(request, 'apartment_list.html', {'apartments': apartments})  