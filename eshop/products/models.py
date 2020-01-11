from django.db import models

# Create your models here.

class product(models.Model):
    product_name = models.CharField(max_length=150)
    product_color = models.CharField(max_length=150)
    product_price = models.DecimalField(max_digits=9, decimal_places=2)
    product_image = models.ImageField(upload_to='images')
    product_avability = models.BooleanField(blank= 'True')

    def __str__(self):
        return self.product_name