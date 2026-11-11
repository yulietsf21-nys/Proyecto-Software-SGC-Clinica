from servicios import (
    obtener_usuarios, crear_usuario, modificar_usuario, eliminacion_logica_usuario,
    obtener_servicios, crear_servicio,
    obtener_insumos, crear_insumo,
    obtener_atenciones, crear_atencion, modificar_atencion, eliminar_atencion,
    obtener_atencion_insumos, crear_detalle_atencion
)

# Controladores para llamar a servicios
# 1. Usuarios
def obtener_usuarios_db():
    return obtener_usuarios()

def crear_usuario_db(usuario):
    return crear_usuario(usuario)

def actualizar_usuario_db(usuario_id, usuario):
    return modificar_usuario(usuario_id, usuario)

def eliminar_usuario_db(usuario_id):
    return eliminacion_logica_usuario(usuario_id)

# 2. Servicios
def obtener_servicios_db():
    return obtener_servicios()
 
def crear_servicio_db(servicio):
    return crear_servicio(servicio)

# 3. Insumos
def obtener_insumos_db():
    return obtener_insumos()

def crear_insumo_db(insumo):
    return crear_insumo(insumo)

# 4. Atenciones
def obtener_atenciones_db():
    return obtener_atenciones()

def crear_atencion_db(atencion):
    return crear_atencion(atencion)

def modificar_atencion_db(atencion_id, atencion):
    return modificar_atencion(atencion_id, atencion)

def eliminar_atencion_db(atencion_id):
    return eliminar_atencion(atencion_id)

# 5. Detalle de Insumos
def obtener_atencion_insumos_db():
    return obtener_atencion_insumos()

def crear_detalle_atencion_db(detalle):
    return crear_detalle_atencion(detalle)
    





