from django.urls import path
from . import views

urlpatterns = [
    path("", views.all_stock, name="stock"),
    path("<int:stock_id>/", views.product_detail, name="product_detail"),
    path("add/", views.add_product, name="add_product"),
    path("edit/<int:stock_id>/", views.edit_product, name="edit_product"),
    path(
        "delete/<int:stock_id>/", views.delete_product, name="delete_product"
    ),
]
