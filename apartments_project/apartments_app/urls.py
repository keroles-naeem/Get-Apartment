from django.urls import path  
from .views import (  
    ApartmentListCreateAPIView,  
    ApartmentRetrieveUpdateDestroyAPIView,  
    InquiryListCreateAPIView,  
    InquiryRetrieveUpdateDestroyAPIView,
    apartment_search_view,
    apartment_list
)  

urlpatterns = [  
    path('search/', apartment_search_view, name='apartment_search'),  
    path('list/', apartment_list, name='apartment_list'),  #

    path('apartments/', ApartmentListCreateAPIView.as_view(), name='apartment-list-create'),  
    path('apartments/<int:pk>/', ApartmentRetrieveUpdateDestroyAPIView.as_view(), name='apartment-detail'),  
    path('inquiries/', InquiryListCreateAPIView.as_view(), name='inquiry-list-create'),  
    path('inquiries/<int:pk>/', InquiryRetrieveUpdateDestroyAPIView.as_view(), name='inquiry-detail'),  
]