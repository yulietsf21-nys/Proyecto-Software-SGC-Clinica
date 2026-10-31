from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from rutas import router

# Importamos los esquemas de Pydantic
from modelos import (
    UsuarioSchema,
    ServicioSchema,
    InsumoSchema,
    AtencionSchema,
    DetalleAtencionSchema
)

# Iniciar FastAPI
app = FastAPI(
    title="API Sistema de Gestión de Costos (SGC) - Clínica",
    description="Backend en FastAPI para la gestión de costos operativos médicos",
    version="1.0.0"
)

# Configurar CORS (Conectar React - FastAPI)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Ruta raíz
@app.get("/")
def ruta_raiz():
    return {"mensaje": "¡Bienvenido al Backend del Sistema de Gestión de Costos de la Clínica!"}

# Incluir todas las rutas
app.include_router(router)