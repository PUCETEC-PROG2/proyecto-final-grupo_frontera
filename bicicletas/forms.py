from django import forms
from .models import Cliente, Venta, Categoria, Producto #importa de modelos 
#clase cliente
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'birth_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'cedula': forms.TextInput(attrs={'class': 'form-control'})
        }
        labels = {
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'birth_date': 'Fecha de Nacimiento',
            'phone': 'Teléfono',
            'cedula': 'Cédula de Identidad' #cedula del cliente
        }
        
#clase ventas
class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = '__all__'
        widgets = {
            'date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'product': forms.Select(attrs={'class': 'form-control'}),
            'cliente': forms.Select(attrs={'class': 'form-control'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control', 'min': '1'}),#ayuda a que usuario ingrese un valor valido
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'date': 'Fecha de la Venta',
            'product': 'Producto',
            'cliente': 'Cliente',
            'cantidad': 'Cantidad',
            'price': 'Precio de Venta',
        }

#clase de oroducto
class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'picture': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'name': 'Nombre del Producto',
            'picture': 'Imagen del Producto',
            'price': 'Precio',
            'cantidad': 'Cantidad',
            'category': 'Categoría',
        }
#clase de la categoria de bicis
class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'type': forms.Select(attrs={'class': 'form-control'}),
            'brand': forms.Select(attrs={'class': 'form-control'}),
            
        }
        labels = {
            'name': 'Nombre de la Categoría',
            'type': 'Tipo',
            'brand': 'Marca',
            
        }

