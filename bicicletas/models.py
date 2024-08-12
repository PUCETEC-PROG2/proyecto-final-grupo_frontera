
from django.db import models
 
class Cliente(models.Model):
    primer_nombre = models.CharField(max_length=30, null=False)
    ultimo_nombre = models.CharField(max_length=30, null=False)
    fecha_nacimiento = models.DateField(null=False)
    telefono = models.CharField(max_length=10, null=False)

    
    
 
    def __str__(self):
        return f'{self.primer_nombre} {self.ultimo_nombre}'

class Categoria(models.Model):
    nombre = models.CharField(max_length=50, null=False)
    
    TYPE_CHOICES = [
        ('BU', 'Bicicletas Urbanas'),
        ('BM', 'Bicicletas de Montaña'),
        ('BE', 'Bicicletas Eléctricas'),
        ('BT', 'Bicicletas de Triatlón'),
    ]
    
    tipo = models.CharField(max_length=2, choices=TYPE_CHOICES, null=False)

    def __str__(self):
        return f"{self.nombre} {self.tipo}"


class Marca(models.Model):
    BRAND_CHOICES = [
        ('Giant', 'Giant'),
        ('Trek', 'Trek'),
        ('Specialized', 'Specialized'),
        ('Cannondale', 'Cannondale'),
    
    ]
    
    nombre = models.CharField(max_length=30, choices=BRAND_CHOICES, null=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='marcas')

    def __str__(self):
        return self.nombre

    
class Producto(models.Model):
    nombre = models.CharField(max_length=100, null=False)
    precio = models.DecimalField(null=False, default=1, max_digits=4, decimal_places=2)
    cantidad = models.IntegerField(default=1, null=False)
    Categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    Marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    imagenes = models.ImageField(upload_to='producto_imagenes')
 
    def __str__(self):
        return f"{self.nombre}"
    
class Venta(models.Model):
    fecha = models.DateTimeField(null=False)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    precio = models.DecimalField(null=False, max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"{self.fecha} {self.cliente} {self.precio}"