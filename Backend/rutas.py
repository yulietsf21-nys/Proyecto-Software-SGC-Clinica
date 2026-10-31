from fastapi import APIRouter
from modelos import (
    UsuarioSchema,
    ServicioSchema,
    InsumoSchema,
    AtencionSchema,
    DetalleAtencionSchema
)

# Importamos todas las funciones necesarias desde controladores con el sufijo _db
from controladores import (
    obtener_usuarios_db, crear_usuario_db, actualizar_usuario_db, eliminar_usuario_db,
    obtener_servicios_db, crear_servicio_db,
    obtener_insumos_db, crear_insumo_db,
    obtener_atenciones_db, crear_atencion_db,
    obtener_atencion_insumos_db, crear_detalle_atencion_db
)

# Crear enrutador para agrupar Endpoints
router = APIRouter()

# Rutas Usuarios
@router.get("/usuarios")
def ver_usuarios():
    return obtener_usuarios_db()

@router.post("/usuarios")
def registrar_usuario(usuario: UsuarioSchema):
    return crear_usuario_db(usuario)

@router.put("/usuarios/{usuario_id}")
def actualizar_usuario(usuario_id: int, usuario: UsuarioSchema):
    return actualizar_usuario_db(usuario_id, usuario)

@router.delete("/usuarios/{usuario_id}")
def eliminar_usuario(usuario_id: int):
    return eliminar_usuario_db(usuario_id)


# Rutas de Servicios Médicos
@router.get("/servicios")
def ver_servicios():
    return obtener_servicios_db()

@router.post("/servicios")
def registrar_servicio(servicio: ServicioSchema):
    return crear_servicio_db(servicio)


# Rutas de Insumos
@router.get("/insumos")
def ver_insumos():
    return obtener_insumos_db()

@router.post("/insumos")
def registrar_insumo(insumo: InsumoSchema):
    return crear_insumo_db(insumo)


# Rutas Atenciones Médicas
@router.get("/atenciones")
def ver_atenciones():
    return obtener_atenciones_db()

@router.post("/atenciones")
def registrar_atencion(atencion: AtencionSchema):
    return crear_atencion_db(atencion)


# Rutas de Atención e Insumos
@router.get("/atencion_insumos")
def ver_atencion_insumos():
    return obtener_atencion_insumos_db()

@router.post("/atencion_insumos")
def registrar_detalle_atencion(detalle: DetalleAtencionSchema):
    return crear_detalle_atencion_db(detalle)