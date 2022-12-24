from rest_framework import serializers

from .models import *


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class FirmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Firm
        fields = "__all__"


class CategorySerializer(serializers.Serializer):
    category_name = serializers.CharField(max_length=44)

    def create(self, validate_date):
        category = Category.objects.create(
            category_name=validate_date['category_name']
        )
        return category

    def update(self, instance, validate_date):
        instance.category_name = validate_date['category_name']
        instance.save()
        return instance

