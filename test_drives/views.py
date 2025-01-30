from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import TestDriveForm


@login_required  
def book_test_drive(request):
    if request.method == 'POST':
        form = TestDriveForm(request.POST)
        if form.is_valid():
            test_drive = form.save(commit=False)  
            test_drive.user = request.user  
            test_drive.save()  
            return redirect('test_drive_confirmation')  
    else:
        form = TestDriveForm()

    return render(request, 'test_drives/book_test_drive.html', {'form': form})

def test_drive_confirmation(request):
    return render(request, 'test_drives/confirmation.html')
