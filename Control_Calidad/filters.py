import django_filters

from .models import *
from django_filters import DateFilter , CharFilter , NumberFilter
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User
from django.forms import ModelForm
from django import forms

class OderFilter(django_filters.FilterSet):
    #
    ##    Fecha_Inicio = DateFilter(field_name = "Fecha_registro" , lookup_expr = 'gte')
    ##    Fecha_Terminado = DateFilter(field_name = "Fecha_registro" , lookup_expr = 'lte')
    #Filtro de fecha por inicio y fin
    #Para excluir registros
    #exclude = ['Numero_empleado','Fecha_registro']
    Nombre_empleado = CharFilter(field_name= "Nombre_empleado" , lookup_expr= "icontains")

    class Meta:
        model = Empleados
        fields = "__all__"

class Oder_Filter_Almacen(django_filters.FilterSet):
    
   Nombre = CharFilter(field_name= "Nombre" , lookup_expr= "icontains")
   
   class Meta:
       
        model = Almacen
        
        fields = "__all__"     
        
        
class Oder_Filter_Productos(django_filters.FilterSet):
    
   Nombre = CharFilter(field_name= "Nombre" , lookup_expr= "icontains")
   
   class Meta:
       
        model = Producto
        
        fields = "__all__"  
        
        widgets = {'Fecha_ingreso':forms.DateInput(attrs={'type':'date'})}

class Oder_Filter_Control_Calidad(django_filters.FilterSet):
    
      
    Numero_de_Pedio_Calidad = CharFilter(field_name= "Numero_de_Pedio_Calidad" , lookup_expr= "icontains")
   
    class Meta:
       
        model = Calidad_Control_Lotes_Registro
        
        fields = "__all__"  
        
        widgets = {'Fecha_registro':forms.DateInput(attrs={'type':'date'})}
        
        
class Oder_Filter_Pruebas(django_filters.FilterSet):

    Nombre_Prueba = CharFilter(field_name= "Nombre_Prueba" , lookup_expr= "icontains")
    
   
    class Meta:
       
        model = Calidad_Pruebas_Registro
        
        fields = "__all__"  
        
        
class Oder_Filter_Liberacion(django_filters.FilterSet):

    Numero_liberacion = NumberFilter(field_name= "Numero_liberacion" , lookup_expr= "icontains")

    class Meta:
       
        model = Calidad_Liberacion_Registro
        
        fields = "__all__"          
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # -*- coding: utf-8 -*-

