from django.db import models

# Create your models here.

class Apartment(models.Model):  
    PROPERTY_TYPE_CHOICES = [  
        ('villa', 'Villa'),  
        ('apartment', 'Apartment'),  
        ('townhouse', 'Townhouse'),  
    ]  
    
    title = models.CharField(max_length=255)  
    description = models.TextField()  
    price = models.DecimalField(max_digits=10, decimal_places=2)  
    location = models.CharField(max_length=255)  
    bedrooms = models.IntegerField()  
    bathrooms = models.IntegerField()  
    property_type = models.CharField(max_length=20, choices=PROPERTY_TYPE_CHOICES, default='apartment')  
    # image = models.ImageField(upload_to='apartments/', blank=True, null=True)  


    def __str__(self):  
        return self.title  

class Inquiry(models.Model):  
    apartment = models.ForeignKey(Apartment, related_name='inquiry_set', on_delete=models.CASCADE)  
    name = models.CharField(max_length=255)  
    email = models.EmailField()  
    message = models.TextField()  
    phone = models.CharField(max_length=20, blank=True, null=True)
    def __str__(self):  
        return f"Inquiry for {self.apartment.title} by {self.name}"