from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_stock, name='stock'),
    path('<int:stock_id>/', views.product_detail, name='product_detail'),
    path('add/', views.add_product, name='add_product'),
]