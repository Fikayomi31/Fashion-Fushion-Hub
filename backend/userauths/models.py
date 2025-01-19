from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.db.models.signals import post_save

USER_TYPE = (
    ('Customer', 'Customer'),
    ('Vendor', 'Vendor')
)

class User(AbstractUser):
    username = models.CharField(unique=True, max_length=100)
    email = models.EmailField(unique=True)
    full_name = models.CharField(unique=True, max_length=100)
    otp = models.CharField(max_length=250, null=True, blank=True)
    user_type = models.CharField(max_length=100, choices=USER_TYPE, default='Customer')
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    def __str__(self):
        return self.email
    
    def save(self, *args, **kwargs):
        email_username, _ = self.email.split("@")
        if not self.full_name:
            self.full_name = email_username
        if not self.username:
            self.username = email_username
        super(User, self).save(*args, **kwargs)
        
        
class CustomerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='user_folder', default="default-user.jpg")
    full_name = models.CharField(max_length=100)
    address = models.CharField(max_length=150)
    bio = models.CharField(max_length=150)
    phone_number = PhoneNumberField(region='NG')
    date =models.DateField(auto_now=False, auto_now_add=True)
    
    def __str__(self):
        if self.full_name:
            return str(self.full_name)
        else:
            return str(self.user.full_name)
        
    
    def save(self, *args, **kwargs):
        if self.full_name == "" or self.full_name == None:
            self.full_name  == self.user.username
        super(CustomerProfile, self).save(*args, ** kwargs)
        
        
        
class VendorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='user_folder', default="default-user.jpg")
    full_name = models.CharField(max_length=100)
    address = models.CharField(max_length=150)
    bio = models.CharField(max_length=150)
    phone_number = PhoneNumberField(region='NG')
    date =models.DateField(auto_now=False, auto_now_add=True)
    
    def __str__(self):
        if self.full_name:
            return str(self.full_name)
        else:
            return str(self.user.full_name)
        
    
    def save(self, *args, **kwargs):
        if self.full_name == "" or self.full_name == None:
            self.full_name  == self.user.username
        super(VendorProfile, self).save(*args, ** kwargs)
        

# Signals to ensure profile is created for every user
def create_user_profile(sender, instance, created, **kwargs):
    """Automatically create profile when a user is created."""
    if created:
        if instance.user_type == 'Customer':
            CustomerProfile.objects.create(user=instance)
        elif instance.user_type == 'Vendor':
            VendorProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)
