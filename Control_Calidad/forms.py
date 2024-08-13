from django.db import models
from django.forms import ModelForm
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User

class Control_de_lotes_alta_form(ModelForm):
    class Meta:
        
        model = Calidad_Control_Lotes_Registro
        
        fields = '__all__'
        
        widgets = {'Fecha_registro':forms.DateInput(attrs={'type':'date'}),'Fecha_programada_de_pruebas':forms.DateInput(attrs={'type':'date'})}
        
class Registros_empleados_form(ModelForm):  
    class Meta:
        model = Empleados
        fields = '__all__'
        widgets = {'Fecha_registro':forms.DateInput(attrs={'type':'date'})}
        
class Registros_almacenes_form(ModelForm):  
   
    class Meta:
        
        model = Almacen
        
        fields = '__all__'

class Registros_Productos_form(ModelForm):  
   
    class Meta:
        
        model = Producto
        
        fields = '__all__'
        
        widgets = {'Fecha_ingreso':forms.DateInput(attrs={'type':'date'})}

class Registro_Pruebas_form(ModelForm):

    class Meta:
        
        model = Calidad_Pruebas_Registro
        
        fields = '__all__'
        
        widgets = {'Fecha_programada_de_pruebas':forms.DateInput(attrs={'type':'date'})}

        
class Registro_Liberacion_form(ModelForm):

    class Meta:
        
        model = Calidad_Liberacion_Registro
        
        fields = '__all__'
        
        widgets = {'Fecha_liberacion':forms.DateInput(attrs={'type':'date'})}

        
        
        
        
        
        
        
        
        
        # -*- coding: utf-8 -*-

