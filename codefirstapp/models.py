from django.db import models

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=50)
    product_desc = models.CharField(max_length=2000)


class ProductTest(models.Model):
    product_name = models.CharField(max_length=50)
    product_desc = models.CharField(max_length=2000)