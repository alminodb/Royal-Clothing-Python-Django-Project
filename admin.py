from django.contrib import admin
from .models import *



@admin.register(CategoryName)
class CategoryNameAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(SizeName)
class SizeNameAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    class ProductSizeAdmin(admin.StackedInline):
        model = ProductSize


    class ProductImagesAdmin(admin.StackedInline):
        model = ProductImages

    list_display = ('name', 'stock', 'price')
    list_editable = ('stock', 'price')
    inlines = [ProductSizeAdmin, ProductImagesAdmin]
