from django.utils import timezone
from shortuuid.django_fields import ShortUUIDField
import shortuuid
from django_ckeditor_5.fields import CKEditor5Field
from django.utils.text import slugify

from django.db import models
from userauths.models import User, Profile
from django.db.models import CASCADE



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
PAYMENT_METHOD = (
    ('PayPal', 'PayPal'),
    ('Stripe', 'Stripe'),
    ('Flutterwave', 'Flutterwave'),
    ('Paystack', 'Paystack'),
    ('Visa', 'Visa'),
    ('Mastercard', 'Mastercard'),
    ('bank_transfer', 'Bank Transfer'),
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

PAYMENT_STATUS_CHOICES = (
    ('pending', 'Pending'),
    ('completed', 'Completed'),
    ('failed', 'Failed'),
)
STATUS = (
    ('Published', 'Published'),
    ('Draft', 'Draft'),
    ('Disabled', 'Disabled'),
)

class Category(models.Model):
    title = models.CharField(max_length=200, choices=CATEGORY_TYPE, default='MEN')
    slug = models.SlugField(unique=True, null=True, blank=True)
    image = models.ImageField(upload_to='image', null=True, blank=True)

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

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name='products', null=True, blank=True)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.SET_NULL, null=True, blank=True, related_name='products')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    stock = models.PositiveIntegerField(default=0, null=True, blank=True)
    images = models.ImageField(upload_to='product_images/', blank=True, null=True)
    vendor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')
    date_added = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(unique=True, null=True, blank=True)
    product_id = ShortUUIDField(unique=True, length=6, max_length=20, alphabet='1234567890')
    status = models.CharField(choices=STATUS, max_length=50, default='Published')
    date = models.DateTimeField(timezone.now)


    class Meta:
        ordering = ['-id']
        verbose_name_plural = "Products"

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if self.slug == "" or self.slug == None:
            self.slug = slugify(self.title) + "-" + str(shortuuid.uuid().lower()[:2])
        super(Product, self).save(*args, **kwargs)

    def average_rating(self):
        average_rating = Review.objects.filter(prodect=self).aggregate(avg_rating=models.Avg('rating'))
        return average_rating['avg_rating']
    
    def rating_count(self):
        return Review.objects.filter(product=self).count()
    
    def reviews(self):
        return Review.objects.filter(product=self, active=True)

class Variant(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=1000, verbose_name="Variant Name", null=True, blank=True)

    def items(self):
        return VariantItem.objects.filter(variant=self)
    
    def __str__(self):
        return self.name
    
class VariantItem(models.Model):
    variant = models.ForeignKey(Variant, on_delete=models.CASCADE, related_name='variant_items')
    title = models.CharField(max_length=1000, verbose_name="Item Title", null=True, blank=True)
    content = models.CharField(max_length=1000, verbose_name="Item Content", null=True, blank=True)

    def __str__(self):
        return self.variant.name

class Gallery(models.Model):
    product = models.ForeignKey(Product, on_delete=CASCADE, null=True, blank=True)
    image = models.FileField(upload_to='images', default='gallery.jpg')
    gallery_id= ShortUUIDField(unique=True, length=6, max_length=20, alphabet='1234567890')

    def __str__(self):
        return f"{self.product.name} - image"


class Coupon(models.Model):
    vendor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    code = models.CharField(max_length=100)
    discount = models.IntegerField(default=1)

    def __str__(self):
        return self.code
    
class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=12, default=0.00, decimal_places=2)
    vat = models.DecimalField(max_digits=12, default=0.00, decimal_places=2)
    total = models.DecimalField(max_digits=12, default=0.00, decimal_places=2)
    cart_id = models.CharField(max_length=1000, null=True, blank=True)
    qty = models.PositiveIntegerField(default=0, null=True, blank=True)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.cart_id} - {self.product.name}"

    
class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='customer', blank=True)
    vendor = models.ManyToManyField(User, blank=True)
    sub_total = models.DecimalField(max_digits=12, default=0.00, decimal_places=2)
    shipping = models.DecimalField(max_digits=12, default=0.00, decimal_places=2)
    tax = models.DecimalField(max_digits=12, default=0.00, decimal_places=2)
    total = models.DecimalField(max_digits=12, default=0.00, decimal_places=2)
    coupons = models.ManyToManyField(Coupon, blank=True)
    payment_id = models.CharField(max_length=1000, null=True, blank=True)
    order_id = ShortUUIDField(length=6, max_length=20, alphabet='1234567890')
    date = models.DateTimeField(timezone.now)
    order_status = models.CharField(max_length=50, choices=ORDER_STATUS, default='Pending')
    payment_status = models.CharField(max_length=100, choices=PAYMENT_STATUS, default='Processing')
    payment_method = models.CharField(max_length=100, choices=PAYMENT_METHOD, default='Bank Transfer')
    


    class Meta:
        ordering = ['-date']

    def order_items(self):
        return OrderItem.objects.filter(order=self)

    def __str__(self):
        return self.order_id
    

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    vendor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    order_status = models.CharField(max_length=50, choices=ORDER_STATUS, default='Pending')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    vat = models.DecimalField(max_digits=12, default=0.00, decimal_places=2)
    total = models.DecimalField(max_digits=12, default=0.00, decimal_places=2)
    initial_total = models.DecimalField(max_digits=12, default=0.00, decimal_places=2)
    saved = models.DecimalField(max_digits=12, default=0.00, decimal_places=2)
    coupon = models.ManyToManyField(Coupon, blank=True) 
    applied_coupon = models.BooleanField(default=False)
    color = models.CharField(max_length=100, null=True, blank=True)
    size = models.CharField(max_length=100, null=True, blank=True)
    qty = models.IntegerField(default=0)
    item_id = ShortUUIDField(unique=True, length=6, max_length=20, alphabet='1234567890')
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
    review = models.TextField(null=True, blank=True)
    rating = models.IntegerField(choices=RATING, default=None)
    reply = models.CharField(null=True, blank=True, max_length=1000)
    date = models.DateTimeField(default=timezone.now)
    active = models.BooleanField(default=False) 

    def __str__(self):
        return self.product.title
    

    def profile(self):
        return User.objects.get(user=self.user)
    



class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)



    