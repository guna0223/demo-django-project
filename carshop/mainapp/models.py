from django.db import models

# Create your models here.
class Products(models.Model):
    img = models.ImageField(upload_to="product_images/")
    title = models.CharField(max_length=200)
    model = models.TextField(max_length=400)
    link = models.CharField(max_length=200)
    active = models.BooleanField(default=False)
    
