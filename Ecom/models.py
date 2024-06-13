from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length = 300)
    description = models.TextField(max_length=5000)
    price = models.DecimalField(max_digits = 9, decimal_places = 2)
    image = models.ImageField(upload_to = 'products/')