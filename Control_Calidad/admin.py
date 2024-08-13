from django.contrib import admin
from .models import *

# Register your models here.
class Calidad_Pruebas_Registro_Admin(admin.ModelAdmin):
    list_display=("id","Numero_de_Lote","Nombre_Prueba","Fecha_programada_de_pruebas","Enviado_Liberacion")    
    #AGREGAR UN BOTON DE BUSQUEDA:   

    #FILTRAR 
    list_filter=("Nombre_Prueba","Enviado_Liberacion")
    
    date_hierarchy = "Fecha_programada_de_pruebas"


class Calidad_Liberacion_Registro_Admin(admin.ModelAdmin):
    list_display=("Codigo_de_liberacion","Lote_liberado","Enviado_almacen","Validado","Devueltos_a_pruebas")    
    #AGREGAR UN BOTON DE BUSQUEDA:   

    #FILTRAR 
    list_filter=("Enviado_almacen","Validado","Devueltos_a_pruebas")


admin.site.register(Empleados)
admin.site.register(Almacen)
admin.site.register(Producto)
admin.site.register(Calidad_Control_Lotes_Registro)
admin.site.register(Calidad_Pruebas_Registro,Calidad_Pruebas_Registro_Admin)
admin.site.register(Calidad_Liberacion_Registro,Calidad_Liberacion_Registro_Admin)


