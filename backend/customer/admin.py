"""from django.contrib import admin
#import/export model data functionality to your Django Admin models.
from import_export.admin import ImportExportModelAdmin
from customer import models as customer_models

class AddressAdmin(ImportExportModelAdmin):
    list_display = ['user', 'full_name']

class WishlistAdmin(admin.ModelAdmin):
    list_display = ['user', 'product']

class NotificationAdmin(admin.ModelAdmin):
    list_display = ['user', 'type', 'seen', 'date']

admin.site.register(customer_models.Address, AddressAdmin)
admin.site.register(customer_models.Wishlist, WishlistAdmin)
admin.site.register(customer_models.Notification, NotificationAdmin)

"""