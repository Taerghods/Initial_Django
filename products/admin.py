from django.contrib import admin
from products.models import Category, Product

# Usename: admin1
# Email: admin1@gmail.com
# Password: gmail.com

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'image', 'category']
    list_filter = ['category']
    search_fields = ['name']
admin.site.register(Product, ProductAdmin)