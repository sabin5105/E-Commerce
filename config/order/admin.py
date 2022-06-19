from django.contrib import admin
from order.models import Order

# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'product',)

admin.site.register(Order, OrderAdmin)