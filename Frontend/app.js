const API_URL = 'http://127.0.0.1:8000';
let editandoId = null;

async function cargarUsuarios() {
    try {
        const respuesta = await fetch(`${API_URL}/usuarios`);
        const usuarios = await respuesta.json();
        
        const tbody = document.getElementById('tablaUsuarios');
        if (!tbody) return;
        
        tbody.innerHTML = '';
        
        usuarios.forEach(u => {
            const userId = u.id || u.id_usuario || u.usuario_id;

            tbody.innerHTML += `
                <tr>
                    <td>${userId}</td>
                    <td>${u.nombre}</td>
                    <td>${u.apellido || ''}</td>
                    <td>${u.correo}</td>
                    <td>${u.rol || 'Auxiliar'}</td>
                    <td class="text-center">
                        <button class="btn btn-warning btn-sm me-1" onclick="prepararEdicion(${userId}, '${u.nombre}', '${u.apellido || ''}', '${u.correo}', '${u.rol || 'Auxiliar'}')">Editar</button>
                        <button class="btn btn-danger btn-sm" onclick="eliminarUsuario(${userId})">Eliminar</button>
                    </td>
                </tr>
            `;
        });
    } catch (error) {
        console.error("Error al obtener usuarios:", error);
    }
}

const formUsuario = document.getElementById('formUsuario');
if (formUsuario) {
    formUsuario.addEventListener('submit', async (e) => {
        e.preventDefault();

        const id = document.getElementById('usuarioId').value;
        const datosUsuario = {
            nombre: document.getElementById('nombre').value,
            apellido: document.getElementById('apellido').value,
            correo: document.getElementById('correo').value,
            contrasena: document.getElementById('contrasena').value || "123456",
            rol: document.getElementById('rol').value || "Auxiliar"
        };

        let url = `${API_URL}/usuarios`;
        let metodo = 'POST';

        if (id) {
            url = `${API_URL}/usuarios/${id}`;
            metodo = 'PUT';
        }

        try {
            const respuesta = await fetch(url, {
                method: metodo,
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(datosUsuario)
            });

            if (respuesta.ok) {
                alert(id ? '¡Usuario actualizado con éxito!' : '¡Usuario registrado con éxito!');
                limpiarFormulario();
                cargarUsuarios();
            } else {
                alert('Ocurrió un error al procesar la solicitud.');
            }
        } catch (error) {
            console.error('Error en la petición:', error);
        }
    });
}

function prepararEdicion(id, nombre, apellido, correo, rol) {
    document.getElementById('usuarioId').value = id;
    document.getElementById('nombre').value = nombre;
    document.getElementById('apellido').value = apellido;
    document.getElementById('correo').value = correo;
    document.getElementById('rol').value = rol;
    document.getElementById('contrasena').value = '';

    document.getElementById('btnGuardar').innerText = "Actualizar Usuario";
    document.getElementById('btnGuardar').className = "btn btn-warning";
    const btnCancelar = document.getElementById('btnCancelar');
    if (btnCancelar) btnCancelar.style.display = 'inline-block';
}

function limpiarFormulario() {
    document.getElementById('formUsuario').reset();
    document.getElementById('usuarioId').value = '';
    document.getElementById('btnGuardar').innerText = "Guardar Usuario";
    document.getElementById('btnGuardar').className = "btn btn-success";
    const btnCancelar = document.getElementById('btnCancelar');
    if (btnCancelar) btnCancelar.style.display = 'none';
}

async function eliminarUsuario(id) {
    if (confirm("¿Estás seguro de que deseas desactivar este usuario?")) {
        try {
            const respuesta = await fetch(`${API_URL}/usuarios/${id}`, {
                method: 'DELETE'
            });
            
            if (respuesta.ok) {
                alert("¡Usuario desactivado exitosamente!");
                cargarUsuarios();
            } else {
                alert("Error al intentar desactivar el usuario.");
            }
        } catch (error) {
            console.error("Error de red:", error);
        }
    }
}

window.onload = cargarUsuarios;