from django.db import models

# Create your models here.
class Order(models.Model):
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, verbose_name='User')

    product = models.ForeignKey('product.Product', on_delete=models.CASCADE, verbose_name='Product')
    quantity = models.IntegerField(verbose_name='Quantity')
    created_dt = models.DateTimeField(auto_now_add=True, verbose_name='Created Date')

    def __str__(self):
        return self.name

    class Meta: # admin page setting
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
        db_table = 'my_order'