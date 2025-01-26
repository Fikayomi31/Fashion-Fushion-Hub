from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import CASCADE
from phonenumber_field.modelfields import PhoneNumberField

USER_TYPE = (
    ('Customer', 'Customer'),
    ('Vendor', 'Vendor')
)

class User(AbstractUser):
    username = models.CharField(unique=True, max_length=100)
    email = models.EmailField(unique=True)
    otp = models.CharField(max_length=250, null=True, blank=True)
    refresh_token = models.CharField(max_length=250, null=True, blank=True)
    user_type = models.CharField(max_length=100, choices=USER_TYPE, default='Customer')
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    def __str__(self):
        return self.email
    
    def save(self, *args, **kwargs):
        email_username, _ = self.email.split("@")
        if not self.username:
            self.username = email_username
        super(User, self).save(*args, **kwargs)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=CASCADE)
    image = models.ImageField(upload_to='images', default='user.jpg', null=True, blank=True)
    full_name = models.CharField(max_length=100, null=True, blank=True)
    number = models.CharField(max_length=100, null=True, blank=True)
    user_type = models.CharField(max_length=200, choices=USER_TYPE, default="Customer")

    def __str__(self):
        return self.user.username
    
    def save(self, *args, **kwargs):
        if self.full_name == "" or self.full_name is None:
            self.full_name = self.user.username
        super(Profile, self).save(*args, **kwargs)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
