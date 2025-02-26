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
    list_display = [ 'title', 'price', 'shipping_amount', 'stock_qty', 'in_stock', 'vendor', 'featured', 'slug']
    search_fields =['title']
    list_filter = ['date']
    inlines = [GalleryInline, SpecificationInline, SizeInline, ColorInline]


class CartAdmin(admin.ModelAdmin):
    list_display = ['cart_id', 'product', 'user', 'qty', 'price', 'total', 'date']
    search_fields = ['cart_id', 'product__name', 'user__username']
    list_filter = ['date', 'product']

class CouponAdmin(admin.ModelAdmin):
    list_display = ['code', 'vendor', 'discount']
    search_fields = ['code', 'vendor__name']

class CartOrderAdmin(admin.ModelAdmin):
    list_display = ['order_id', 'customer', 'total', 'payment_status', 'order_status', 'date']
    search_fields = ['order_id', 'customer__username']
    list_editable = ['payment_status', 'order_status']

class CartOrderItemAdmin(admin.ModelAdmin):
    list_display = ['oid', 'order', 'product', 'qty', 'price', 'total']
    search_fields = ['oid', 'order__order_id', 'product__name']
    list_filter = ['order__date']

class ReviewAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'rating', 'active', 'date']
    search_fields = ['user__username', 'product__name']
    list_filter = ['active', 'rating']

admin.site.register(store_model.Category, CategoryAdmin)
admin.site.register(store_model.Product, ProductAdmin)
admin.site.register(store_model.Cart, CartAdmin)
admin.site.register(store_model.CartOrder, CartOrderAdmin)
admin.site.register(store_model.CartOrderItem,CartOrderItemAdmin)
admin.site.register(store_model.Tax)
