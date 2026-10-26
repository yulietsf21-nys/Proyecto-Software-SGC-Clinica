// Función para consultar los usuarios desde el Backend de FastAPI
async function cargarUsuarios() {
    try {
        // Hacemos la petición GET a tu endpoint de FastAPI
        const respuesta = await fetch('http://127.0.0.1:8000/usuarios');
        
        // Convertimos la respuesta a formato JSON
        const datos = await respuesta.json();
        
        console.log("Usuarios obtenidos de la Base de Datos:", datos);
        
        // Aquí puedes pintar los datos en una tabla de tu HTML si lo deseas
    } catch (error) {
        console.error("Error al conectar con el backend:", error);
    }
}

// Ejecutar la función al cargar la página
window.onload = cargarUsuarios;