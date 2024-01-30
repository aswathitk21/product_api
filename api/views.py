from django.db.models import Avg
from django.shortcuts import render

# Create your views here.
from rest_framework import filters, status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
import csv

from api.models import Product
from api.serializer import ProductSerializer, RetreiveSerializer, SearchBySerializer

from api.serializer import DiscountSerializer


class ProductView(APIView):
    def get(self, request):
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)


class RetreiveAPI(APIView):
    def get(self, request, id, format=None):
        queryset = Product.objects.all().filter(product_id=id)
        serializer = RetreiveSerializer(queryset, many=True)
        return Response(serializer.data)


class TopProductApi(APIView):
    def get(self, request):
        queryset = Product.objects.all().order_by('rating')[:5]
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)


class AverageDiscount(APIView):
    def get(self, request):
        values = Product.objects.values('category').distinct()
        print(values)
        result=[]
        for value in values:
            category_name = value['category']
            queryset = Product.objects.filter(category=category_name)
            avg = queryset.aggregate(avdg_discount=Avg('discount_percentage'))
            data = {
                'category': category_name,
                'average': avg,
            }
            result.append(data)
        return Response(result)


class SearchAByCategory(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = SearchBySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['category']
