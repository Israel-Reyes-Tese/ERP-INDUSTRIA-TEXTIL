from django.db import models

# Create your models here.
class Empleados(models.Model):
    
    Numero_empleado = models.CharField(max_length = 255 , unique = True )  
    
    Nombre_empleado = models.CharField(max_length = 255)  
    
    Apellido_empleado = models.CharField(max_length = 255) 
    
    Puesto_empleado = models.CharField(max_length = 255) 
    
    Fecha_registro = models.DateField()
    
    Imagen_Perfil = models.URLField(null = True)
   
    class Meta:
        
        verbose_name = "Empleados"
        
        verbose_name_plural = "Empleado"
    
    def __str__(self):
        return self.Numero_empleado  
    
class Almacen(models.Model):
    
    Nombre = models.CharField(max_length = 255 , unique = True )
    
    Numero_almacen =  models.IntegerField()
    
    Encargado_de_almacen =models.ForeignKey(Empleados, on_delete = models.CASCADE)
    
    Imagen_Perfil = models.URLField(null = True)
    
    class Meta:
        
        verbose_name = "Almacenes"
        
        verbose_name_plural = "Almacen"   
        
    def __str__(self):
        return self.Nombre
    
    
class Producto(models.Model):
    
    Nombre = models.CharField(max_length = 255 , unique = True )
    
    Fecha_ingreso = models.DateField(null = False) 
    
    class Meta:
        
        verbose_name = "Productos"
        
        verbose_name_plural = "Producto"       

    def __str__(self):
        return self.Nombre  
        
class Calidad_Control_Lotes_Registro(models.Model):
    
    Numero_de_Pedio_Calidad = models.CharField(max_length = 255 , null = True , unique = True )
    
    Numero_Lote = models.IntegerField()
    
    Fecha_registro = models.DateField(null = False)
    
    Fecha_programada_de_pruebas = models.DateField(null = True)

    Motivo = models.TextField(null = False)
    
    Encargado_de_control_lotes = models.ForeignKey(Empleados, on_delete = models.CASCADE)
    
    Productos = models.ManyToManyField(Producto)
    
    Numero_de_productos = models.IntegerField()
    
    Enviado_Pruebas = models.BooleanField(default = False)
    
    Almacen_alojado = models.ForeignKey(Almacen, on_delete = models.CASCADE)
    
    class Meta:
    
        verbose_name = "Control de lote"
        
        verbose_name_plural = "Control de lote" 
    
    def __str__(self):
        
        return self.Numero_de_Pedio_Calidad      
    
    
class Calidad_Pruebas_Registro(models.Model):
    
    Numero_de_Lote = models.ForeignKey(Calidad_Control_Lotes_Registro, on_delete = models.CASCADE)

    Nombre_Prueba = models.CharField(max_length = 255)
    
    Numero_de_Prueba = models.IntegerField()

    Encargado_de_pruebas = models.ForeignKey(Empleados, on_delete = models.CASCADE)

    Tipo_de_pruebas = models.CharField(max_length = 255)
   
    Pruebas_satisfactorias = models.BooleanField(default = False , null = True)
    
    Fecha_programada_de_pruebas = models.DateField(null = True)
    
    Enviado_Liberacion = models.BooleanField(default = False , null = True)

    
    
    class Meta:
    
        verbose_name = "Pruebas"
        
        verbose_name_plural = "Prueba"
    
    def __str__(self):
        return self.Nombre_Prueba  
    
class Calidad_Liberacion_Registro(models.Model):
    
    Codigo_de_liberacion = models.CharField(max_length = 255 , null = True , unique = True )
    
    Lote_liberado = models.ForeignKey(Calidad_Control_Lotes_Registro, on_delete = models.CASCADE)
    
    Encargado_de_liberacion = models.ForeignKey(Empleados, on_delete = models.CASCADE)
    
    Numero_liberacion = models.IntegerField()
    
    Fecha_liberacion = models.DateField()
    
    Notas = models.TextField()
    
    Enviado_almacen = models.BooleanField(default = False)
    
    Validado = models.BooleanField(default = False)
    
    Devueltos_a_pruebas = models.BooleanField(default = False)
    
    class Meta:
    
        verbose_name = "Liberacion"
        
        verbose_name_plural = "Liberaciones"   
    
    def __str__(self):
        return self.Codigo_de_liberacion  
    