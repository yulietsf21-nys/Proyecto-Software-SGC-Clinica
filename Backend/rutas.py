from fastapi import APIRouter
from modelos import (
    UsuarioSchema,
    ServicioSchema,
    InsumoSchema,
    AtencionSchema,
    DetalleAtencionSchema
)

from controladores import (
    obtener_usuarios, crear_usuario,
    obtener_servicios, crear_servicio,
    obtener_insumos, crear_insumo,
    obtener_atenciones, crear_atencion,
    obtener_atencion_insumos, crear_detalle_atencion
)

# Crear enrutador para agrupar Endpoints
router = APIRouter()

# Rutas Usuarios
@router.get("/usuarios")
def ver_usuarios():
    return obtener_usuarios()

@router.post("/usuarios")
def registrar_usuario(usuario: UsuarioSchema):
    return crear_usuario(usuario)

# Rutas de Servicios Médicos
@router.get("/servicios")
def ver_servicios():
    return obtener_servicios()

@router.post("/servicios")
def registrar_servicio(servicio: ServicioSchema):
    return crear_servicio(servicio)

# Rutas de Insumos
@router.get("/insumos")
def ver_insumos():
    return obtener_insumos()

@router.post("/insumos")
def registrar_insumo(insumo: InsumoSchema):
    return crear_insumo(insumo)

# Rutas Atenciones Médicas
@router.get("/atenciones")
def ver_atenciones():
    return obtener_atenciones()

@router.post("/atenciones")
def registrar_atencion(atencion: AtencionSchema):
    return crear_atencion(atencion)

# Rutas de Atención e Insumos
@router.get("/atencion_insumos")
def ver_atencion_insumos():
    return obtener_atencion_insumos()

@router.post("/atencion_insumos")
def registrar_detalle_atencion(detalle: DetalleAtencionSchema):
    return crear_detalle_atencion(detalle)