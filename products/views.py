from django.shortcuts import render
from .models import Stock

# Create your views here.

def all_stock (request):
    """ A view to show all stock, including sorting and search queries """

    stock = Stock.objects.all()

    context = {
        'Stock_items': stock,
    }

    return render(request, 'products/products.html', context)