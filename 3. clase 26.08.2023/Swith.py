#Generar un programa que permita hacer el registro e iniciar sesion dentro del while, debe imprimir
#el menu usando la implementacion de IF, elif, else (selector multiple).
#Cuando inicie sesion que implemente la solucion del calculo de cuotas creada en el reto anterior.

# Simulación de una base de datos usando un diccionario
database = {}

def insert_record(id, data):
    database[id] = data
    print(f"Registro con ID {id} insertado.")

def get_record(id):
    if id in database:
        return database[id]
    else:
        return "Registro no encontrado."

def update_record(id, new_data):
    if id in database:
        database[id] = new_data
        print(f"Registro con ID {id} actualizado.")
    else:
        print("Registro no encontrado.")

def delete_record(id):
    if id in database:
        del database[id]
        print(f"Registro con ID {id} eliminado.")
    else:
        print("Registro no encontrado.")

def show_all_records():
    print("Registros en la base de datos:")
    for id, data in database.items():
        print(f"ID: {id}, Datos: {data}")

# Ejemplo de uso
#insert_record(1, {input("Nombre"): "Ejemplo 1", "edad": 25, "ciudad": "Ciudad 1"})
#insert_record(2, {"nombre": "Ejemplo 2", "edad": 30, "ciudad": "Ciudad 2"})

print("Que operación deseas realizar?")
print("1. Ingresar")
print("2. Registrarse")
print("3. Salir")

respuesta = input("")

if respuesta == 1:
    