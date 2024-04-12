from django.db import models
from datetime import datetime

# Create your models here.
from .choices import gender_choices


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre', unique=True)

    def __str__(self):
        return 'Nombre: {}'.format(self.name)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['id']


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre', unique=True)
    cate = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product/%Y/%m/%d', null=True, blank=True)
    pvp = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['id']


class Client(models.Model):
    names = models.CharField(max_length=150, verbose_name='Nombres')
    surnames = models.CharField(max_length=150, verbose_name='Apellidos')
    dni = models.CharField(max_length=10, unique=True, verbose_name='Dni')
    birthday = models.DateField(default=datetime.now, verbose_name='Fecha de nacimiento')
    address = models.CharField(max_length=150, null=True, blank=True, verbose_name='Dirección')
    sexo = models.CharField(max_length=10, choices=gender_choices, default='male', verbose_name='Sexo')

    def __str__(self):
        return self.names

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['id']


class Sale(models.Model):
    cli = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_joined = models.DateField(default=datetime.now)
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    iva = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    total = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return self.cli.names

    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'
        ordering = ['id']


class DetSale(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    prod = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    cant = models.IntegerField(default=0)
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return self.prod.name

    class Meta:
        verbose_name = 'Detalle de Venta'
        verbose_name_plural = 'Detalle de Ventas'
        ordering = ['id']



# LO COMENTADO ABAJO FUE UN EJEMPLO DE LOS PRIMEROS CAPITULOS DEL CURSO
# PUEDE SERVIR PARA DARSE CUENTA DE ALGUNAS OPCIONES:

# class Type(models.Model):
#     # Clase que identifica los tipos de empleados
#     name = models.CharField(max_length=150, verbose_name="nombre")

#     def __str__(self) -> str:
#         return self.name

#     class Meta:
#         verbose_name = 'Tipo'
#         verbose_name_plural = 'Tipos'
#         ordering = ['id']

# class Category(models.Model):
#     name = models.CharField(max_length=100)

#     def __str__(self) -> str:
#         return "Nro: {} / Nombre: {}".format(self.id, self.name)

    
#     class Meta:
#         verbose_name = 'Categoria'
#         verbose_name_plural = 'Categorias'
#         ordering = ['id']

# class Employee(models.Model):
#     category = models.ManyToManyField(Category)
#     type = models.ForeignKey(Type, on_delete=models.CASCADE) # on_delete=models.PROTECT hace que se impida eliminar un registro de Tipo si hay empleados que lo referenciam
#     names = models.CharField(max_length=150, verbose_name='Nombres') #verbose_name: este parámetro lo va a tomar cuando por ejemplo cree un formulario para el nombre del campo, si no lo pongo pone directamente el nombre del atributo
#     dni = models.CharField(max_length=10, unique=True, verbose_name='Dni')
#     date_joined = models.DateField(default=datetime.now, verbose_name='Fecha de Registro')
#     date_creation = models.DateTimeField(auto_now=True) #auto_now = cuando se cree el registro a este atributo se le colocará la fecha actual, si luego lo modifico esta fecha no se modificará mas
#     date_udpated = models.DateTimeField(auto_now_add=True) #auto_now_add = cuando cree el registo este atributo se creará automaticamente, y cuando lo modifique se actualizará con la fecha del momento
#     age = models.PositiveIntegerField(default=0)
#     salary = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
#     state = models.BooleanField(default=True)
#     # gender = models.CharField(max_length=50)
#     avatar = models.ImageField(upload_to='avatar/%Y/%m/%d', null=True, blank=True) # upload_to indica donde guardar la imegen, con '/%Y/%m/%d' le agrego la fecha
#     cvitae  = models.FileField(upload_to='cvitae/%Y/%m/%d', null=True, blank=True) # con null y blank igual a True permito que estos campos estén vaciós

#     def __str__(self) -> str:
#         return self.names
    
#     class Meta:
#         verbose_name = 'Empleado' # Va a tomar este nombre en el Panel Admin
#         verbose_name_plural = "Empleados" # idem anterior pero en plural
#         db_table = 'empleado' # Le puedo especificar si quiero el nombre de la tabla con que quiero que se cree en la BD
#         ordering = ['-id'] # Le indico como quiero que se vialicen ordenados en el Admin(creo), con'-' le indico orden descendente




