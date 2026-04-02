import sqlite3
import os
from werkzeug.security import generate_password_hash, check_password_hash

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

usuario_ejemplo = "admin"
contraseña_ejemplo = "1234"
hash_ejemplo = generate_password_hash(contraseña_ejemplo)

try:
    cursor.execute(
        "INSERT INTO usuarios (usuario, contraseña) VALUES (?, ?)",
        (usuario_ejemplo, hash_ejemplo)
    )
    con.commit()
    print("Usuario de ejemplo creado")
except sqlite3.IntegrityError:
    print("El usuario ya existe")


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


iniciar_sesion()
con.close()
