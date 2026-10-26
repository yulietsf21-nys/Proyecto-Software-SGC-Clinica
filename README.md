# Sistema de Gestión de Costos (SGC) - Clínica

Proyecto desarrollado como parte de la formación en análisis y desarrollo de software, implementando una arquitectura modular por capas para el control de atenciones, insumos, servicios y usuarios de una clínica.

## Tecnologías Utilizadas
* **Backend:** Python, FastAPI, Uvicorn, Pydantic, psycopg2.
* **Base de Datos:** PostgreSQL (`db_sgco`).
* **Frontend:** HTML5, CSS3, Bootstrap 5, JavaScript (Fetch API).

## Estructura del Proyecto
* `/Backend`: Contiene la lógica de la API REST, modelos de datos, controladores y rutas.
* `/Frontend`: Contiene la interfaz gráfica de usuario y la navegación básica.

## Cómo Ejecutar el Proyecto

### 1. Ejecutar el Backend
1. Abre una terminal en la carpeta `Backend`.
2. Instala las dependencias necesarias:
   ```bash
   python -m pip install uvicorn fastapi psycopg2-binary pydantic