# Los diccionarios permiten tener clave valor
# son cambiables
# no permiten duplicados
# Desde python 3.7 son ordenados
# permiten agregar, remover items
# son iterables 
# poseen distintos metodos para manipular los datos
# admite distintos tipos de datos

usuario = {"nombre":"pepito", "apellido":"Perez", "edad":"25"}

print(usuario)

# muestra las claves del diccionario
print(usuario.keys())

# muestra los valores del diccionario 
print(usuario.values())

# Para conocer el tamaño del diccionario usamos el metodo len()
print(len(usuario))
print(type(usuario))

# cuando queremos buscar un item podemos usar get()

print(usuario.get("nombre"))
print(usuario["edad"])

# Podemos agragar nuevos items

usuario["correo"]="pepito@mail.com"

print(usuario.get("correo"))
print(usuario.keys())

# Podemos actualizar un valor

usuario.update({"correo":"perez@mail.com"})

print(usuario.get("correo"))

# para remover items del diccionario
""""
usuario.pop("nombre")
print(usuario.keys())

usuario.popitem()
print(usuario.keys())

del usuario["edad"]
print(usuario.keys())"""

# para recorrer el diccionario podemos elegir entre recorrer las claves, recorrer los valores o recorrer ambos

# ambos

for x,y in usuario.items():
    print(x,y)

# Recorrer claves

for x in usuario.keys():
    print(x)

# Recorrer valores

for y in usuario.values():
    print(y)

# Podemos tener un diccionario de diccionarios

usarios= {"usuario1":{"nombre":"Juan","edad":12}, "usuario":{"nombre":"Maria","edad":15}, "usuario3":{"nombre":"Julia","edad":18}}

estudiante1 = {"nota1":4.5,"nota2":4.3}
estudiante2 = {"nota1":4,"nota2":4.5}
estudiante3 = {"nota1":3.5,"nota2":2.3}

estudiantes = {"estudiante1":estudiante1,"estudiante2":estudiante2,"estudiante3":estudiante3}

print(estudiantes["estudiante2"]["nota2"])