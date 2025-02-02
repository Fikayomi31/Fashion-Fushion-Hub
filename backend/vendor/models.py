from django.db import models
from shortuuid.django_fields import ShortUUIDField
from userauths.models import User
from django.utils.text import slugify


NOTIFICATION_TYPE = (
    ('New Order', 'New Order'),
    ('New Review', 'New Review'),
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

TYPE = (
    ('New Order', 'New Order'),
    ('Item Shipped', 'Item Shipped'),
    ('Item Delivered', 'Item Delivered')
)


class Vendor(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, related_name='vendor')
    image = models.ImageField(upload_to='vendor/images', default='vendor.jpg', blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, max_length=500)
    mobile = models.CharField(max_length=100, help_text='Shop Mobile Number', null=True, blank=True)
    active = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Vendors'
        ordering = ['-date']


    def __str__(self):
        return str(self.store_name)
    
    def save(self, *args, **kwargs):
        if self.slug == "" or self.slug == None:
            self.slug = slugify(self.title)
        super(Vendor, self).save(*args, **kwargs)


"""class Payment(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.SET_NULL, null=True, blank=True)
    item = models.ForeignKey(OrderItem, on_delete=models.SET_NULL, null=True, related_name='order_item')
    amount = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    payment_id = ShortUUIDField(unique=True, length=6, max_length=10, alphabet='1234567890')
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.vendor)
    
    class Meta:
        ordering = ['-date']


class BankAccount(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.SET_NULL, null=True)
    account_type = models.CharField(max_length=50, choices=PAYMENT_METHOD, null=True, blank=True)
    bank_name = models.CharField(max_length=500)
    account_number = models.CharField(max_length=500)
    account_name = models.CharField(max_length=100)
    bank_code = models.CharField(max_length=100, null=True, blank=True)
    stripe_id = models.CharField(max_length=100, null=True, blank=True)
    paypal_address = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Bank Account'

    def __str__(self):
        return self.bank_name
    

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='vendor_notification')
    type = models.CharField(max_length=100, choices=TYPE, default=None)
    seen = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    order = models.ForeignKey(OrderItem, on_delete=models.CASCADE, null=True, blank=True)


    class Meta:
        verbose_name_plural = 'Notification'

    def __str__(self):
        return self.type
        """