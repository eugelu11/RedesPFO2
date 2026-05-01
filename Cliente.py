import requests

logueado = False

while True:
    print("1. Registrarse")
    print("2. Login")
    if logueado:
        print("3. Ver tareas")

    opcion = input("Elegí una opción: ")

    if opcion == "1":
        usuario = input("Usuario: ")
        contraseña = input("Contraseña: ")
        res = requests.post("http://127.0.0.1:5000/registro", json={
            "usuario": usuario,
            "contraseña": contraseña
        })
        print(res.json())

    elif opcion == "2":
        usuario = input("Usuario: ")
        contraseña = input("Contraseña: ")
        res = requests.post("http://127.0.0.1:5000/login", json={
            "usuario": usuario,
            "contraseña": contraseña
        })
        datos = res.json()
        print(datos)
        if datos["mensaje"] == "Login exitoso":
            logueado = True  # recien cuando uno se loguea se habilita la opción de tareas

    elif opcion == "3":
        if not logueado:
            print("Tenés que hacer login primero.")
        else:
            res = requests.get("http://127.0.0.1:5000/tareas")
            print(res.text)

    else:
        print("Seleccioná una opción válida")