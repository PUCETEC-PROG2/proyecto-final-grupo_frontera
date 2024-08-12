from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.template import loader
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from bicicletas.forms import ClienteForm, CategoriaForm, ProductoForm, VentaForm
from .models import Cliente, Categoria, Producto, Venta

class CustomLoginView(LoginView):
    template_name = 'login.html'

def index(request):
    return render(request, 'index.html')

def cliente(request):
    clientes = cliente.objects.order_by('ultimo_nombre')
    template = loader.get_template('cliente.html')
    return HttpResponse(template.render({'clientes': clientes}, request))

def info_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk= cliente_id)
    template = loader.get_template('display_cliente.html')
    context = {
        'cliente': cliente
    }
    return HttpResponse(template.render(context, request))

@login_required
def add_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('bicicletas:cliente')
    else:
        form = ClienteForm()   
    return render(request, 'cliente_form.html', {'form': form})

@login_required
def edit_cliente(request, id):
    cliente = get_object_or_404(Cliente, pk = id)
    if request.method == 'POST':
        form = ClienteForm(request.POST, request.FILES, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('bicicletas:cliente')
    else:
        form = ClienteForm(instance=cliente)       
    return render(request, 'cliente_form.html', {'form': form})

@login_required
def delete_cliente(request, id):
    cliente = get_object_or_404(Cliente, pk = id)
    cliente.delete()
    return redirect("bicicletas:cliente")



def categoria(request):
    categorias = Categoria.objects.order_by('nombre')
    template = loader.get_template('categoria.html')
    return HttpResponse(template.render({'categorias': categorias}, request))

def info_categoria(request, category_id):
    categoria = get_object_or_404(Categoria, pk= categoria_id)
    template = loader.get_template('display_categoria.html')
    context = {
        'categoria': categoria
    }
    return HttpResponse(template.render(context, request))

@login_required
def add_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('bicicletas:categoria')
    else:
        form = CategoriaForm()   
    return render(request, 'categoria_form.html', {'form': form})

@login_required
def edit_categoria(request, id):
    categoria = get_object_or_404(Categoria, pk = id)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, request.FILES, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('bicicletas:categoria')
    else:
        form = CategoriaForm(instance=categoria)       
    return render(request, 'categoria_form.html', {'form': form})

@login_required
def delete_categoria(request, id):
    categoria = get_object_or_404(Categoria, pk = id)
    categoria.delete()
    return redirect("bicicletas:categoria")



def producto(request):
    productos = Producto.objects.order_by('nombre')
    template = loader.get_template('producto.html')
    return HttpResponse(template.render({'productos': productos}, request))

def info_producto(request, product_id):
    producto = get_object_or_404(Producto, pk= product_id)
    template = loader.get_template('display_producto.html')
    context = {
        'producto': producto
    }
    return HttpResponse(template.render(context, request))

@login_required
def add_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('bicicletas:producto')
    else:
        form = ProductoForm()   
    return render(request, 'producto_form.html', {'form': form})


@login_required
def edit_producto(request, id):
    producto = get_object_or_404(Producto, pk = id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('bicicletas:producto')
    else:
        form = ProductoForm(instance=producto)       
    return render(request, 'producto_form.html', {'form': form})

@login_required
def delete_producto(request, id):
    producto = get_object_or_404(Producto, pk = id)
    producto.delete()
    return redirect("bicicletas:producto")



def venta(request):
    ventas = Venta.objects.order_by('producto')
    template = loader.get_template('venta.html')
    return HttpResponse(template.render({'ventas': ventas}, request))

def info_venta(request, sale_id):
    venta = get_object_or_404(Venta, pk= venta_id)
    template = loader.get_template('display_ventas.html')
    context = {
        'venta': venta
    }
    return HttpResponse(template.render(context, request))

@login_required
def add_venta(request):
    if request.method == 'POST':
        form = VentaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('bicicletas:venta')
    else:
        form = VentaForm()   
    return render(request, 'ventas_form.html', {'form': form})


@login_required
def edit_venta(request, id):
    venta = get_object_or_404(Venta, pk = id)
    if request.method == 'POST':
        form = VentaForm(request.POST, request.FILES, instance=venta)
        if form.is_valid():
            form.save()
            return redirect('bicicletas:venta')
    else:
        form = VentaForm(instance=venta)       
    return render(request, 'ventas_form.html', {'form': form})

@login_required
def delete_venta(request, id):
    venta = get_object_or_404(Venta, pk = id)
    venta.delete()
    return redirect("bicicletas:venta")