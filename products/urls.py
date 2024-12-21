from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_stock, name='stock'),
    path('<stock_id>', views.product_detail, name='product_detail'),
]