from django.db import models

class Product(models.Model):
    product_name = models.CharField(max_length=80)
    product_price = models.FloatField()
