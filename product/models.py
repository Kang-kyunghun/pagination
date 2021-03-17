from django.db import models

class Product(models.Model):
    name        = models.CharField(max_length=100)
    image_url   = models.URLField(max_length=2000)
    description = models.CharField(max_length=2000)

    class Meta:
        db_table    = 'products'