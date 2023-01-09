from django.contrib import admin
from .models import Customer,Product,Retailer
# Register your models here.

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display=['id','name','email','address']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=['id','name','quantity','price']

@admin.register(Retailer)
class RetailerAdmin(admin.ModelAdmin):
    list_display=['id','name','email','address']