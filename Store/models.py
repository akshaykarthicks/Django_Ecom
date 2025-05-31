from django.db import models
import datetime

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
    class Meta: # this is for the admin panel   
        verbose_name='category'
        verbose_name_plural = 'category'
    

class customer(models.Model):
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    phone=models.CharField(max_length=50)
    email=models.EmailField(max_length=150)
    password=models.CharField(max_length=50)
    
    def __str__(self):
        return f'{self.firstname} {self.lastname}'
    
class product(models.Model):
    name=models.CharField(max_length=50)    
    price=models.DecimalField(default=0,max_digits=10,decimal_places=2)
    description=models.CharField(max_length=11500)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,default=1) # category of product 
    image= models.ImageField(upload_to='uploads/product/')
    
    # SALE STAR 
    #migrate to sale model
    is_sale=models.BooleanField(default=False) # is sale on or not  in admin panel
    sale_price=models.DecimalField(max_digits=10,decimal_places=2,default=0) # sale price of product
    
    
    def __str__(self):
        return self.name
    
#customer
class order(models.Model):
    product=models.ForeignKey(product,on_delete=models.CASCADE)
    customer=models.ForeignKey(customer,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    address=models.CharField(max_length=500,blank=True)
    phone=models.CharField(max_length=50)
    date=models.DateTimeField(default=datetime.datetime.now)
    status=models.CharField(max_length=50,default='pending')
    
    
    def __str__(self):
        return self.name    
    