import sqlite3
import os
from flask import Flask, request
from werkzeug.security import generate_password_hash, check_password_hash
app = Flask(__name__)
print(app.url_map) 

@app.route('/')
def index():
    return "Servidor funcionando"

def index():
    return



PATH_APP = os.getcwd()
PATH_BBDD = os.path.join(PATH_APP, 'miBBDD.db')

con = sqlite3.connect(PATH_BBDD)
cursor = con.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        usuario TEXT PRIMARY KEY NOT NULL, 
        contraseña TEXT NOT NULL
    )
""")
con.commit()



@app.route('/registro', methods=['POST'])
def registrar_usuario():
    data = request.get_json()
    usuario = data['usuario']
    contraseña = data['contraseña']

    hash_contraseña = generate_password_hash(contraseña)

    try:
        cursor.execute(
            "INSERT INTO usuarios (usuario, contraseña) VALUES (?, ?)",
            (usuario, hash_contraseña)
        )
        con.commit()
        return{"mensaje": "Usuario registrado"}
    except sqlite3.IntegrityError:
        return{"mensaje": "Usuario ya existe"}

@app.route('/login', methods=['POST'])
def iniciar_sesion():
    data = request.get_json()
    usuario = data['usuario']
    contraseña = data['contraseña']

    cursor.execute(
        "SELECT contraseña FROM usuarios WHERE usuario = ?",
        (usuario,)
    )
    resultado = cursor.fetchone()

    if resultado:
        hash_guardado = resultado[0]
        if check_password_hash(hash_guardado, contraseña):
            return {"mensaje": "Login exitoso"}
        else:
            return {"mensaje": "Usuario o contraseña incorrectos"}
    else:
            return {"mensaje": "Usuario o contraseña incorrectos"}


@app.route('/tareas', methods=['GET'])
def tareas():
    return "<h1>Bienvenido/a</h1> <br><h2>Este es el PFO 2 de Eugenia Lucchelli</h2>"    


if __name__ =="__main__":
    app.run(debug=True)
con.close()
