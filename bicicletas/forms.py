from django import forms
from .models import Cliente, Categoria, Producto, Venta

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
        widgets = {
            'primer_nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'ultimo_nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_nacimiento': forms.DateInput(attrs={'class': 'form-control', 'tipo': 'fecha'}),
            'teléfono': forms.TextInput(attrs={'class': 'form-control'}),
            'cedula': forms.TextInput(attrs={'class': 'form-control'})
        }
        labels = {
            'primer_nombre': 'Nombre',
            'ultimo_nombre': 'Apellido',
            'fecha_nacimiento': 'Fecha de Nacimiento',
            'teléfono': 'Teléfono',
            'cedula': 'Cédula de Identidad'
        }
        
class CategoriaForm(forms.ModelForm):
    class Meta:
       model = Categoria
       pass

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }
        labels = {
            'nombre': 'Nombre del Producto',
            'precio': 'Precio',
            'cantidad': 'Cantidad',
            'categoria': 'Categoría',
            'imagen': 'Imagen del Producto',
        }

class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = '__all__'
        widgets = {
            'fecha': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'producto': forms.Select(attrs={'class': 'form-control'}),
            'cliente': forms.Select(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'fecha': 'Fecha de la Venta',
            'producto': 'Producto', #que escogio el clientea
            'cliente': 'Cliente',
            'precio': 'Precio de Venta',
        }