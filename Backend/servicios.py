from conexion import conectar_db
from modelos import ( 
    UsuarioSchema,
    ServicioSchema,
    InsumoSchema,
    AtencionSchema,
    DetalleAtencionSchema
)    

# 1. Controlador de Usuarios (Administrador, Auxiliar, Contador)
# Obtener Usuarios

def obtener_usuarios():
    conexion = conectar_db()
    if conexion is None:
        return {"error": "No se pudo conectar a ala base de datos"}

    try:
        cursor = conexion.cursor()
        cursor.execute("select id_usuario, nombre, apellido, correo, contrasena, rol from usuarios;")
        registros = cursor.fetchall()    

        usuarios = []
        for fila in registros:
            usuarios.append({
                "id_usuario": fila[0],
                "nombre": fila[1],
                "apellido": fila[2],
                "correo": fila[3],
                "contrasena": fila[4],
                "rol": fila[5]
            })

        cursor.close()
        conexion.close()
        return usuarios
    except Exception as e:
        print(f"Error al obtener usuarios: {e}")   
        return {"error": "Error al consultar usuarios"}

# Crear Usuario
def crear_usuario(usuario: UsuarioSchema):
    conexion = conectar_db()
    if conexion is None:
        return {"error": "No se pudo conectar a la base de datos"}

    try:
        cursor = conexion.cursor()
        query = """
            insert into usuarios (nombre, apellido, correo, contrasena, rol)
            values (%s, %s, %s, %s, %s)
            returning id_usuario;
        """
        valores = (
            usuario.nombre,
            usuario.apellido,
            usuario.correo,
            usuario.contrasena,
            usuario.rol
        )
        cursor.execute(query, valores)
        id_generado = cursor.fetchone([0])
        conexion.commit()

        cursor.close()
        conexion.close()
        return{"mensaje": "Usuario creado exitosamente", "id_usuario": id_generado}
    except Exception as e:
        print(f"Error al crear usuario: {e}")
        return {"error": "No se pudo registrar el usuario"}


 # 2. Controlador de Servicios Médicos
 # Consultar servicio
def obtener_servicios():
    conexion = conectar_db()
    if conexion is None:
        return {"error" "No se pudo conectar a la base de datos"} 

    try:
        cursor = conexion.cursor()
        cursor.execute("select id_servicio, nombre_servicio, categoria, costo_base from servicios;")
        registros = cursor.fetchall()

        servicios = []
        for fila in registros:
            servicios.append({
                "id_servicio": fila[0],
                "nombre_servicio": fila[1],
                "categoria": fila[2], 
                "costo_base": float(fila[3])
            })       
        cursor.close()
        conexion.close()
        return servicios
    except Exception as e:
        print(f"Error al obtener servicios: {e}")
        return {"error": "Error al consultar servicios"}

# Crear servicio
def crear_servicio(servicio: ServicioSchema):
    conexion = conectar_db()
    if conexion is None:
        return {"error": "No se pudo conectar a la base de datos"}

    try:
        cursor = conexion.cursor()
        query = """
            INSERT INTO servicios (nombre_servicio, categoria, costo_base)
            VALUES (%s, %s, %s)
            RETURNING id_servicio;
        """
        valores = (servicio.nombre_servicio, servicio.categoria, servicio.costo_base)
        cursor.execute(query, valores)
        id_generado = cursor.fetchone()[0]
        conexion.commit()

        cursor.close()
        conexion.close()
        return {"mensaje": "Servicio médico creado con éxito", "id_servicio": id_generado}
    except Exception as e:
        print(f"Error al crear servicio: {e}")
        return {"error": "No se pudo registrar el servicio"}        


# 3. Controlador de Insumos
# Consultar Insumo 
def obtener_insumos():
    conexion = conectar_db()
    if conexion is None:
        return {"error": "No se pudo conectar a la base de datos"}

    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT id_insumo, nombre_insumo, costo_unitario, unidad_medida, stock FROM insumos;")
        registros = cursor.fetchall()

        insumos = []
        for fila in registros:
            insumos.append({
                "id_insumo": fila[0],
                "nombre_insumo": fila[1],
                "costo_unitario": float(fila[2]),
                "unidad_medida": fila[3],
                "stock": fila[4]
            })

        cursor.close()
        conexion.close()
        return insumos
    except Exception as e:
        print(f"Error al obtener insumos: {e}")
        return {"error": "Error al consultar insumos"} 

# Crear Insumo
def crear_insumo(insumo: InsumoSchema):
    conexion = conectar_db()
    if conexion is None:
        return {"error": "No se pudo conectar a la base de datos"}

    try:
        cursor = conexion.cursor()
        query = """
            INSERT INTO insumos (nombre_insumo, costo_unitario, unidad_medida, stock)
            VALUES (%s, %s, %s, %s)
            RETURNING id_insumo;
        """
        valores = (insumo.nombre_insumo, insumo.costo_unitario, insumo.unidad_medida, insumo.stock)
        cursor.execute(query, valores)
        id_generado = cursor.fetchone()[0]
        conexion.commit()

        cursor.close()
        conexion.close()
        return {"mensaje": "Insumo creado con éxito", "id_insumo": id_generado}
    except Exception as e:
        print(f"Error al crear insumo: {e}")
        return {"error": "No se pudo registrar el insumo"}
        

# 4. Controlador de Atenciones Médicas  
# Consultar Atenciones Médicas
def obtener_atenciones():
    conexion = conectar_db()
    if conexion is None:
        return {"error": "Nose puede conectar a la base de datos"}

    try:
        cursor = conexion.cursor()

        # JOIN con 'servicios' para mostrar el nombre del servicio además del id_servicio

        query = """
           select a.id_atencion, a.id_servicio, s.nombre_servicio, a.area_departamento, a.fecha_atencion, a.costo_total
           from atenciones a
           inner join servicios s on a.id_servicio = s.id_servicio
           """
        cursor.execute(query)
        registros = cursor.fetchall()

        atenciones = []
        for fila in registros:
            atenciones.append({
                "id_atencion": fila[0],
                "id_servicio": fila[1],
                "nombre_servicio": fila[2],
                "area_departamento": fila[3],
                "fecha_atencion": str(fila[4]),
                "costo_total": float(fila[5])
            })

        cursor.close()
        conexion.close()
        return atenciones
    except Exception as e:
        print(f"Error al obtener atenciones: {e}")
        return {"error": "Error al consultar atenciones"}

# Crear Atencion
def crear_atencion(atencion: AtencionSchema):
    conexion = conectar_db()
    if conexion is None:
        return {"error": "No se pudo conectar a la base de datos"}

    try:
        cursor = conexion.cursor()
        query = """
            INSERT INTO atenciones (id_servicio, area_departamento, fecha_atencion, costo_total)
            VALUES (%s, %s, %s, %s)
            RETURNING id_atencion;
        """
        valores = (
            atencion.id_servicio,
            atencion.area_departamento,
            atencion.fecha_atencion,
            atencion.costo_total
        )
        cursor.execute(query, valores)
        id_generado = cursor.fetchone()[0]
        conexion.commit()

        cursor.close()
        conexion.close()
        return {"mensaje": "Atención médica registrada con éxito", "id_atencion": id_generado}
    except Exception as e:
        print(f"Error al registrar atención: {e}")
        return {"error": "No se pudo registrar la atención médica"}    


# 5. Controlador de Detalle de Insumos por Atención
# Consultar Detalle de Insumos por Atención 
def obtener_atencion_insumos():
    conexion = conectar_db()
    if conexion is None:
        return {"error": "No se pudo conectar con la base de datos"}

    try:
        cursor = conexion.cursor()

  # Hacemos JOIN con 'insumos' para incluir el nombre del material usado
        query = """
            SELECT ai.id_detalle, ai.id_atencion, ai.id_insumo, i.nombre_insumo, ai.cantidad, ai.subtotal_insumo
            FROM atencion_insumos ai
            INNER JOIN insumos i ON ai.id_insumo = i.id_insumo;
        """
        cursor.execute(query)
        registros = cursor.fetchall()

        detalles = []
        for fila in registros:
            detalles.append({
                "id_detalle": fila[0],
                "id_atencion": fila[1],
                "id_insumo": fila[2],
                "nombre_insumo": fila[3],
                "cantidad": fila[4],
                "subtotal_insumo": float(fila[5])
            })

        cursor.close()
        conexion.close()
        return detalles
    except Exception as e:
        print(f"Error al obtener detalle de insumos: {e}")
        return {"error": "Error al consultar detalles de insumos"}

# Crear Detalle de Insumo porr Atención
def crear_detalle_atencion(detalle: DetalleAtencionSchema):
    conexion = conectar_db()
    if conexion is None:
        return {"error": "No se pudo conectar a la base de datos"}

    try:
        cursor = conexion.cursor()
        query = """
            INSERT INTO atencion_insumos (id_atencion, id_insumo, cantidad, subtotal_insumo)
            VALUES (%s, %s, %s, %s)
            RETURNING id_detalle;
        """
        valores = (
            detalle.id_atencion,
            detalle.id_insumo,
            detalle.cantidad,
            detalle.subtotal_insumo
        )
        cursor.execute(query, valores)
        id_generado = cursor.fetchone()[0]
        conexion.commit()

        cursor.close()
        conexion.close()
        return {"mensaje": "Detalle de insumo registrado con éxito", "id_detalle": id_generado}
    except Exception as e:
        print(f"Error al registrar detalle de insumo: {e}")
        return {"error": "No se pudo registrar el detalle del insumo"}
