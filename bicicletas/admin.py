from django.contrib import admin

# Register your models here.

from .models import Cliente, Categoria, Venta, Producto


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    pass

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    pass

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    pass

@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    pass