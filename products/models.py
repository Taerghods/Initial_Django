from django.db import models

class Category(models.Model):
    name = models.CharField('دسته‌بندی', max_length=100, unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField('نام محصول', max_length=200)
    price = models.IntegerField('قیمت محصول')
    image = models.ImageField('تصویر', upload_to='products_images/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product_set')

    def __str__(self):
        return self.name