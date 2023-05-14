from django.contrib import admin
from products.models import ProductCategory, Product, Basket

# Register your models here.
admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(Basket)