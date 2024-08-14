from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView


app_name = "bicicletas"
urlpatterns = [
    path("", views.index, name="index"),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path("cliente", views.cliente, name="cliente"),
    path("cliente/<int:cliente_id>/", views.info_cliente, name="info_cliente"),
    path("add_cliente/", views.add_cliente, name="add_cliente"),
    path("edit_cliente/<int:id>/", views.edit_cliente, name="edit_cliente"),
    path("delete_cliente/<int:id>/", views.delete_cliente, name="delete_cliente"),
    path("category", views.category, name="category"),
    path("category/<int:category_id>/", views.info_category, name="info_category"),
    path("add_category/", views.add_category, name="add_category"),
    path("edit_category/<int:id>/", views.edit_category, name="edit_category"),
    path("delete_category/<int:id>/", views.delete_category, name="delete_category"),
    path("product", views.product, name="product"),
    path("product/<int:product_id>/", views.info_product, name="info_product"),
    path("add_product/", views.add_product, name="add_product"),
    path("edit_product/<int:id>/", views.edit_product, name="edit_product"),
    path("delete_product/<int:id>/", views.delete_product, name="delete_product"),
    path("venta", views.venta, name="venta"),
    path("venta/<int:sale_id>/", views.info_venta, name="info_venta"),
    path("add_venta/", views.add_venta, name="add_venta"),
    path("edit_venta/<int:id>/", views.edit_venta, name="edit_venta"),
    path("delete_venta/<int:id>/", views.delete_venta, name="delete_venta"),
]