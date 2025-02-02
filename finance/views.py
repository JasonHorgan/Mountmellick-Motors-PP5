from django.shortcuts import render, redirect
from .forms import FinanceApplicationForm
from django.contrib import messages

def finance_application(request):
    """ Handle the finance application form submission. """
    
    if request.method == 'POST':
        form = FinanceApplicationForm(request.POST)
        if form.is_valid():
            finance_application = form.save(commit=False)
            finance_application.user = request.user  
            finance_application.save()

            messages.success(request, 'Your finance application has been submitted successfully!')
            return redirect('finance_success', application_number=finance_application.application_number) 
    else:
        form = FinanceApplicationForm()

    return render(request, 'finance/finance_application.html', {'form': form})

def finance_info(request):
    """ Display information about the finance process. """
    return render(request, 'finance/finance_info.html')

def finance_success(request, application_number):
    """ Display the success message with the application number. """
    return render(request, 'finance/finance_success.html', {'application_number': application_number})
