from django.db import models


class CategoryName(models.Model):
    name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    category = models.ForeignKey(CategoryName, on_delete=models.CASCADE)
    name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ManyToManyField(Category)
    name = models.CharField(max_length=128)
    stock = models.IntegerField()
    price = models.FloatField()

    def __str__(self):
        return self.name


class SizeName(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class ProductSize(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    size = models.ForeignKey(SizeName, on_delete=models.CASCADE)

    def __str__(self):
        return self.product.name


class ProductImages(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.product.name
