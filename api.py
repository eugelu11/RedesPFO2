import sqlite3
import os
from flask import Flask
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__SISTEMA DE LOGIN__)

@app.route('/')

def index():
    return


if __SISTEMA DE LOGIN__ =="__main__":
    app.run(debug=True)

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


def registrar_usuario():
    print("\n--- REGISTRO ---")
    usuario = input("Ingrese su usuario: ")
    contraseña = input("Ingrese su contraseña: ")

    hash_contraseña = generate_password_hash(contraseña)

    try:
        cursor.execute(
            "INSERT INTO usuarios (usuario, contraseña) VALUES (?, ?)",
            (usuario, hash_contraseña)
        )
        con.commit()
        print("Usuario registrado exitosamente")
    except sqlite3.IntegrityError:
        print("Ese usuario ya existe")


def iniciar_sesion():
    print("\n--- LOGIN ---")
    usuario = input("Ingrese su usuario: ")
    contraseña = input("Ingrese su contraseña: ")

    cursor.execute(
        "SELECT contraseña FROM usuarios WHERE usuario = ?",
        (usuario,)
    )
    resultado = cursor.fetchone()

    if resultado:
        hash_guardado = resultado[0]
        if check_password_hash(hash_guardado, contraseña):
            print("Login exitoso")
            return True
        else:
            print("Contraseña incorrecta")
            return False
    else:
        print("Usuario no encontrado")
        return False


while True:
    print("\n=== SISTEMA DE LOGIN ===")
    print("1. Registrarse")
    print("2. Iniciar sesion")
    print("3. Salir")

    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        registrar_usuario()
    elif opcion == "2":
        if iniciar_sesion():
            print("Bienvenido/a a la plataforma")
            break
    elif opcion == "3":
        break
    else:
        print("Opcion invalida")

con.close()
