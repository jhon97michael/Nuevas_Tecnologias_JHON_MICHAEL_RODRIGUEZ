#Se requiere una funcionalidad para el sistema de prestamos de cliclas de la ciudad, el sistema debe:
#1. Registrar los usuarios, debe permitir agregarlos a una base de datos (lista).
#2. El usuario con  el numero de tarjeta podra tomar una cicla.
#3. El usuario debe poder tomar la cicla indicando el origen y el destino de la misma.
#Usando los conocimientos en Python adquiridos, cree una funcionalidad que permita guardar esta informacion y consultarla. en una aplicación.

#base de datos
bd_usuarios=[]
bicis_disponibles = {"bici1":{"origen":None, "destino":None},"bici2":{"origen":None, "destino":None},"bici3":{"origen":None, "destino":None}}

#Funcion para registrar usuarios
def agregar_usuario():
    num_tarjeta=input("Ingrese su número de tarjeta: ")
    nombre=input("Ingrese su nombre: ")
    apellido=input("Ingrese su apellido: ")
    correo=input("Ingrese su correo electronico: ")
    bd_usuarios.append({"num_tarjeta": num_tarjeta, "nombre":nombre,"apellido":apellido,"correo":correo})

def prestar_bici():
    tarjeta=input("Ingresa su numero de tarjeta: ")
    if any(usuario["num_tarjeta"] == tarjeta for usuario in bd_usuarios):
        origen = input("Ingrese su origen: ")
        destino = input("Ingrese su destino: ")
        bicis_disponibles[bicicleta]["origen"]=origen
        bicis_disponibles[bicicleta]["destino"]=destino
        print(f"Has tomado la {bicicleta} desde {origen} hasta {destino}")
    else:
        print("Usuario no registrado.")

def consultar_bici(bicicleta):
    info=bicis_disponibles.get(bicicleta)
    if info:
        print(f"Bicicleta {bicicleta}: origen: {info['origen']} destino: {info['destino']}")
    else:
        print(f"Bicicleta {bicicleta} no encontrada.")

#interactuar con el usuario
while True:
    print("Seleccione una opcion: ")
    print("1. Registrar usuario. \n 2. Prestar bicicleta. \n 3. Consultar bicicleta. \n 4. Salir.")

    opcion = int(input("ingrese su opcion."))

    if opcion==1:
        agregar_usuario()
    elif opcion==2:
        prestar_bici()
    elif opcion==3:
        bicicleta = input("Ingrese el nombre de la bicicleta: ")
        consultar_bici()
    elif opcion==4:
        break
    else:
        print("Opción no valida.")