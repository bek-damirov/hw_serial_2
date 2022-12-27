from rest_framework import serializers

from .models import Product, Category, Firm


class ProductSerializer(serializers.Serializer):
    product_name = serializers.CharField(max_length=55)
    price = serializers.IntegerField()
    firm = serializers.IntegerField()
    category = serializers.IntegerField()

    def create(self, validate_date):
        product = Product.objects.create(
            product_name=validate_date['product_name'],
            price=validate_date['price'],
            firm=validate_date['firm'],
            category=validate_date['category']
        )
        return product

    def update(self, instance, validate_date):
        instance.product_name = validate_date['product_name']
        instance.price = validate_date['price']
        instance.firm = validate_date['firm']
        instance.category = validate_date['category']
        instance.save()
        return instance


class FirmSerializer(serializers.Serializer):
    firm_name = serializers.CharField(max_length=77)
    firm_office = serializers.CharField(max_length=55)

    def create(self, validate_date):
        firm = Firm.objects.create(
            firm_name=validate_date['firm_name'],
            firm_office=validate_date['firm_office']
        )
        return firm

    def update(self, instance, validate_date):
        instance.firm_name = validate_date['firm_name']
        instance.firm_office = validate_date['firm_office']
        instance.save()
        return instance


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


# class ProductSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Product
#         fields = "__all__"
#
#
# class FirmSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Firm
#         fields = "__all__"
