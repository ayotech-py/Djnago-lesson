import collections
from http.client import PAYMENT_REQUIRED
from itertools import product
from pyexpat import model
from termios import PENDIN
from tkinter import CASCADE
from unicodedata import name
from django.db import models

class Collection(models.Model):
    name = models.CharField(max_length=225)
    featured_products = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True, related_name='+')

class Promotion(models.Model):
    description = models.CharField(max_length=255)
    discount = models.FloatField()

class Product(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)
    collection = models.ForeignKey(Collection, on_delete=models.PROTECT)
    promotions = models.ManyToManyField(Promotion)

class Customer(models.Model):
    MEMBERSHIP_BRONZE = 'B'
    MEMBERSHIP_SLIVER = 'S'
    MEMBERSHIP_GOLD = 'G'

    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_BRONZE, 'Bronze'),
        (MEMBERSHIP_SLIVER, 'Sliver'),
        (MEMBERSHIP_SLIVER, 'Gold'),
    ]
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True)
    membership = models.CharField(max_length=1, choices=MEMBERSHIP_CHOICES)
    
class Order(models.Model):
    placed_at = models.DateField(auto_now_add=True)
    PENDING = 'P'
    COMPLETED = 'C'
    FAILED = 'F'
    
    PAYMENT = [
        (PENDING, 'Pending'),
        (COMPLETED, 'Completed'),
        (FAILED, 'Failed')
    ]
    payment_status = models.CharField(max_length=1, choices=PAYMENT, default=PENDING)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    
class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    #One To One Relationship
    #customer = models.OneToOneField(Customer, on_delete=CASCADE, primary_key=True)
    #One To One Relationship
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    
class OrderItems(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)    

class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
    quantity = models.PositiveIntegerField()
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    cart = models.ForeignKey(Cart, on_delete=models.PROTECT)