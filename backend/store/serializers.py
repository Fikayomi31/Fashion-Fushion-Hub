from rest_framework import serializers

from store.models import Category, Notification, ProductFaq, Size, Gallery, Specification,Product, Cart, CartOrder, Color, CartOrderItem, Review, Coupon, Gallery
from vendor.models import Vendor


class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = '__all__'

class GallerySerializer(serializers.ModelSerializer):

    class Meta:
        model = Gallery
        fields = '__all__'

class SizeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Size
        fields = '__all__'

class ColorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Color
        fields = '__all__'

class Specificationserializer(serializers.ModelSerializer):

    class Meta:
        model = Specification
        fields = '__all__'




class ProductSerializer(serializers.ModelSerializer):
    gallery = GallerySerializer(many=True, read_only=True)
    color = ColorSerializer(many=True, read_only=True)
    specification = Specificationserializer(many=True, read_only=True)  # Fixed casing
    size = SizeSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = [
            'id',
            'title',
            'description',
            'category',
            'price',
            'discount',
            'shipping_amount',
            'stock_qty',
            'image',
            'in_stock',
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
    
    def __init__(self, *args, **kwargs):  # Moved to correct indentation
        super(ProductSerializer, self).__init__(*args, **kwargs)  # Fixed method name

        request = self.context.get('request')  # Fixed attribute access

        if request and request.method == "POST":
            self.Meta.depth = 0
        else:
            self.Meta.depth = 3


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'

    def __init__(self, *args, **kwargs):
            super(CartSerializer, self).__init__(*args, **kwargs)

            request = self.context.get('request')

            if request and request.method == "POST":
                self.Meta.depth = 0
            else:
                self.Meta.depth = 3

class CartOrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = CartOrderItem
        fields = '__all__'

    def __init__(self, *args, **kwargs):
            super(CartOrderItemSerializer, self).__init__(*args, **kwargs)

            request = self.context.get('request')

            if request and request.method == "POST":
                self.Meta.depth = 0
            else:
                self.Meta.depth = 3


class CartOrderSerializer(serializers.ModelSerializer):
    orderitem = CartOrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = CartOrder
        fields = '__all__'

    def __init__(self, *args, **kwargs):
            super(CartOrderSerializer, self).__init__(*args, **kwargs)

            request = self.context.get('request')

            if request and request.method == "POST":
                self.Meta.depth = 0
            else:
                self.Meta.depth = 3
class ProductFaqSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductFaq
        fields = '__all__'

    def __init__(self, *args, **kwargs):
            super(ProductFaqSerializer, self).__init__(*args, **kwargs)

            request = self.context.get('request')

            if request and request.method == "POST":
                self.Meta.depth = 0
            else:
                self.Meta.depth = 3

class VendorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vendor
        fields = '__all__'

    def __init__(self, *args, **kwargs):
            super(VendorSerializer, self).__init__(*args, **kwargs)

            request = self.context.get('request')

            if request and request.method == "POST":
                self.Meta.depth = 0
            else:
                self.Meta.depth = 3

class Reviewerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'

    def __init__(self, *args, **kwargs):
            super(Reviewerializer, self).__init__(*args, **kwargs)

            request = self.context.get('request')

            if request and request.method == "POST":
                self.Meta.depth = 0
            else:
                self.Meta.depth = 3

class CouponSerializer(serializers.ModelSerializer):

    class Meta:
        model = Coupon
        fields = '__all__'

    def __init__(self, *args, **kwargs):
            super(CouponSerializer, self).__init__(*args, **kwargs)

            request = self.context.get('request')

            if request and request.method == "POST":
                self.Meta.depth = 0
            else:
                self.Meta.depth = 3

class NotificationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Notification
        fields = '__all__'

    def __init__(self, *args, **kwargs):
            super(NotificationSerializer, self).__init__(*args, **kwargs)

            request = self.context.get('request')

            if request and request.method == "POST":
                self.Meta.depth = 0
            else:
                self.Meta.depth = 3
