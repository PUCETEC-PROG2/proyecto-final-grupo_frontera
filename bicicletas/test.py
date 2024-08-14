from django.urls import path
from . import views

app_name = "bicicletas"
urlpatterns = [
    path("", views.index, name="index"),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path("venta", views.venta, name="venta"),
    path("venta/<int:venta_id>/", views.venta, name="display_venta"),
    path("add_venta/", views.add_venta, name="add_venta"),
    path("delete_venta/<int:id>/", views.delete_venta, name="delete_venta"),
    path("edit_venta/<int:id>/", views.edit_venta, name="edit_venta"),
]