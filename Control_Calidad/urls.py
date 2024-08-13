from django.urls import path, include
from .views import *
from . import *

urlpatterns = [
    path('', Inicio,name=""),   
    path('Inicio_Sesion/', Inicio_Sesion,name="Inicio_Sesion"), 
    path('Inicio_Sesion_P/', Inicio_Sesion_P,name="Inicio_Sesion_P"), 
    path('Ayuda/', Ayuda,name="Ayuda"), 
    path('Inicio_Calidad/', Inicio_Calidad,name="Inicio_Calidad"), 
    path('Control_de_lotes_alta/', Control_de_lotes_alta,name="Control_de_lotes_alta"),
    
    path('Empleados_Inicio_View/', Empleados_Inicio_View,name="Empleados_Inicio_View"),
    path('Empleados_Consulta_View/', Empleados_Consulta_View,name="Empleados_Consulta_View"),
    path('Registro_empleados_View/', Registro_empleados_View,name="Registro_empleados_View"),   
    path('Empleados_Modificar_Eliminar_view/', Empleados_Modificar_Eliminar_view,name="Empleados_Modificar_Eliminar_view"),   
    path('Empleados_Modificar_view/<id>/', Empleados_Modificar_view,name="Empleados_Modificar_view"),   
    path('Empleados_Eliminar_view/<id>/', Empleados_Eliminar_view,name="Empleados_Eliminar_view"),
    
    path('Almacenes_Inicio_view/', Almacenes_Inicio_view,name="Almacenes_Inicio_view"),
    path('Registro_Almacenes_View/', Registro_Almacenes_View,name="Registro_Almacenes_View"),
    path('Almacen_Consulta_View/', Almacen_Consulta_View,name="Almacen_Consulta_View"),
    path('Almacen_Modificar_Eliminar_view/', Almacen_Modificar_Eliminar_view,name="Almacen_Modificar_Eliminar_view"),
    path('Almacen_Modificar_view/<id>/', Almacen_Modificar_view,name="Almacen_Modificar_view"),   
    path('Almacen_Eliminar_view/<id>/', Almacen_Eliminar_view,name="Almacen_Eliminar_view"),  
    
    path('Productos_Inicio_view/', Productos_Inicio_view,name="Productos_Inicio_view"),
    path('Registro_Productos_View/', Registro_Productos_View,name="Registro_Productos_View"),
    path('Productos_Consulta_View/', Productos_Consulta_View,name="Productos_Consulta_View"),
    path('Producto_Modificar_Eliminar_view/', Producto_Modificar_Eliminar_view,name="Producto_Modificar_Eliminar_view"),
    path('Producto_Modificar_view/<id>/', Producto_Modificar_view,name="Producto_Modificar_view"),   
    path('Producto_Eliminar_view/<id>/', Producto_Eliminar_view,name="Producto_Eliminar_view"),  

    path('Control_de_Lotes_Inicio_view/', Control_de_Lotes_Inicio_view,name="Control_de_Lotes_Inicio_view"),
    path('Control_de_lotes_alta/', Control_de_lotes_alta,name="Control_de_lotes_alta"),
    path('Control_de_Lotes_Consulta_View/', Control_de_Lotes_Consulta_View,name="Control_de_Lotes_Consulta_View"),
    path('Control_de_Lotes_Modificar_Eliminar_view/', Control_de_Lotes_Modificar_Eliminar_view,name="Control_de_Lotes_Modificar_Eliminar_view"),
    path('Control_de_Lotes_Modificar_view/<id>/', Control_de_Lotes_Modificar_view,name="Control_de_Lotes_Modificar_view"),
    path('Control_de_Lotes_Eliminar_view/<id>/', Control_de_Lotes_Eliminar_view,name="Control_de_Lotes_Eliminar_view"),  

    path('Pruebas_Inicio_view/', Pruebas_Inicio_view,name="Pruebas_Inicio_view"),
    path('Pruebas_alta_view/', Pruebas_alta_view,name="Pruebas_alta_view"),
    path('Prueba_Consulta_View/', Prueba_Consulta_View,name="Prueba_Consulta_View"),
    path('Pruebas_Modificar_Eliminar_view/', Pruebas_Modificar_Eliminar_view,name="Pruebas_Modificar_Eliminar_view"),
    path('Pruebas_Modificar_view/<id>/', Pruebas_Modificar_view,name="Pruebas_Modificar_view"),
    path('Pruebas_Eliminar_view/<id>/', Pruebas_Eliminar_view,name="Pruebas_Eliminar_view"),  

    path('Liberacion_Inicio_view/', Liberacion_Inicio_view,name="Liberacion_Inicio_view"),
    path('Liberacion_alta_view/', Liberacion_alta_view,name="Liberacion_alta_view"),
    path('Liberacion_Consulta_View/', Liberacion_Consulta_View,name="Liberacion_Consulta_View"),
    path('Liberacion_Modificar_Eliminar_view/', Liberacion_Modificar_Eliminar_view,name="Liberacion_Modificar_Eliminar_view"),
    path('Liberacion_Modificar_view/<id>/', Liberacion_Modificar_view,name="Liberacion_Modificar_view"),
    path('Liberacion_Eliminar_view/<id>/', Liberacion_Eliminar_view,name="Liberacion_Eliminar_view"),  

    path('Pruebas_Template/', Pruebas_Template,name="Pruebas_Template"),

]
