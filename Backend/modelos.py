from pydantic import BaseModel
from datetime import date
from typing import Optional

# Modelo para usuarios
class UsuarioSchema(BaseModel):
    nombre: str
    apellido: str
    correo: str
    contrasena: str
    rol: str = "Auxiliar"

# Modelo para Servicios Médicos
class ServicioSchema(BaseModel):
    nombre_servicio: str
    categoria: str
    costo_base: float


# Modelo para Insumos
class InsumoSchema(BaseModel):
    nombre_insumo: str
    costo_unitario: float
    unidad_medida: str
    stock: int

# Modelo para Atenciones Médicas
class AtencionSchema(BaseModel):
    id_servicio: int
    area_departamento: str
    fecha_atencion: date
    costo_total: float

# Modelo para Detalle de Insumos por Atención
class DetalleAtencionSchema(BaseModel):
    id_atencion: int
    id_insumo: int
    cantidad: int
    subtotal_insumo: float         
