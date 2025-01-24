from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models.functions import Lower
from .models import Stock
from .forms import ProductForm


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

def add_product(request):
    """ Add a product to the store """
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()  # Save the product and get the instance
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))  # Pass product.id
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()
        
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def edit_product(request, stock_id):
    """ Edit a product in the store """
    product = get_object_or_404(Stock, pk=stock_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.make} {product.model}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)

def delete_product(request, stock_id):
    """ Delete a product from the store """
    product = get_object_or_404(Stock, pk=stock_id)  # Correct variable name: product
    product.delete()  # Call delete() on product, not stock
    messages.success(request, 'Product deleted!')
    return redirect(reverse('stock'))  # Ensure this matches the name of the all_stock view
