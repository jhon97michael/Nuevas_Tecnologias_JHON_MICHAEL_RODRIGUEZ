# Lista para almacenar la información de los usuarios
usuarios = []

# Diccionario para almacenar la información de las bicicletas disponibles
bicicletas_disponibles = {"bicicleta1": {"origen": None, "destino": None},
                          "bicicleta2": {"origen": None, "destino": None},
                          "bicicleta3": {"origen": None, "destino": None}}

# Función para registrar un usuario
def registrar_usuario():
    nombre = input("Ingrese su nombre: ")
    tarjeta = input("Ingrese su número de tarjeta: ")
    usuarios.append({"nombre": nombre, "tarjeta": tarjeta})

# Función para que un usuario tome una bicicleta
def tomar_bicicleta():
    tarjeta = input("Ingrese su número de tarjeta: ")
    if any(usuario["tarjeta"] == tarjeta for usuario in usuarios):
        
        origen = input("Ingrese el origen: ")
        destino = input("Ingrese el destino: ")
        bicicletas_disponibles[bicicleta]["origen"] = origen
        bicicletas_disponibles[bicicleta]["destino"] = destino
        print(f"Ha tomado la bicicleta {bicicleta} desde {origen} hasta {destino}.")
    else:
        print("Usuario no registrado.")

# Función para consultar información de una bicicleta
def consultar_bicicleta(bicicleta):
    info = bicicletas_disponibles.get(bicicleta)
    if info:
        print(f"Bicicleta {bicicleta}: Origen: {info['origen']}, Destino: {info['destino']}")
    else:
        print(f"Bicicleta {bicicleta} no encontrada.")

# Bucle para interactuar con el sistema
while True:
    print("\nSeleccione una opción:")
    print("1. Registrar usuario")
    print("2. Tomar bicicleta")
    print("3. Consultar información de bicicleta")
    print("4. Salir")
    
    opcion = input("Ingrese el número de la opción: ")
    
    if opcion == "1":
        registrar_usuario()
    elif opcion == "2":
        tomar_bicicleta()
    elif opcion == "3":
        bicicleta = input("Ingrese el nombre de la bicicleta: ")
        consultar_bicicleta(bicicleta)
    elif opcion == "4":
        break
    else:
        print("Opción no válida. Por favor, ingrese una opción válida.")