function Eliminar_Registro(id) {
Swal.fire({
  title: '¿QUIERES GUARDAS LOS CAMBIOS?',
  showDenyButton: true,
  confirmButtonText: `GUARDAR`,
  denyButtonText: `CANCELAR`,
}).then((result) => {
  if (result.isConfirmed) {
    window.location.href="/Empleados_Eliminar_view/"+id+"/";
    Swal.fire('GUARDADO!', '', 'CORRECTO')
  } else if (result.isDenied) {
    Swal.fire('LOS CAMBIOS NO SE GUARDARON', '', 'info')
  }
})
}

function Eliminar_Registro_Al(id) {
Swal.fire({
  title: '¿QUIERES GUARDAS LOS CAMBIOS?',
  showDenyButton: true,
  confirmButtonText: `GUARDAR`,
  denyButtonText: `CANCELAR`,
}).then((result) => {
  if (result.isConfirmed) {
    window.location.href="/Almacen_Eliminar_view/"+id+"/";
    Swal.fire('GUARDADO!', '', 'CORRECTO')
  } else if (result.isDenied) {
    Swal.fire('LOS CAMBIOS NO SE GUARDARON', '', 'info')
  }
})
}

function Eliminar_Registro_Pr(id) {
Swal.fire({
  title: '¿QUIERES GUARDAS LOS CAMBIOS?',
  showDenyButton: true,
  confirmButtonText: `GUARDAR`,
  denyButtonText: `CANCELAR`,
}).then((result) => {
  if (result.isConfirmed) {
    window.location.href="/Producto_Eliminar_view/"+id+"/";
    Swal.fire('GUARDADO!', '', 'CORRECTO')
  } else if (result.isDenied) {
    Swal.fire('LOS CAMBIOS NO SE GUARDARON', '', 'info')
  }
})
}
function Eliminar_Registro_CT_LT(id) {
Swal.fire({
  title: '¿QUIERES GUARDAS LOS CAMBIOS?',
  showDenyButton: true,
  confirmButtonText: `GUARDAR`,
  denyButtonText: `CANCELAR`,
}).then((result) => {
  if (result.isConfirmed) {
    window.location.href="/Control_de_Lotes_Eliminar_view/"+id+"/";
    Swal.fire('GUARDADO!', '', 'CORRECTO')
  } else if (result.isDenied) {
    Swal.fire('LOS CAMBIOS NO SE GUARDARON', '', 'info')
  }
})
}
function Eliminar_Registro_PR(id) {
Swal.fire({
  title: '¿QUIERES GUARDAS LOS CAMBIOS?',
  showDenyButton: true,
  confirmButtonText: `GUARDAR`,
  denyButtonText: `CANCELAR`,
}).then((result) => {
  if (result.isConfirmed) {
    window.location.href="/Pruebas_Eliminar_view/"+id+"/";
    Swal.fire('GUARDADO!', '', 'CORRECTO')
  } else if (result.isDenied) {
    Swal.fire('LOS CAMBIOS NO SE GUARDARON', '', 'info')
  }
})
}
function Eliminar_Registro_Lb(id) {
Swal.fire({
  title: '¿QUIERES GUARDAS LOS CAMBIOS?',
  showDenyButton: true,
  confirmButtonText: `GUARDAR`,
  denyButtonText: `CANCELAR`,
}).then((result) => {
  if (result.isConfirmed) {
    window.location.href="/Liberacion_Eliminar_view/"+id+"/";
    Swal.fire('GUARDADO!', '', 'CORRECTO')
  } else if (result.isDenied) {
    Swal.fire('LOS CAMBIOS NO SE GUARDARON', '', 'info')
  }
})
}


