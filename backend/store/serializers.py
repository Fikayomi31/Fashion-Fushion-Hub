from rest_framework import serializer

from store.models import Category, SubCategory ,Product, Cart, Order, Variant, SubCategory, OrderItem, Review, Coupon, Gallery, VariantItem, Variant
class CategorySerialier(serializer.ModelSerializer):
    
    class Meta:
        models = Category
        fields = '__all__'

class SubCategorySerializer(serializer.ModelSerializer):
    
    class Meta:
        models = SubCategory
        fields = '__all__'

class ProductSerializer(serializer.ModelSerializer):

    class Meta:
        models = Product
        fields = '__all__'

class VariantSerializer(serializer.ModelSerializer):

    class Meta:
        models = Variant
        fields = '__all__'

class VariantItemSerializer(serializer.ModelSerializer):

    class Meta:
        models = VariantItem
        fields = '__all__'

class GallerySerializer(serializer.ModelSerializer):

    class Meta:
        models = Gallery
        fields = '__all__'

class CouponSerializer(serializer.ModelSerializer):

    class Meta:
        models = Coupon
        fields = '__all__'

class CartSerializer(serializer.ModelSerializer):

    class Meta:
        models = Cart
        fields = '__all__'

class OrderSerializer(serializer.ModelSerializer):

    class Meta:
        models = Order
        fields = '__all__'

class OrderItemSerializer(serializer.ModelSerializer):

    class Meta:
        models = OrderItem
        fields = '__all__'

class ReviewSerializer(serializer.ModelSerializer):

    class Meta:
        models = Review
        fields = '__all__'