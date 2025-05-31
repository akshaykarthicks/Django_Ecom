from django.contrib import admin
from .models import Category,customer,product,order
 
#to add in the database

# Register your models here.
admin.site.register(Category)
admin.site.register(customer)
admin.site.register(product)
admin.site.register(order)