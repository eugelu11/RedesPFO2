import requests

while True:
    print("1. Registrarse")
    print("2. Login")
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
        print(res.json())
        

    elif opcion == "3": 
        res=requests.get("http://127.0.0.1:5000/tareas")
    
        print(res.text)

    else: print("Seleccioná una opción valida")