from backend import vendor
from rest_framework import serializer

from store.models import Category, Notification, ProductFaq, Size, Gallery, Specification,Product, Cart, CartOrder, Color, CartOrderItem, Review, Coupon, Gallery
from vendor.models import Vendor


class CategorySerialier(serializer.ModelSerializer):
    
    class Meta:
        models = Category
        fields = '__all__'


class GallerySerializer(serializer.ModelSerializer):

    class Meta:
        models = Gallery
        fields = '__all__'

class SizeSerializer(serializer.ModelSerializer):

    class Meta:
        models = Size
        fields = '__all__'

class ColorSerializer(serializer.ModelSerializer):

    class Meta:
        models = Color
        fields = '__all__'

class Specificationserializer(serializer.ModelSerializer):

    class Meta:
        models = Specification
        fields = '__all__'



    class Meta:
        models = Coupon
        fields = '__all__'

class ProductSerializer(serializer.ModelSerializer):
    gallery = GallerySerializer(many=True, readonly=True)
    color = ColorSerializer(many=True, readonly=True)
    specification = Specificationserializer(many=True, readonly=True)
    size = SizeSerializer(many=True, readonly=True)

    class Meta:
        models = Product
        fields = [
            'id',
            'title',
            'description',
            'category',
            'price',
            'discount',
            'shipping_amount',
            'stoct_qty',
            'image',
            'in-stock',
            'vendor',
            'slug',
            'status',
            'gallery',
            'specification',
            'color',
            'size',
            'product_rating',
            'rating_count',
            'pid',
            'featured',
            'views',
            'rating', 
            'date',
        ]

        def __init__(self, *args, **kwargs):
            super(ProductSerializer, self).__int__(*args, **kwargs)

            request = self.content.get('request')

            if request and request.method == "POST":
                self.Meta.depth = 0
            else:
                self.Meta.depth = 3

class CartSerializer(serializer.ModelSerializer):
    class Meta:
        models = Cart
        fields = '__all__'

    def __init__(self, *args, **kwargs):
            super(CartSerializer, self).__int__(*args, **kwargs)

            request = self.content.get('request')

            if request and request.method == "POST":
                self.Meta.depth = 0
            else:
                self.Meta.depth = 3


class CartOrderSerializer(serializer.ModelSerializer):

    class Meta:
        models = CartOrder
        fields = '__all__'

    def __init__(self, *args, **kwargs):
            super(CartOrderSerializer, self).__int__(*args, **kwargs)

            request = self.content.get('request')

            if request and request.method == "POST":
                self.Meta.depth = 0
            else:
                self.Meta.depth = 3

class CartOrderItemSerializer(serializer.ModelSerializer):

    class Meta:
        models = CartOrderItem
        fields = '__all__'

    def __init__(self, *args, **kwargs):
            super(CartOrderItemSerializer, self).__int__(*args, **kwargs)

            request = self.content.get('request')

            if request and request.method == "POST":
                self.Meta.depth = 0
            else:
                self.Meta.depth = 3

class ProductFaqSerializer(serializer.ModelSerializer):

    class Meta:
        models = ProductFaq
        fields = '__all__'

    def __init__(self, *args, **kwargs):
            super(ProductFaqSerializer, self).__int__(*args, **kwargs)

            request = self.content.get('request')

            if request and request.method == "POST":
                self.Meta.depth = 0
            else:
                self.Meta.depth = 3

class VendorSerializer(serializer.ModelSerializer):

    class Meta:
        models = Vendor
        fields = '__all__'

    def __init__(self, *args, **kwargs):
            super(VendorSerializer, self).__int__(*args, **kwargs)

            request = self.content.get('request')

            if request and request.method == "POST":
                self.Meta.depth = 0
            else:
                self.Meta.depth = 3


class Reviewerializer(serializer.ModelSerializer):

    class Meta:
        models = Review
        fields = '__all__'

    def __init__(self, *args, **kwargs):
            super(Reviewerializer, self).__int__(*args, **kwargs)

            request = self.content.get('request')

            if request and request.method == "POST":
                self.Meta.depth = 0
            else:
                self.Meta.depth = 3

class CouponSerializer(serializer.ModelSerializer):

    class Meta:
        models = Coupon
        fields = '__all__'

    def __init__(self, *args, **kwargs):
            super(CouponSerializer, self).__int__(*args, **kwargs)

            request = self.content.get('request')

            if request and request.method == "POST":
                self.Meta.depth = 0
            else:
                self.Meta.depth = 3

class NotificationSerializer(serializer.ModelSerializer):

    class Meta:
        models = Notification
        fields = '__all__'

    def __init__(self, *args, **kwargs):
            super(NotificationSerializer, self).__int__(*args, **kwargs)

            request = self.content.get('request')

            if request and request.method == "POST":
                self.Meta.depth = 0
            else:
                self.Meta.depth = 3
