from django.urls import path
from . import views

urlpatterns = [
    path("book/", views.book_test_drive, name="book_test_drive"),
    path(
        "confirmation/",
        views.test_drive_confirmation,
        name="test_drive_confirmation",
    ),
    path(
        "edit/<int:test_drive_id>/",
        views.edit_test_drive,
        name="edit_test_drive",
    ),
    path(
        "delete/<int:test_drive_id>/",
        views.delete_test_drive,
        name="delete_test_drive",
    ),
]
