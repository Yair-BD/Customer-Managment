from django.db import models
from django.db.models.base import Model
from django.db.models.fields import EmailField, FloatField

class Customer(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=50, null=True)
    date_create = models.DateTimeField(auto_now_add=True, null=True)
    date_update = models.DateTimeField(auto_now_add=False, auto_now=True, null=True)



    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)


    def __str__(self):
        return self.name

class Product(models.Model):
    CATEGORY = (
        ('Indoor','Indoor'),
        ('Outdoor','Outdoor')
    )

    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    date_create = models.DateTimeField(auto_now_add=True, null=True)
    tags = models.ManyToManyField(Tag)


    def __str__(self):
        return self.name

 
class Order(models.Model):
    STATUS = (
        ('Pending','Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered','Delivered')
    )
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    date_create = models.DateTimeField(auto_now_add=True, null=True)
    date_update = models.DateTimeField(auto_now_add=False, auto_now=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)


