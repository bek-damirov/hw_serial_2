from django.db import models


class Product(models.Model):
    product_name = models.CharField(max_length=55)
    price = models.IntegerField()
    firm = models.IntegerField()
    category = models.IntegerField()

    def __str__(self):
        return self.product_name


class Firm(models.Model):
    firm_name = models.CharField(max_length=77)
    firm_office = models.CharField(max_length=55)

    def __str__(self):
        return self.firm_name


class Category(models.Model):
    category_name = models.CharField(max_length=44)

    def __str__(self):
        return self.category_name

