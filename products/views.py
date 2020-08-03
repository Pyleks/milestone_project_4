from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.


def all_products(request):
    """ all Products page view """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)



def product_detail(request, product_id):
    """ Showing individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'products': product,
    }

    return render(request, 'products/product_detail.html', context)
