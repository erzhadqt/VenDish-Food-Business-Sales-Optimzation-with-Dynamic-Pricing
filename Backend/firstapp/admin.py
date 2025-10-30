from django.contrib import admin
from .models import Product, Costing, Order, OrderProduct, Sales, Feedback

# Register your models here
admin.site.register(Product)
admin.site.register(Costing)
admin.site.register(Order)
admin.site.register(OrderProduct)
admin.site.register(Sales)
admin.site.register(Feedback)