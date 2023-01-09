from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    products = models.ManyToManyField("Product")

    def __str__(self):
        return self.name

class Product(models.Model):

    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.IntegerField()
    retailer= models.ForeignKey("Retailer",on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Retailer(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name

