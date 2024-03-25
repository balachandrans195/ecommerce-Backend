from rest_framework import serializers

from .models import Customer, Rating, Category, Product, Cart


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model= Customer
        fields= '__all__'
        
        
class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model= Rating
        fields= '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'
