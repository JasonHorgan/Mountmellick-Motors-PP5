from django.shortcuts import render, redirect, get_object_or_404
from .forms import FinanceApplicationForm
from products.models import Stock  
from django.contrib import messages

def finance_application(request, stock_id):
    """ Handle the finance application form submission for a specific car. """
    car = get_object_or_404(Stock, id=stock_id)  # Get the car object based on the stock_id

    if request.method == 'POST':
        form = FinanceApplicationForm(request.POST)
        if form.is_valid():
            finance_application = form.save(commit=False)
            finance_application.user = request.user  # Assign the logged-in user to the finance application
            finance_application.car = car  # Assign the selected car to the finance application
            finance_application.save()

            messages.success(request, 'Your finance application has been submitted successfully!')
            return redirect('finance_success', application_number=finance_application.application_number)  # Pass the application number
    else:
        form = FinanceApplicationForm()

    return render(request, 'finance/finance_application.html', {'form': form, 'car': car})



def finance_info(request):
    """ Display information about the finance process, including the 10% deposit. """
    return render(request, 'finance/finance_info.html')


def finance_success(request, application_number):
    """ Display the success message with the application number. """
    return render(request, 'finance/finance_success.html', {'application_number': application_number})

