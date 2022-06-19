from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='Name')
    price = models.IntegerField(verbose_name='Price')
    created_dt = models.DateTimeField(auto_now_add=True, verbose_name='Created Date')
    description = models.TextField(verbose_name='Description')
    stock = models.IntegerField(verbose_name='Stock')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        db_table = 'my_product'

        