import csv

from rest_framework import serializers

from api.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'




class RetreiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['product_name', 'category', 'discounted_price', 'actual_price', 'rating', 'rating_count']

class SearchBySerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=['product_name', 'discounted_price', 'actual_price', 'rating', 'category','rating_count','about_product','review_content','product_link']

class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=['discounted_price', 'category']

