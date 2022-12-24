from django.shortcuts import render

from rest_framework import generics
from rest_framework import viewsets
from .models import *
from .serializers import ProductSerializer, FirmSerializer, CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class FirmCreateListView(generics.ListCreateAPIView):
    queryset = Firm.objects.all()
    serializer_class = FirmSerializer


class FirmRetrieveUpdateDestroyApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Firm.objects.all()
    serializer_class = FirmSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
