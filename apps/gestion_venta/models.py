from django.db import models
from django.forms import model_to_dict

class Categoria(models.Model):
    name = models.CharField(verbose_name='Nombre', max_length=50, unique=True)
    description = models.TextField(verbose_name="Descripción")
    state = models.BooleanField(verbose_name = 'Activo', default=True)
    def __str__(self):
        return self.name
    
    def get_model_to_dict(self):
        item= model_to_dict(self)
        return item
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural ='Categorias'
        ordering =['-name']

class Producto(models.Model):
    name = models.CharField(verbose_name='Nombre de los productos', max_length=50, unique=True)
    description = models.TextField(verbose_name="Descripción")
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    stock = models.PositiveIntegerField(verbose_name='Stock disponible', default=0)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL,  null=True, verbose_name='Categoría a la que pertenece')
    
    def __str__(self):
        return self.name
    
    def get_model_to_dict(self):
        item= model_to_dict(self)
        return item
    
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural ='Productos'
        ordering =['-name']

class Cliente (models.Model): 
    name = models.CharField(verbose_name='Nombre', max_length=50, unique=True)
    apellido = models.CharField(verbose_name='Apellido', max_length=50)
    correo = models.EmailField(verbose_name='Correo Electrónico', unique=True)
    direccion = models.CharField(verbose_name='Dirección', max_length=255, blank=True, null=True)
    telefono = models.CharField(verbose_name='Número de Teléfono', max_length=15, blank=True, null=True)

    def __str__(self):
        return self.name
    
    def get_model_to_dict(self):
        item= model_to_dict(self)
        return item
    
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural ='Clientes'
        ordering =['-name']