from django.urls import path
from . import views

urlpatterns = [
    path('book/', views.book_test_drive, name='book_test_drive'),
    path('confirmation/', views.test_drive_confirmation, name='test_drive_confirmation'),
]
