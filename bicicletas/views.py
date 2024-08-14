from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.template import loader
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from bicicletas.forms import CategoriaForm, VentaForm, ProductoForm, ClienteForm
from .models import Producto, Cliente, Venta, Categoria

class CustomLoginView(LoginView):
    template_name = 'login.html' #al archivo para logear el usuario

def index(request):
    return render(request, 'index.html')

def cliente(request):
    clientes = Cliente.objects.order_by('last_name')
    template = loader.get_template('cliente.html')
    return HttpResponse(template.render({'clientes': clientes}, request))

def info_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)
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
def delete_cliente(request, id):
    cliente = get_object_or_404(Cliente, pk = id)
    cliente.delete()
    return redirect("bicicletas:cliente")

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

#para editar el c,iente


#categoria-----------------------------------------------------------------#
def category(request):
    categorys = Categoria.objects.order_by('name')
    template = loader.get_template('categoria.html')
    return HttpResponse(template.render({'categorys': categorys}, request))
#para añadir las categoria 
@login_required
def add_category(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('bicicletas:category')
    else:
        form = CategoriaForm()   
    return render(request, 'categoria_form.html', {'form': form}) #formulario de las categoria 



#muestra la informacion que se puso dentro de la categoria
def info_category(request, category_id):
    category = get_object_or_404(Categoria, pk= category_id)
    template = loader.get_template('display_categoria.html')
    context = {
        'category': category
    }
    return HttpResponse(template.render(context, request))
#para editar si es que se hubo un errro al ingrsar akgo en el añadir categoria
@login_required
def edit_category(request, id):
    category = get_object_or_404(Categoria, pk = id)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, request.FILES, instance=category)
        if form.is_valid():
            form.save()
            return redirect('bicicletas:category')
    else:
        form = CategoriaForm(instance=category)       
    return render(request, 'categoria_form.html', {'form': form})


#para boorrar una categoria que no sirva o que se haya ido mal
@login_required
def delete_category(request, id):
    category = get_object_or_404(Categoria, pk = id)
    category.delete()
    return redirect("bicicletas:category")


#producto____________________________________________________________#
def product(request):
    products = Producto.objects.order_by('name')
    template = loader.get_template('producto.html')
    return HttpResponse(template.render({'products': products}, request))

@login_required #edita un producto qye se haya ido mal 
def edit_product(request, id):
    product = get_object_or_404(Producto, pk = id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('bicicletas:product')
    else:
        form = ProductoForm(instance=product)       
    return render(request, 'producto_form.html', {'form': form})#al fomrulario de los productos

#muestra informacione especifica del producto qye pusimos 
def info_product(request, product_id):
    product = get_object_or_404(Producto, pk= product_id)
    template = loader.get_template('display_producto.html')#detalles del producto 
    context = {
        'product': product
    }
    return HttpResponse(template.render(context, request))
#para añadir las bicicletas en el formulario de producto
@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('bicicletas:product')
    else:
        form = ProductoForm()   
    return render(request, 'producto_form.html', {'form': form})
#aqui------------------------->


#se borra producto 
@login_required
def delete_product(request, id):
    product = get_object_or_404(Producto, pk = id)
    product.delete()
    return redirect("bicicletas:product")


#ventas---------------------------------------------------#
def venta(request):
    ventas = Venta.objects.order_by('product')
    template = loader.get_template('venta.html')
    return HttpResponse(template.render({'ventas': ventas}, request))


@login_required
def edit_venta(request, id):
    venta = get_object_or_404(Venta, pk=id)
    form = VentaForm(request.POST or None, instance=venta)
    
    if form.is_valid():
        nueva_cantidad = form.cleaned_data['cantidad']
        product = venta.product
        
        if nueva_cantidad <= product.cantidad + venta.cantidad:
            product.cantidad = product.cantidad + venta.cantidad - nueva_cantidad
            form.save()
            product.save()
            return redirect('bicicletas:venta')
        else:
            form.add_error('cantidad', 'No hay muchas bicicletas.') #en el caso de que no haya nada de productos

    return render(request, 'venta_form.html', {'form': form})

@login_required
def add_venta(request):
    form = VentaForm(request.POST or None, request.FILES or None)
    
    if request.method == 'POST' and form.is_valid():
        venta = form.save(commit=False)
        product = venta.product
        
        if venta.cantidad <= product.cantidad:
            product.cantidad -= venta.cantidad
            product.save()
            venta.save()
            return redirect('bicicletas:venta')
        else:
            form.add_error('cantidad', 'No hay bicicletas') #asi como arriba 

    return render(request, 'venta_form.html', {'form': form})


def info_venta(request, sale_id):
    venta = get_object_or_404(Venta, pk= sale_id)
    template = loader.get_template('display_venta.html')#detalles de la venta que se hizo 
    context = {
        'venta': venta
    }
    return HttpResponse(template.render(context, request))


#para borrar
@login_required
def delete_venta(request, id):
    venta = get_object_or_404(Venta, pk = id)
    venta.delete()
    return redirect("bicicletas:venta")

#lista de las ventas(aun en procesof)
def ventas_list(request):
    ventas = Venta.objects.all()  #  todas las ventas
    return render(request, 'ventas_list.html', {'ventas': ventas})