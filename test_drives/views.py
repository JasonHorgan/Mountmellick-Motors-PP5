from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import TestDriveForm

@login_required
@login_required  # Ensure the user is logged in
def book_test_drive(request):
    if request.method == 'POST':
        form = TestDriveForm(request.POST)
        if form.is_valid():
            test_drive = form.save(commit=False)  # Don't save yet
            test_drive.user = request.user  # Set the user field to the logged-in user
            test_drive.save()  # Now save the test drive with the user field populated
            return redirect('test_drive_confirmation')  # Redirect to the confirmation page
    else:
        form = TestDriveForm()

    return render(request, 'test_drives/book_test_drive.html', {'form': form})

def test_drive_confirmation(request):
    return render(request, 'test_drives/confirmation.html')
