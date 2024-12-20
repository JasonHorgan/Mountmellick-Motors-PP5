from django.shortcuts import render, get_object_or_404
from .models import Stock

# Create your views here.

def all_stock (request):
    """ A view to show all stock, including sorting and search queries """

    stock = Stock.objects.all()

    context = {
        'stock': stock,
    }

    return render(request, 'products/products.html', context)

def product_detail (request, stock_id):
    """ A view to show individual stock details """

    stock = get_object_or_404(Stock, pk=stock_id)

    context = {
        'stock': stock,
    }

    return render(request, 'products/product_detail.html', context)