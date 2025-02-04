from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import TestDriveForm
from .models import TestDrive

@login_required
def book_test_drive(request):
    if request.method == "POST":
        form = TestDriveForm(request.POST)
        if form.is_valid():
            test_drive = form.save(commit=False)
            test_drive.user = request.user
            test_drive.save()
            return redirect("test_drive_confirmation")
    else:
        form = TestDriveForm()

    return render(request, "test_drives/book_test_drive.html", {"form": form})

def test_drive_confirmation(request):
    return render(request, "test_drives/confirmation.html")

@login_required
def edit_test_drive(request, test_drive_id):
    test_drive = get_object_or_404(TestDrive, id=test_drive_id, user=request.user)
    if request.method == "POST":
        form = TestDriveForm(request.POST, instance=test_drive)
        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        form = TestDriveForm(instance=test_drive)

    return render(request, "test_drives/edit_test_drive.html", {"form": form, "test_drive": test_drive})

@login_required
def delete_test_drive(request, test_drive_id):
    test_drive = get_object_or_404(TestDrive, id=test_drive_id, user=request.user)
    if request.method == "POST":
        test_drive.delete()
        return redirect("profile")

    return render(request, "test_drives/delete_test_drive.html", {"test_drive": test_drive})