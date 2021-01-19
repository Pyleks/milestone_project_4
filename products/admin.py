# Code Mostly from Code Insitute

from django.contrib import admin
from .models import Product, Category


# Register your models here.
# Lists the products by the categories below in admin center.
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'brand',
        'rating',
        'image',

    )

    # This allow the products to be ordered by SKU, can be changed with any of the ones above.
    ordering = ('sku',)


# List the friendly name first and the name after.
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


# Runs the classes above to display the edited admin view
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
