# finance/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('finance-info/', views.finance_info, name='finance_info'),
    path('finance-application/<int:stock_id>/', views.finance_application, name='finance_application'),
    path('finance-success/<str:application_number>/', views.finance_success, name='finance_success'),
]
