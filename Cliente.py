import requests

logueado = False

while True:
    if not logueado:
        print("1. Registrarse")
        print("2. Login")
        print("3. Salir")
        opcion = input("Elegí una opción: ") #acá no se muestran las tareas porque no se hizo el login

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
                logueado = True

        elif opcion == "3":
            print("Chauuu")
            break

        else:
            print("Seleccioná una opción válida")

    else:
        print("1. Ver tareas")
        print("2. Salir")
        opcion = input("Elegí una opción: ") #esta opción solo se activa al hacer el login

        if opcion == "1":
            res = requests.get("http://127.0.0.1:5000/tareas")
            print(res.text)

        elif opcion == "2":
            print("Chauuu")
            break

        else:
            print("Elegí una opción válida")