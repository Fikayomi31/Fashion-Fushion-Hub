from itertools import product
from django.utils import timezone
from shortuuid.django_fields import ShortUUIDField
import shortuuid

from django.db import models
from django.utils.text import slugify
from django.dispatch import receiver
from django.db.models.signals import post_save
from userauths.models import User, Profile
from vendor.models import Vendor
from django.db.models import CASCADE



CATEGORY_TYPE = (
    ('MEN', 'MEN'),
    ('WOMEN', 'WOMEN'),
    ('TEEN', 'TEEN'),
    ('UNISEX', 'UNISEX')
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
    ('Draft', 'Draft'),
    ('Disabled', 'Disabled'),
    ('In review', 'In Review'),
    ('Published', 'Published'),
)
SIZE_STATUS = (
    ('XXXXL', 'XXXXL'),
    ('XXXL', 'XXXL'),
    ('XXL', 'XXL'),
    ('XL', 'XL'),
    ('L', 'L'),
    ('M', 'M'),
    ('S', 'S')

)

class Category(models.Model):
    title = models.CharField(max_length=200, choices=CATEGORY_TYPE, default='MEN')
    slug = models.SlugField(unique=True, null=True, blank=True)
    image = models.ImageField(upload_to='image', null=True, blank=True)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Category"
        ordering = ['title']
        
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if self.slug == "" or self.slug == None:
            self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    shipping_amount = models.DecimalField(decimal_places=2, max_digits=12, default=0.0) 
    stock_qty = models.PositiveIntegerField(default=1)
    in_stock = models.BooleanField(default=True)
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)
    vendor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')
    rating = models.PositiveIntegerField(default=0, null=True, blank=True)
    views = models.PositiveIntegerField(default=0, null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)
    status = models.CharField(choices=STATUS, max_length=100, default='Published')
    featured = models.BooleanField(default=False)
    pid = ShortUUIDField(unique=True, length=10, max_length=20, alphabet='1234567890')    
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-id']
        verbose_name_plural = "Products"

    def __str__(self):
        return self.title
    
    def product_rating(self):
        product_rating = Review.objects.filter(product=self).aggregate(avg_rating=models.Avg('rating'))
        return product_rating['avg_rating'] or 0
    
    def rating_count(self):
        return Review.objects.filter(product=self).count()
        

    def gallery(self):
        return Gallery.objects.filter(product=self)
    
    def specification(self):
        return Specification.objects.filter(product=self)
    
    def size(self):
        return Size.objects.filter(product=self)
    
    def color(self):
        return Color.objects.filter(product=self)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        super(Product, self).save(*args, **kwargs)  # ✅ Save first

        # ✅ Now, update the rating after saving
        self.rating = self.product_rating()
    
        # ✅ Save again to update the rating field
        super(Product, self).save(update_fields=['rating'])


class Specification(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=1000)
    content = models.CharField(max_length=1000)
    
    def __str__(self):
        return self.title
    
class Size(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=1000, choices=SIZE_STATUS, default='XXL')
    

    def __str__(self):
        return self.name

class Gallery(models.Model):
    product = models.ForeignKey(Product, on_delete=CASCADE, null=True, blank=True)
    image = models.FileField(upload_to='images', default='gallery.jpg')
    gid= ShortUUIDField(unique=True, length=6, max_length=20, alphabet='1234567890')
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.product.title

class Color(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=1000)
    color_code = models.CharField(max_length=1000)

    def __str__(self):
        return self.name
    
class Coupon(models.Model):
    vendor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="coupons_provided")
    user_by = models.ManyToManyField(User, blank=True, related_name="coupons_used")
    code = models.CharField(max_length=100)
    discount = models.IntegerField(default=1)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.code
    
class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    tax = models.DecimalField(max_digits=12, default=0.00, decimal_places=2)
    total = models.DecimalField(max_digits=12, default=0.00, decimal_places=2)
    shipping_amount = models.DecimalField(decimal_places=2, max_digits=12, default=0.0) 
    sub_total = models.DecimalField(decimal_places=2, max_digits=12, default=0.0) 
    price = models.DecimalField(decimal_places=2, max_digits=12, default=0.0) 
    country = models.CharField(max_length=100, null=True, blank=True)
    color = models.CharField(max_length=100, null=True, blank=True)
    size = models.CharField(max_length=100, null=True, blank=True)
    cart_id = models.CharField(max_length=1000, null=True, blank=True)
    qty = models.PositiveIntegerField(default=0, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.cart_id} - {self.product.title}"

class CartOrder(models.Model):
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='customer', blank=True)
    vendor = models.ManyToManyField(User, blank=True)
    
    sub_total = models.DecimalField(max_digits=12, default=0.00, decimal_places=2)
    shipping = models.DecimalField(max_digits=12, default=0.00, decimal_places=2)
    tax = models.DecimalField(max_digits=12, default=0.00, decimal_places=2)
    total = models.DecimalField(max_digits=12, default=0.00, decimal_places=2)
    payment_id = models.CharField(max_length=1000, null=True, blank=True)

    order_status = models.CharField(max_length=50, choices=ORDER_STATUS, default='Pending')
    payment_status = models.CharField(max_length=100, choices=PAYMENT_STATUS, default='Processing')

    #coupon
    initial_cost = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    saved  = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)

    #Bio data
    full_name = models.CharField(max_length=100, null=True, blank=True)
    email =  models.CharField(max_length=100, null=True, blank=True)
    mobile =  models.CharField(max_length=100, null=True, blank=True)

    #shipping Address
    address = models.CharField(max_length=100, null=True, blank=True)
    city =  models.CharField(max_length=100, null=True, blank=True)
    state =  models.CharField(max_length=100, null=True, blank=True)
    country =  models.CharField(max_length=100, null=True, blank=True)


    oid = ShortUUIDField(length=10, max_length=25, alphabet="abcdefghijklmnopqrstuvxyz")
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']
        verbose_name_plural = "Cart Order"

    def __str__(self):
        return self.oid
    
    def orderitem(self):
        return CartOrderItem.objects.filter(order=self)
    

class CartOrderItem(models.Model):
    order = models.ForeignKey(CartOrder, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    vendor = models.ForeignKey(User, on_delete=models.CASCADE)

    order_status = models.CharField(max_length=50, choices=ORDER_STATUS, default='Pending')
    
    price = models.DecimalField(max_digits=10, decimal_places=2)
    tax = models.DecimalField(max_digits=12, default=0.00, decimal_places=2)
    total = models.DecimalField(max_digits=12, default=0.00, decimal_places=2)
    sub_total = models.DecimalField(max_digits=12, default=0.00, decimal_places=2)
    shipping_amount= models.DecimalField(max_digits=10, decimal_places=2)
    
    color = models.CharField(max_length=100, null=True, blank=True)
    size = models.CharField(max_length=100, null=True, blank=True)
    qty = models.IntegerField(default=0)
    
    #coupon
    initial_cost = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    saved  = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    oid = ShortUUIDField(length=10, max_length=25, alphabet="abcdefghijklmnopqrstuvxyz")
    date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-date']

    # Method to return a formatted order ID
    def order_id(self):
        return f"Order ID #{self.order.oid}"

    def __str__(self):
        return self.oid


class ProductFaq(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=CASCADE)
    email = models.EmailField(null=True, blank=True)
    question = models.CharField(max_length=1000)
    answer = models.TextField(null=True, blank=True)
    active = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question
    
    class Meta:
        verbose_name_plural = "Product FAQs"

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
        return Profile.objects.get(user=self.user)
    
    class Meta:
        verbose_name_plural = "Review  & Rating"


@receiver(post_save, sender=Review)
def update_product_rating(sender, instance, **kwargs):
    if instance.product:
        instance.product.save()

class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.title

    class Meta:
        verbose_name_plural = "Wishlist"

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    order = models.ForeignKey(CartOrder, on_delete=models.SET_NULL, null=True, blank=True)
    order_item = models.ForeignKey(CartOrderItem, on_delete=models.SET_NULL, null=True, blank=True)
    seen = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.order:
            return self.order.oid
        else:
            return f"Notification - {self.pk}"
        
class Tax(models.Model):
    country = models.CharField(max_length=100)
    rate = models.IntegerField(default=5, help_text="Numbers added here are in percentage e.g 5%")
    active = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.country
    
    class Meta:
        verbose_name_plural = "Taxes"
        ordering = ['country']