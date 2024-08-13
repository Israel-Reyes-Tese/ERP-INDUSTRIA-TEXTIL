from django.shortcuts import render
from .models import *
from .forms import *
from django.contrib import messages
from .filters import *
from django.shortcuts import redirect, get_object_or_404
from datetime import *
from django.contrib.auth.decorators import login_required, permission_required
# Create your views here.
def Inicio(request):
    
    Fecha = datetime.now()
    
    today = date.today()
    
    Fecha_año = str(Fecha.year)
    
    Fecha_mes = Fecha.month
    Fecha_dia = Fecha.day
    
    if Fecha_mes <= 9:     
        Fecha_mes = str(Fecha.month)
        Fecha_mes = "0"+Fecha_mes
    else:
        Fecha_mes = str(Fecha.month)
        
        
    if Fecha_dia <= 9:     
        Fecha_dia = str(Fecha.day)
        Fecha_dia = "0"+Fecha_dia
        
    else:
        Fecha_dia = str(Fecha.day)
        
    
    Fecha_actual = Fecha_año+"-"+Fecha_mes+"-"+Fecha_dia
    
    Objectos = Calidad_Control_Lotes_Registro.objects.all()
    
    P_C_CL_F = Calidad_Control_Lotes_Registro.objects.filter(Fecha_programada_de_pruebas__gt = str(Fecha_actual))
    
    P_C_CL_F_R = Calidad_Control_Lotes_Registro.objects.filter(Fecha_programada_de_pruebas__lt = str(Fecha_actual))
    
    Se_vence_hoy = Calidad_Control_Lotes_Registro.objects.filter(Fecha_programada_de_pruebas = str(Fecha_actual))
    
    Cou_P_C_CL_F = P_C_CL_F.count()
    
    Cou_P_C_CL_F_R = P_C_CL_F_R.count()
    
    Cou_Se_vence_hoy = Se_vence_hoy.count()
    
    Progreso = Cou_P_C_CL_F + Cou_Se_vence_hoy
    
    Pr_To = Cou_P_C_CL_F + Cou_P_C_CL_F_R + Cou_Se_vence_hoy
    
# =============================================================================
#  Pruebas   
# =============================================================================
    
    Pruebas_Filtrado_Fecha_mayor = Calidad_Pruebas_Registro.objects.filter(Fecha_programada_de_pruebas__gt = str(Fecha_actual))
    
    Pruebas_Filtrado_Fecha_menor = Calidad_Pruebas_Registro.objects.filter(Fecha_programada_de_pruebas__lt = str(Fecha_actual))
    
    Pruebas_Filtrado_Fecha_igual = Calidad_Pruebas_Registro.objects.filter(Fecha_programada_de_pruebas = str(Fecha_actual))



    
    
    Count_Pruebas_Filtrado_Fecha_mayor = Pruebas_Filtrado_Fecha_mayor.count()
    
    Count_Pruebas_Filtrado_Fecha_menor = Pruebas_Filtrado_Fecha_menor.count()
    
    Count_Pruebas_Filtrado_Fecha_igual = Pruebas_Filtrado_Fecha_igual.count()



    Progreso_Pruebas = Count_Pruebas_Filtrado_Fecha_igual + Count_Pruebas_Filtrado_Fecha_menor
    
# =============================================================================
# Liberacion
# =============================================================================

    Objec_Calidad_Liberacion_Registro = Calidad_Liberacion_Registro.objects.all()
    
    Enviado_almacen_Calidad_Liberacion_Registro_F = Calidad_Liberacion_Registro.objects.filter(Enviado_almacen = True)
    
    Validado_Calidad_Liberacion_Registro_F = Calidad_Liberacion_Registro.objects.filter(Validado = True)
    
    Enviado_Error_Calidad_Liberacion_Registro_F_al = Calidad_Liberacion_Registro.objects.filter(Enviado_almacen = False )
    
    Validado_Error_Calidad_Liberacion_Registro_F_val = Calidad_Liberacion_Registro.objects.filter(Validado = False )
    
    Devueltos_Calidad_Liberacion_Registro_F_val = Calidad_Liberacion_Registro.objects.filter(Devueltos_a_pruebas = True)
    
    
    Count_Progreso_Calidad_Liberacion_Registro_F = Enviado_almacen_Calidad_Liberacion_Registro_F.count()
    
    Count_Pausa_Calidad_Liberacion_Registro_F = Validado_Calidad_Liberacion_Registro_F.count()
    
    Count_Validado_Error_Calidad_Liberacion_Registro_F_val = Validado_Error_Calidad_Liberacion_Registro_F_val.count()
    
    data ={
        
        "Fecha":Fecha,
        "Objectos":Objectos,
        "P_C_CL_F":P_C_CL_F,
        "Cou_P_C_CL_F":Cou_P_C_CL_F,
        "P_C_CL_F_R":P_C_CL_F_R,
        "Cou_P_C_CL_F_R":Cou_P_C_CL_F_R,
        "Pr_To":Pr_To,
        "Se_vence_hoy":Se_vence_hoy,
        "Progreso":Progreso,
        "Pruebas_Filtrado_Fecha_mayor":Pruebas_Filtrado_Fecha_mayor,
        "Pruebas_Filtrado_Fecha_menor":Pruebas_Filtrado_Fecha_menor,
        "Pruebas_Filtrado_Fecha_igual":Pruebas_Filtrado_Fecha_igual,
        "Count_Pruebas_Filtrado_Fecha_mayor":Count_Pruebas_Filtrado_Fecha_mayor,
        "Count_Pruebas_Filtrado_Fecha_menor":Count_Pruebas_Filtrado_Fecha_mayor,
        "Count_Pruebas_Filtrado_Fecha_igual":Count_Pruebas_Filtrado_Fecha_menor,
        "Progreso_Pruebas":Progreso_Pruebas,
        "Objec_Calidad_Liberacion_Registro":Objec_Calidad_Liberacion_Registro,
        "Enviado_almacen_Calidad_Liberacion_Registro_F":Enviado_almacen_Calidad_Liberacion_Registro_F,
        "Validado_Calidad_Liberacion_Registro_F":Validado_Calidad_Liberacion_Registro_F,
        "Enviado_Error_Calidad_Liberacion_Registro_F_al":Enviado_Error_Calidad_Liberacion_Registro_F_al,
        "Validado_Error_Calidad_Liberacion_Registro_F_val":Validado_Error_Calidad_Liberacion_Registro_F_val,
        "Count_Progreso_Calidad_Liberacion_Registro_F":Count_Progreso_Calidad_Liberacion_Registro_F,
        "Count_Pausa_Calidad_Liberacion_Registro_F":Count_Pausa_Calidad_Liberacion_Registro_F, 
        "Count_Validado_Error_Calidad_Liberacion_Registro_F_val":Count_Validado_Error_Calidad_Liberacion_Registro_F_val,
        "Devueltos_Calidad_Liberacion_Registro_F_val":Devueltos_Calidad_Liberacion_Registro_F_val,
    
        }
    return render (request,"Home.html",data)



def Inicio_Sesion(request):
    
    data = {
        'form':Formulario_Ayuda()
        }  
    
    if request.method == 'POST':
        Formulario = Formulario_Ayuda(data = request.POST)
        if Formulario.is_valid():
            Formulario.save()
            data["Mensaje"] = "ENVIADO!!"
        else:
            data["form"] = Formulario
    
    return render (request,"Iniciar_Sesion.html",data )  
   

def Inicio_Sesion_P(request):
    return render(request,"Inicio_02.html")



def Ayuda(request):
    data = {
        'form':Formulario_Ayuda()
        }
    
    if request.method == 'POST':
        Formulario = Formulario_Ayuda(data = request.POST)
        if Formulario.is_valid():
            Formulario.save()
            messages.succes(request, "Enviado")
        else:
            data["form"] = Formulario
        
    return render(request,"Ayuda.html",data)

@permission_required('Control_Calidad.view_empleados')

def Inicio_Calidad(request):
    return render(request,"Inicio_Calidad.html")

@permission_required('Control_Calidad.add_empleados')
def Registro_empleados_View(request):
    data = {
        'form':Registros_empleados_form()
        }
    if request.method == 'POST':
        Formulario = Registros_empleados_form(data = request.POST)
        if Formulario.is_valid():
            Formulario.save()
            messages.success(request,"REGISTRO GUARDADO!!")
        else:
            data["form"] = Formulario
            
    return render(request, "Empleados_Alta.html",data)

@permission_required('Control_Calidad.view_empleados')
def Empleados_Inicio_View(request):
    return render(request, "Empleados_Inicio.html")

@permission_required('Control_Calidad.view_empleados')
def Empleados_Consulta_View(request):   
    Registros_Empleados_Object = Empleados.objects.all()
    Filtros_Orde = OderFilter(request.POST, queryset = Registros_Empleados_Object )
    Orden = Filtros_Orde.qs
    data = {
        "Registros_Empleados_Object":Registros_Empleados_Object,
        "Filtros_Orde":Filtros_Orde,
        "Orden":Orden,
        }
    
    return render(request,"Empleados_Consulta.html", data)

@permission_required('Control_Calidad.change_empleados','Control_Calidad.delete_empleados')

def Empleados_Modificar_Eliminar_view(request):
    
    Registros_Empleados_Object = Empleados.objects.all()
    
    Filtros_Orde = OderFilter(request.POST, queryset = Registros_Empleados_Object )
    
    Orden = Filtros_Orde.qs
    
    data = {
        
        "Registros_Empleados_Object":Registros_Empleados_Object,
        
        "Filtros_Orde":Filtros_Orde,
        
        "Orden":Orden,
        }
    return render(request,"Empleados_Modificacion_e_Eliminacion.html", data)   


@permission_required('Control_Calidad.change_empleados','Control_Calidad.delete_empleados')
def Empleados_Modificar_view(request, id):
    
    Registros_Empleados_Object = get_object_or_404(Empleados, id=id)  
    
    data = {
        
        
        'form':Registros_empleados_form(instance = Registros_Empleados_Object)
        
        }
    
    if request.method == 'POST':
        Formulario = Registros_empleados_form(data = request.POST, instance = Registros_Empleados_Object , files = request.FILES )
        if Formulario.is_valid():
            Formulario.save()
            messages.success(request, 'MODIFICADO CORRECTAMENTE')
            return redirect(to = "Empleados_Modificar_Eliminar_view")
        else:
            messages.success(request, 'NO SE PUEDE MODIFICAR')
    
    return render(request , 'Empleados_Modificacion.html',data)

@permission_required('Control_Calidad.change_empleados','Control_Calidad.delete_empleados')
def Empleados_Eliminar_view(request, id):
    Registros_Empleados_Object = get_object_or_404(Empleados, id=id)    
    Registros_Empleados_Object.delete()
    return redirect(to = "Empleados_Modificar_Eliminar_view")
    
# =============================================================================
# 
# =============================================================================

@permission_required('Control_Calidad.view_almacen')
def Almacenes_Inicio_view(request):
    return render (request,"Almacen_Inicio.html")


@permission_required('Control_Calidad.add_almacen')

def Registro_Almacenes_View(request):
    data = {
        'form':Registros_almacenes_form()
        }
    if request.method == 'POST':
        Formulario = Registros_almacenes_form(data = request.POST)
        if Formulario.is_valid():
            Formulario.save()
            messages.success(request,"REGISTRO GUARDADO!!")
        else:
            data["form"] = Formulario
            
    return render(request, "Almacen_Alta.html",data)

@permission_required('Control_Calidad.view_almacen')
def Almacen_Consulta_View(request):  
    
    Registros_Almacenes_Object = Almacen.objects.all()
    
    Filtros_Orde = Oder_Filter_Almacen(request.POST, queryset = Registros_Almacenes_Object )
    
    Orden = Filtros_Orde.qs
    
    data = {
        
        "Registros_Almacenes_Object":Registros_Almacenes_Object,
        
        "Filtros_Orde":Filtros_Orde,
        
        "Orden":Orden,
        
        }
    
    return render(request,"Almacen_Consulta.html", data)
@permission_required('Control_Calidad.change_almacen','Control_Calidad.delete_almacen')

def Almacen_Modificar_Eliminar_view(request):
    
    Registros_Almacenes_Object = Almacen.objects.all()
    
    Filtros_Orde = Oder_Filter_Almacen(request.POST, queryset = Registros_Almacenes_Object )
    
    Orden = Filtros_Orde.qs
    
    data = {
        
        "Registros_Almacenes_Object":Registros_Almacenes_Object,
        
        "Filtros_Orde":Filtros_Orde,
        
        "Orden":Orden,
        
        }
    return render(request,"Almacen_Modificacion_e_Eliminacion.html", data)   

@permission_required('Control_Calidad.change_almacen','Control_Calidad.delete_almacen')

def Almacen_Modificar_view(request, id):
    
    Registros_Almacenes_Object = get_object_or_404(Almacen, id=id)  
    
    data = {
        
        
        'form':Registros_almacenes_form(instance = Registros_Almacenes_Object)
        
        }
    
    if request.method == 'POST':
        Formulario = Registros_almacenes_form(data = request.POST, instance = Registros_Almacenes_Object , files = request.FILES )
        if Formulario.is_valid():
            Formulario.save()
            messages.success(request, 'MODIFICADO CORRECTAMENTE')
            return redirect(to = "Almacen_Modificar_Eliminar_view")
        else:
            messages.success(request, 'NO SE PUEDE MODIFICAR')
    
    return render(request , 'Almacen_Modificacion.html',data)

@permission_required('Control_Calidad.change_almacen','Control_Calidad.delete_almacen')

def Almacen_Eliminar_view(request, id):
    
    Registros_Almacenes_Object = get_object_or_404(Almacen, id=id)  
    
    Registros_Almacenes_Object.delete()
    
    return redirect(to = "Almacen_Modificar_Eliminar_view")
# =============================================================================
# 
# =============================================================================

@permission_required('Control_Calidad.view_producto')
def Productos_Inicio_view(request):
    return render (request,"Producto_Inicio.html")

@permission_required('Control_Calidad.add_producto')
def Registro_Productos_View(request):
    
    data = {
        
        'form':Registros_Productos_form()
        
        }
    if request.method == 'POST':
        
        Formulario = Registros_Productos_form(data = request.POST)
        
        if Formulario.is_valid():
            
            Formulario.save()
            
            messages.success(request,"REGISTRO GUARDADO!!")
            
        else:
            
            data["form"] = Formulario
            
    return render(request, "Producto_Alta.html",data)

@permission_required('Control_Calidad.view_producto')
def Productos_Consulta_View(request):  
    
    Registros_Productos_Object = Producto.objects.all()
    
    Filtros_Orde = Oder_Filter_Productos(request.POST, queryset = Registros_Productos_Object )
    
    Orden = Filtros_Orde.qs
    
    data = {
        
        "Registros_Productos_Object":Registros_Productos_Object,
        
        "Filtros_Orde":Filtros_Orde,
        
        "Orden":Orden,
        
        }
    
    return render(request,"Producto_Consulta.html", data)

@permission_required('Control_Calidad.change_producto','Control_Calidad.delete_producto')

def Producto_Modificar_Eliminar_view(request):
    
    Registros_Productos_Object = Producto.objects.all()
    
    Filtros_Orde = Oder_Filter_Productos(request.POST, queryset = Registros_Productos_Object )
    
    Orden = Filtros_Orde.qs
    
    data = {
        
        "Registros_Productos_Object":Registros_Productos_Object,
        
        "Filtros_Orde":Filtros_Orde,
        
        "Orden":Orden,
        
        }
    return render(request,"Producto_Modificacion_e_Eliminacion.html", data)   

@permission_required('Control_Calidad.change_producto','Control_Calidad.delete_producto')

def Producto_Modificar_view(request, id):
    
    Registros_Productos_Object = get_object_or_404(Producto, id=id)  
    
    data = {
        
        
        'form':Registros_Productos_form(instance = Registros_Productos_Object)
        
        }
    
    if request.method == 'POST':
        
        Formulario = Registros_Productos_form(data = request.POST, instance = Registros_Productos_Object , files = request.FILES )
        
        if Formulario.is_valid():
            
            Formulario.save()
  
            messages.success(request, 'MODIFICADO CORRECTAMENTE')
            
            return redirect(to = "Producto_Modificar_Eliminar_view")
        
        else:
            messages.success(request, 'NO SE PUEDE MODIFICAR')
    
    return render(request , 'Producto_Modificacion.html',data)

@permission_required('Control_Calidad.change_producto','Control_Calidad.delete_producto')
def Producto_Eliminar_view(request, id):
    
    Registros_Productos_Object = get_object_or_404(Producto, id=id)  
    
    Registros_Productos_Object.delete()
    
    return redirect(to = "Producto_Modificar_Eliminar_view")
# =============================================================================
# 
# =============================================================================

@permission_required('Control_Calidad.view_calidad_control_lotes_registro')
def Control_de_Lotes_Inicio_view(request):
    return render (request,"Control_de_lotes_Inicio.html")

@permission_required('Control_Calidad.add_calidad_control_lotes_registro')

def Control_de_lotes_alta(request):
    
    data = {
        
        'form':Control_de_lotes_alta_form()
        
        }
    if request.method == 'POST':
        
        Formulario = Control_de_lotes_alta_form(data = request.POST)
        
        if Formulario.is_valid():
            
            Formulario.save()
            
            messages.success(request,"REGISTRO GUARDADO!!")
            
        else:
            
            data["form"] = Formulario
            
    return render(request, "Control_de_lotes_alta.html",data)

@permission_required('Control_Calidad.view_calidad_control_lotes_registro')

def Control_de_Lotes_Consulta_View(request):  
    
    Registros_Lotes_Object = Calidad_Control_Lotes_Registro.objects.all()
    
    Filtros_Orde = Oder_Filter_Control_Calidad(request.POST, queryset = Registros_Lotes_Object )
    
    Orden = Filtros_Orde.qs
    
    data = {
        
        "Registros_Lotes_Object":Registros_Lotes_Object,
        
        "Filtros_Orde":Filtros_Orde,
        
        "Orden":Orden,
        
        }
    
    return render(request,"Control_de_lotes_Consulta.html", data)

@permission_required('Control_Calidad.change_calidad_control_lotes_registro','Control_Calidad.delete_calidad_control_lotes_registro')

def Control_de_Lotes_Modificar_Eliminar_view(request):
    
    Registros_Lotes_Object = Calidad_Control_Lotes_Registro.objects.all()
    
    Filtros_Orde = Oder_Filter_Control_Calidad(request.POST, queryset = Registros_Lotes_Object )
    
    Orden = Filtros_Orde.qs
    
    data = {
        
        "Registros_Lotes_Object":Registros_Lotes_Object,
        
        "Filtros_Orde":Filtros_Orde,
        
        "Orden":Orden,
        
        }
    return render(request,"Control_de_Lotes_Modificacion_e_Eliminacion.html", data) 


@permission_required('Control_Calidad.view_calidad_control_lotes_registro','Control_Calidad.change_calidad_control_lotes_registro','Control_Calidad.delete_calidad_control_lotes_registro')

def Control_de_Lotes_Modificar_view(request, id):
    
    Registros_Lotes_Object = get_object_or_404(Calidad_Control_Lotes_Registro, id=id)  
    
    data = {
        
        
        'form':Control_de_lotes_alta_form(instance = Registros_Lotes_Object)
        
        }
    
    if request.method == 'POST':
        
        Formulario = Control_de_lotes_alta_form(data = request.POST, instance = Registros_Lotes_Object , files = request.FILES )
        
        if Formulario.is_valid():
            
            Formulario.save()
  
            messages.success(request, 'MODIFICADO CORRECTAMENTE')
            
            return redirect(to = "Control_de_Lotes_Modificar_Eliminar_view")
        else:
            messages.success(request, 'NO SE PUEDE MODIFICAR')
    
    return render(request , 'Control_de_Lotes_Modificacion.html',data)

@permission_required('Control_Calidad.change_calidad_control_lotes_registro','Control_Calidad.delete_calidad_control_lotes_registro')

def Control_de_Lotes_Eliminar_view(request, id):
    
    Registros_Lotes_Object = get_object_or_404(Calidad_Control_Lotes_Registro, id=id)  
    
    Registros_Lotes_Object.delete()
    
    return redirect(to = "Control_de_Lotes_Modificar_Eliminar_view")

# =============================================================================
# 
# =============================================================================
@permission_required('Control_Calidad.view_calidad_pruebas_registro')

def Pruebas_Inicio_view(request):
    return render (request,"Prueba_Inicio.html")

@permission_required('Control_Calidad.add_calidad_pruebas_registro')

def Pruebas_alta_view(request):   
    
    data = {
        
        'form':Registro_Pruebas_form()
        
        }
    if request.method == 'POST':
        
        Formulario = Registro_Pruebas_form(data = request.POST)
        
        if Formulario.is_valid():
            
            Formulario.save()
            
            messages.success(request,"REGISTRO GUARDADO!!")
            
        else:
            
            data["form"] = Formulario
            
    return render(request, "Prueba_Alta.html",data)

@permission_required('Control_Calidad.view_calidad_pruebas_registro')

def Prueba_Consulta_View(request):  
    
    Registros_Pruebas_Object = Calidad_Pruebas_Registro.objects.all()
    
    Filtros_Orde = Oder_Filter_Pruebas(request.POST, queryset = Registros_Pruebas_Object )
    
    Orden = Filtros_Orde.qs
    
    data = {
        
        "Registros_Pruebas_Object":Registros_Pruebas_Object,
        
        "Filtros_Orde":Filtros_Orde,
        
        "Orden":Orden,
        
        }
    
    return render(request,"Prueba_Consulta.html", data)

@permission_required('Control_Calidad.change_calidad_pruebas_registro','Control_Calidad.delete_calidad_pruebas_registro')

def Pruebas_Modificar_Eliminar_view(request): 
    
    Registros_Pruebas_Object = Calidad_Pruebas_Registro.objects.all()
    
    Filtros_Orde = Oder_Filter_Pruebas(request.POST, queryset = Registros_Pruebas_Object )
    
    Orden = Filtros_Orde.qs
    
    data = {
        
        "Registros_Pruebas_Object":Registros_Pruebas_Object,
        
        "Filtros_Orde":Filtros_Orde,
        
        "Orden":Orden,
        
        }
    return render(request,"Prueba_Modificacion_e_Eliminacion.html", data) 

@permission_required('Control_Calidad.change_calidad_pruebas_registro','Control_Calidad.delete_calidad_pruebas_registro')
def Pruebas_Modificar_view(request, id):
    
    Registros_Pruebas_Object = get_object_or_404(Calidad_Pruebas_Registro, id=id)  
    
    data = {
        
        'form':Registro_Pruebas_form(instance = Registros_Pruebas_Object)
        
        }
    
    if request.method == 'POST':
        
        Formulario = Registro_Pruebas_form(data = request.POST, instance = Registros_Pruebas_Object , files = request.FILES )
        
        if Formulario.is_valid():
            
            Formulario.save()
  
            messages.success(request, 'MODIFICADO CORRECTAMENTE')
            
            return redirect(to = "Pruebas_Modificar_Eliminar_view")
        else:
            messages.success(request, 'NO SE PUEDE MODIFICAR')
    
    return render(request , 'Prueba_Modificacion.html',data)

@permission_required('Control_Calidad.change_calidad_pruebas_registro','Control_Calidad.delete_calidad_pruebas_registro')

def Pruebas_Eliminar_view(request, id):
    
    Registros_Pruebas_Object = get_object_or_404(Calidad_Pruebas_Registro, id=id)  
    
    Registros_Pruebas_Object.delete()
    
    return redirect(to = "Pruebas_Modificar_Eliminar_view")

# =============================================================================
# 
# =============================================================================
@permission_required('Control_Calidad.view_calidad_liberacion_registro')

def Liberacion_Inicio_view(request):
    return render (request,"Liberacion_Inicio.html")

@permission_required('Control_Calidad.add_calidad_liberacion_registro')

def Liberacion_alta_view(request):   
    
    data = {
        
        'form':Registro_Liberacion_form()
        
        }
    if request.method == 'POST':
        
        Formulario = Registro_Liberacion_form(data = request.POST)
        
        if Formulario.is_valid():
            
            Formulario.save()
            
            messages.success(request,"REGISTRO GUARDADO!!")
            
        else:
            
            data["form"] = Formulario
            
    return render(request, "Prueba_Alta.html",data)

@permission_required('Control_Calidad.view_calidad_liberacion_registro')

def Liberacion_Consulta_View(request):  
    
    Registros_Liberacion_Object = Calidad_Liberacion_Registro.objects.all()
    
    Filtros_Orde = Oder_Filter_Liberacion(request.POST, queryset = Registros_Liberacion_Object )
    
    Orden = Filtros_Orde.qs
    
    data = {
        
        "Registros_Liberacion_Object":Registros_Liberacion_Object,
        
        "Filtros_Orde":Filtros_Orde,
        
        "Orden":Orden,
        
        }
    
    return render(request,"Liberacion_Consulta.html", data)

@permission_required('Control_Calidad.change_calidad_liberacion_registro','Control_Calidad.delete_calidad_liberacion_registro')

def Liberacion_Modificar_Eliminar_view(request): 
    
    Registros_Liberacion_Object = Calidad_Liberacion_Registro.objects.all()
    
    Filtros_Orde = Oder_Filter_Liberacion(request.POST, queryset = Registros_Liberacion_Object )
    
    Orden = Filtros_Orde.qs
    
    data = {
        
        "Registros_Liberacion_Object":Registros_Liberacion_Object,
        
        "Filtros_Orde":Filtros_Orde,
        
        "Orden":Orden,
        
        }
    return render(request,"Liberacion_Modificacion_e_Eliminacion.html", data) 

@permission_required('Control_Calidad.change_calidad_liberacion_registro','Control_Calidad.delete_calidad_liberacion_registro')


def Liberacion_Modificar_view(request, id):
    
    Registros_Liberacion_Object = get_object_or_404(Calidad_Liberacion_Registro, id=id)  
    
    data = {
        
        'form':Registro_Liberacion_form(instance = Registros_Liberacion_Object)
        
        }
    
    if request.method == 'POST':
        
        Formulario = Registro_Liberacion_form(data = request.POST, instance = Registros_Liberacion_Object , files = request.FILES )
        
        if Formulario.is_valid():
            
            Formulario.save()
  
            messages.success(request, 'MODIFICADO CORRECTAMENTE')
            
            return redirect(to = "Liberacion_Modificar_Eliminar_view")
        else:
            messages.success(request, 'NO SE PUEDE MODIFICAR')
    
    return render(request , 'Liberacion_Modificacion.html',data)

@permission_required('Control_Calidad.change_calidad_liberacion_registro','Control_Calidad.delete_calidad_liberacion_registro')


def Liberacion_Eliminar_view(request, id):
    
    Registros_Liberacion_Object = get_object_or_404(Calidad_Liberacion_Registro, id=id)  
    
    Registros_Liberacion_Object.delete()
    
    return redirect(to = "Liberacion_Modificar_Eliminar_view")

# =============================================================================
# 
# =============================================================================
@permission_required('Control_Calidad.change_calidad_liberacion_registro','Control_Calidad.delete_calidad_liberacion_registro')

def Pruebas_Template(request):
    return render(request,"Prueba_Template.html")
