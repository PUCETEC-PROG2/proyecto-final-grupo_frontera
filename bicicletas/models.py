from django.db import models
 
class Cliente(models.Model):
    first_name = models.CharField(max_length=30, null=False)
    last_name = models.CharField(max_length=30, null=False)
    birth_date = models.DateField(null=False)
    
 #devuelve el primer nombre y ultimo
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
class Categoria(models.Model):
    BICICLETA_MARCA = [
        ('GNT', 'Giant'),
        ('TRK', 'Trek'),
        ('SPZ', 'Specialized'),
        ('CND', 'Cannondale'),
    ]

    TIPO_BICICLETA = [
        ('BU', 'Bicicleta Urbana'),
        ('BM', 'Bicicleta de Montaña'),
        ('BE', 'Bicicleta Eléctrica'),
        ('BT', 'Bicicleta de Turismo'),
    ]

    name = models.CharField(max_length=100)
    type = models.CharField(max_length=2, choices=TIPO_BICICLETA)
    marca = models.CharField(max_length=3, choices=BICICLETA_MARCA)
    descripcion = models.TextField()

 #returna el nombre de la bici y el tipo de bici
    def __str__(self):
        return f"{self.name} ({self.type})"
    
class Producto(models.Model):
    name = models.CharField(max_length=100, null=False)
    price = models.DecimalField(null=False, default=1, max_digits=4, decimal_places=2)
    cantidad = models.IntegerField(default=1, null=False)
    category = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='product_images')
 
    def __str__(self):
        return f"{self.name}"
    
class Venta(models.Model):
    product = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    date = models.DateTimeField(null=False)
    cantidad = models.PositiveIntegerField()
    price = models.DecimalField(null=False, max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"{self.cliente} {self.date} {self.price}"