from rest_framework import generics  
from .models import Apartment, Inquiry  
from .serializers import ApartmentSerializer, InquirySerializer  
from django_filters import rest_framework as filters    
from django.core.paginator import Paginator  
from django.shortcuts import render,redirect,get_object_or_404  
from .forms import ApartmentForm, InquiryForm  


# Define a filter set for filtering Apartment objects  
class ApartmentFilter(filters.FilterSet):
    property_type = filters.ChoiceFilter(choices=Apartment.PROPERTY_TYPE_CHOICES)
    search = filters.CharFilter(field_name='title', lookup_expr='icontains', label='Search')
    min_price = filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = filters.NumberFilter(field_name='price', lookup_expr='lte')

    class Meta:
        model = Apartment
        fields = ['property_type', 'search', 'min_price', 'max_price']
class ApartmentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ApartmentFilter

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
    
def apartment_detail(request, apartment_id):
    apartment = get_object_or_404(Apartment, id=apartment_id)
    inquiries = apartment.inquiry_set.all()
    print(inquiries)
    print("hiiiiiiii")
    
    return render(request, 'apartment_detail.html', {
        'apartment': apartment,
        'inquiries': inquiries,

    })
def apartment_search_view(request):  
    return render(request, 'apartment_search.html')


def apartment_list(request):  
    apartment_list = Apartment.objects.all()  # Get all apartments  
    paginator = Paginator(apartment_list, 4)  # Show 4 apartments per page  

    page_number = request.GET.get('page')  # Get the page number from the URL  
    apartments = paginator.get_page(page_number)  # Get the apartments for that page  

    return render(request, 'apartment_list.html', {'apartments': apartments})  


def add_apartment(request):  
    if request.method == 'POST':  
        print ("i passed here")
        apartment_form = ApartmentForm(request.POST)  
        inquiry_form = InquiryForm(request.POST)  

        if apartment_form.is_valid() and inquiry_form.is_valid():  
            # First, save the apartment  
            apartment = apartment_form.save()  

            # Then, create the inquiry associated with the new apartment  
            inquiry = inquiry_form.save(commit=False)  
            inquiry.apartment = apartment  # Link the inquiry to the newly created apartment  
            inquiry.save()  

            return redirect('apartment_list')  # Redirect to a success page or apartment list  

    else:  
        apartment_form = ApartmentForm()  
        inquiry_form = InquiryForm()  

    return render(request, 'add_apartment.html', {  
        'apartment_form': apartment_form,  
        'inquiry_form': inquiry_form,  
    })  