from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserProfileForm
from checkout.models import Order
from test_drives.models import TestDrive  # Import TestDrive model


@login_required
def profile(request):
    """ Display the user's profile, order history, and test drives. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')

    form = UserProfileForm(instance=profile)
    orders = profile.orders.all()
    test_drives = TestDrive.objects.filter(user=request.user)  # Fetch user's test drives

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'test_drives': test_drives,  # Pass test drives to template
        'on_profile_page': True
    }

    return render(request, template, context)


def order_history(request, order_number):
    """ Display the user's order history details. """
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)
