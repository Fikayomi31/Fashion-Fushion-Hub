from django.contrib import admin
from .models import User, CustomerProfile, VendorProfile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'full_name', 'date']
 
admin.site.register(User)
admin.site.register(CustomerProfile, ProfileAdmin)
admin.site.register(VendorProfile, ProfileAdmin)
 
 