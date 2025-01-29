from django.contrib import admin
from store import models as store_model


class GalleryInline(admin.TabularInline):
    model = store_model.Gallery
    extra = 0

class SpecificationInline(admin.TabularInline):  # You can also use admin.StackedInline
    model = store_model.Specification
    extra = 0   

class ColorInline(admin.TabularInline):
    model = store_model.Color
    extra = 0


class SizeInline(admin.TabularInline):
    model = store_model.Size
    extra = 0

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'image']
    list_editable = ['image']
    prepopulated_fields = {'slug': ('title',)}


class ProductAdmin(admin.ModelAdmin):
    list_display = [ 'title', 'price', 'shipping_amount', 'stock_qty', 'in_stock', 'vendor', 'featured']
    search_fields =['title']
    list_filter = ['date']
    inlines = [GalleryInline, SpecificationInline, SizeInline, ColorInline]



"""class GalleryAdmin(admin.ModelAdmin):
    list_display = ['product', 'gallery_id']
    search_fields = ['product__name', 'gallery_id']

class CartAdmin(admin.ModelAdmin):
    list_display = ['cart_id', 'product', 'user', 'qty', 'price', 'total', 'date']
    search_fields = ['cart_id', 'product__name', 'user__username']
    list_filter = ['date', 'product']

class CouponAdmin(admin.ModelAdmin):
    list_display = ['code', 'vendor', 'discount']
    search_fields = ['code', 'vendor__name']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_id', 'customer', 'total', 'payment_status', 'order_status', 'payment_method', 'date']
    search_fields = ['order_id', 'customer__username']
    list_editable = ['payment_status', 'order_status', 'payment_method']

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['item_id', 'order', 'product', 'qty', 'price', 'total']
    search_fields = ['item_id', 'order__order_id', 'product__name']
    list_filter = ['order__date']

class ReviewAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'rating', 'active', 'date']
    search_fields = ['user__username', 'product__name']
    list_filter = ['active', 'rating']"""

admin.site.register(store_model.Category, CategoryAdmin)
admin.site.register(store_model.Product, ProductAdmin)

"""admin.site.register(store_model.Gallery, GalleryAdmin)
admin.site.register(store_model.Cart, CartAdmin)
admin.site.register(store_model.Order, OrderAdmin)
admin.site.register(store_model.Coupon, CouponAdmin)
admin.site.register(store_model.OrderItem, OrderItemAdmin)
admin.site.register(store_model.Review, ReviewAdmin)
"""