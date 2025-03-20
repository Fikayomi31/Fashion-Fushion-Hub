from django.db import models
from shortuuid.django_fields import ShortUUIDField
from userauths.models import User
from django.utils.text import slugify


class Vendor(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, related_name='vendor')
    image = models.ImageField(upload_to='vendor/images', default='vendor.jpg', blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    mobile = models.CharField(max_length=100, help_text='Shop Mobile Number', null=True, blank=True)
    active = models.BooleanField(default=False)
    slug = models.SlugField(blank=True, null=True)

    
    class Meta:
        verbose_name_plural = 'Vendors'
        ordering = ['-date']

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        if self.slug == "" or self.slug == None: 
            self.slug = slugify(self.name)
            
        super(Vendor, self).save(*args, **kwargs)