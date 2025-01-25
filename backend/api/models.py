from enum import unique
from itertools import product
from tkinter import CASCADE
from django.forms import BooleanField
from django.utils import timezone
from shortuuid.django_fields import ShortUUIDField

from django.db import models
from userauths.models import User, CustomerProfile, VendorProfile
from django.utils.text import slugify

"""
Category
Subcategory
Product
Cart
order
Wishlist
"""
CATEGORY_TYPE = (
    ('MEN', 'MEN'),
    ('WOMEN', 'WOMEN'),
    ('TEEN', 'TEEN'),
)

PAYMENT_STATUS = (
    ('Paid', 'Paid'),
    ('Processing', 'Processing'),
    ('Failed', 'Failed'),
) 

RATING = (
    (1, '1 Star'),
    (2, '2 Star'),
    (3, '3 Star'),
    (4, '4 Star'),
    (5, '5 Star'),
)

ORDER_STATUS = (
    ('Pending', 'Pending'),
    ('Shipped', 'Shipped'),
    ('Delivered', 'Delivered'),
    ('Cancelled', 'Cancelled'),
)

PAYMENT_METHOD_CHOICES = (
        ('credit_card', 'Credit Card'),
        ('paypal', 'PayPal'),
        ('bank_transfer', 'Bank Transfer'),
 )
PAYMENT_STATUS_CHOICES = (
    ('pending', 'Pending'),
    ('completed', 'Completed'),
    ('failed', 'Failed'),
)

class Category(models.Model):
    title = models.CharField(max_length=200, choices=CATEGORY_TYPE, default='MEN')
    slug = models.SlugField(unique=True, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['-title']
        
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if self.slug == "" or self.slug == None:
            self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)

class SubCategory(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')

class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name='products', null=True, blank=True)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.SET_NULL, null=True, blank=True, related_name='products')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    stock_quantity = models.PositiveIntegerField()
    images = models.ImageField(upload_to='product_images/', blank=True, null=True)
    vendor = models.ForeignKey(VendorProfile, on_delete=models.CASCADE, related_name='products')
    date_added = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(unique=True, null=True, blank=True)
    product_id = ShortUUIDField(unique=True, length=6, max_length=20, alphabet='1234567890')

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if self.slug == "" or self.slug == None:
            self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)

    def average_rating(self):
        average_rating = Review.objects.filter(prodect=self).aggregate(avg_rating=models.Avg('rating'))
        return average_rating['avg_rating']
    
    def rating_count(self):
        return Review.objects.filter(product=self).count()
    
    def reviews(self):
        return Review.objects.filter(product=self, active=True)
class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digit=12, default=0.00, decimal_places=2)
    vat = models.DecimalField(max_digit=12, default=0.00, decimal_places=2)
    total = models.DecimalField(max_digit=12, default=0.00, decimal_places=2)
    cart_id = ShortUUIDField(unique=True, length=6, max_length=20, alphabet='1234567890')
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.product.title

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.quantity} x {self.product.name} in Cart {self.cart.id}"
    
class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    vendor = models.ManyToManyField(VendorProfile, blank=True)
    sub_total = models.DecimalField(max_digit=12, default=0.00, decimal_places=2)
    total = models.DecimalField(max_digit=12, default=0.00, decimal_places=2)
    coupons = models.ManyToManyField('api.Coupon', blank=True)
    stripe_session_id = models.CharField(max_length=1000, null=True, blank=True)
    order_id = ShortUUIDField(unique=True, length=6, max_length=20, alphabet='1234567890')
    date = models.DateTimeField(timezone.now)
    order_status = models.CharField(max_length=50, choices=ORDER_STATUS, default='Pending')

    class Meta:
        ordering = ['-date']

    def order_items(self):
        return OrderItem.objects.filter(order=self)

    def __str__(self):
        return self.order_id
    

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='orderitem')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_item')
    vendor = models.ForeignKey(VendorProfile, on_delete=CASCADE)
    vat = models.DecimalField(max_digit=12, default=0.00, decimal_places=2)
    total = models.DecimalField(max_digit=12, default=0.00, decimal_places=2)
    initial_total = models.DecimalField(max_digit=12, default=0.00, decimal_places=2)
    saved = models.DecimalField(max_digit=12, default=0.00, decimal_places=2)
    coupons = models.ManyToManyField('api.Coupon', blank=True)
    applied_coupon = models.BooleanField(default=False)
    order_id = ShortUUIDField(unique=True, length=6, max_length=20, alphabet='1234567890')
    date = models.DateTimeField(timezone.now)

    class Meta:
        ordering = ['-date']

    def order_id(self):
        return f"order ID #{self.order.order_id}"
    
    def payment_status(self):
        return f"{self.order.payment_status}"
    
    def __str__(self):
        return self.order_id
    
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    review = models.TextField()
    rating = models.IntegerField(choices=RATING, default=None)
    reply = models.CharField(null=True, blank=True, max_length=1000)
    date = models.DateTimeField(default=timezone.now)
    active = models.BooleanField(default=False) 

    def __str__(self):
        return self.product.title
    

    def profile(self):
        return CustomerProfile.objects.get(user=self.user)
    
class Payment(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    method = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_id = models.CharField(max_length=255)
    status = models.CharField(max_length=50)
    payment_date = models.DateTimeField(auto_now_add=True)

# Shipping Management
class ShippingAddress(models.Model):
    user = models.ForeignKey(CustomerProfile, on_delete=models.CASCADE)
    address_line1 = models.CharField(max_length=255)
    address_line2 = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)

class Wishlist(models.Model):
    user = models.ForeignKey(CustomerProfile, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
