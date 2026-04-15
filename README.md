# PFO 2 - Sistema de Gestión de Tareas con API y Base de Datos:
# Respuestas conceptuales (ver abajo cómo correr):
## 1. 
Las contraseñas deben ser hasheadas por seguridad: en caso de haber alguna vulnerabilidad en el sistema si las contraseñas fueran almacenadas como texto plano quienes realicen el ataque pueden acceder fácilmente a las contraseñas. En cambio al hashearlas las contraseñas se convierten en strings que son únicos y a partir de los cuales no se puede revertir para conocer la contraseña.

## 2.
En nuestro caso SQLite es ideal porque no necesitamos servers, si no que se puede usar el almacenamiento local sin necesidad de configuración. SQLite se puede usar más que nada en proyectos chicos como es nuestro caso. 



## Descripción

Este proyecto consiste en el desarrollo de una API REST utilizando Flask que permite:

* Registrar usuarios
* Iniciar sesión
* Acceder a una vista de tareas

Los datos se almacenan en una base de datos SQLite y las contraseñas se guardan de forma segura mediante hashing.

Además, se incluye un cliente en consola que interactúa con la API mediante requests HTTP.

---

## Tecnologías utilizadas

* Python 3
* Flask
* SQLite
* Requests
* Werkzeug (hash de contraseñas)

---

## Estructura del proyecto

```
/proyecto
│── Servidor.py
│── cliente.py
│── miBBDD.db (se crea automáticamente)
│── README.md
```

---

## Instalación

1. Clonar el repositorio o descargar los archivos
2. Abrir una terminal en la carpeta del proyecto
3. Instalar dependencias:

```bash
py -m pip install flask requests werkzeug
```

---

## Ejecución

### 1. Iniciar el servidor

En una terminal:

```bash
py Servidor.py
```

Deberías ver:

```
Running on http://127.0.0.1:5000
```

---

### 2. Probar en el navegador

Abrir:

```
http://127.0.0.1:5000/tareas
```

Esto mostrará la página HTML de bienvenida.

---

### 3. Ejecutar el cliente

En otra terminal (con el servidor corriendo):

```bash
py cliente.py
```

---

## Uso del cliente

El programa mostrará un menú:

```
1. Registrarse
2. Login
3. Ver tareas
```

### Registrarse

Permite crear un nuevo usuario en la base de datos.

### Login

Verifica las credenciales ingresadas.

### Ver tareas

Muestra el contenido HTML del endpoint `/tareas`.

---

## Seguridad

Las contraseñas se almacenan utilizando hashing con `werkzeug.security`, lo que evita guardar información sensible en texto plano.

---

## Base de datos

Se utiliza SQLite, una base de datos ligera basada en archivos que no requiere configuración adicional ni servidor.

---

## Notas

* La base de datos se crea automáticamente al ejecutar el servidor por primera vez.
* El servidor debe estar en ejecución antes de usar el cliente.
* El sistema está diseñado para fines educativos.

---

## Autora

Eugenia Lucchelli

---

## Estado del proyecto

API funcional
Base de datos persistente
Cliente en consola
Autenticación básica implementada
