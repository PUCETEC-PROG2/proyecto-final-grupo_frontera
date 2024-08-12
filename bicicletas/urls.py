from django.urls import path
from . import views

app_name = "bicicletas"
urlpatterns = [
    path("", views.index, name="index"),
    
    path('login/', views.CustomLoginView.as_view(), name='login'),
    
    path("cliente", views.cliente, name="cliente"),
    path("cliente/<int:cliente_id>/", views.info_cliente, name="info_cliente"),
    path("add_cliente/", views.add_cliente, name="add_cliente"),
    path("edit_cliente/<int:id>/", views.edit_cliente, name="edit_cliente"),
    path("delete_cliente/<int:id>/", views.delete_cliente, name="delete_cliente"),
    #categoria path
    path("categoria", views.categoria, name="categoria"),
    path("categoria/<int:categoria_id>/", views.info_categoria, name="info_categoria"),
    path("add_categoria/", views.add_categoria, name="add_categoria"),
    path("edit_categoria/<int:id>/", views.edit_categoria, name="edit_categoria"),
    path("delete_categoria/<int:id>/", views.delete_categoria, name="delete_categoria"),
    #producto path
    path("producto", views.producto, name="producto"),
    path("producto/<int:producto_id>/", views.info_producto, name="info_producto"),
    path("add_producto/", views.add_producto, name="add_producto"),
    path("edit_producto/<int:id>/", views.edit_producto, name="edit_producto"),
    path("delete_producto/<int:id>/", views.delete_producto, name="delete_producto"),
    #ventas path
    path("venta", views.venta, name="venta"),
    path("venta/<int:venta_id>/", views.info_venta, name="info_venta"),
    path("add_venta/", views.add_venta, name="add_venta"),
    path("edit_venta/<int:id>/", views.edit_venta, name="edit_venta"),
    path("delete_venta/<int:id>/", views.delete_venta, name="delete_venta"),
]