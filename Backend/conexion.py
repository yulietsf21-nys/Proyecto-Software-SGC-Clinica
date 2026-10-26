import psycopg2
from psycopg2 import Error

def conectar_db():
    try:
        conexion = psycopg2.connect(
            database="db_sgco",
            user="postgres",
            password="1234",
            host="localhost",
            port="5432"
        )

        print("¡Conexión exitosa a la base de datos!")
        return conexion
    
    except Error as e:
        print(f"Error al conectar a PosgrestSQL: {e}")
        return None
if __name__ == "__main__":
    conectar_db()