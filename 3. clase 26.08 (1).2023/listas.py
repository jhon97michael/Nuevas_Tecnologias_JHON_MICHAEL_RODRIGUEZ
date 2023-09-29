# las listas son estructuras de datos lineales
# Se crean brackets ejemplo: my_list=[]
# Las listas son ordenadas(Orden de insercion), esto quiere decir 
# que el ultimo dato ingresado ocupara la ultima posicion.
# Emplea metodos para manipular los Items de la lista.
# Como todo array la primera posicion inicia en 0 cero.
# permite items duplicados y los trata como elementos diferentes.
# Las listas son mutables, es decir, podemos agregar, actualizar o remover items
# Puede contener distintos tipos de datos.

nombres = ["Juan","Maria","Pepito","Luisa"]

# el metodo len() valida el tamaño de la lista
print(len(nombres))

# El metodo type() muestra el tipo de la lista
print(type(nombres))

listaDatos = ["Pepito","Perez",1000100100,1.80,True]
print(listaDatos[2])
print(f"El numero de documento es {listaDatos[2]}")

# Slicing de datos o rango de datos.
print(listaDatos[0:2])
print(listaDatos[1:4])
print(listaDatos[:4])
print(listaDatos[2:])

print(listaDatos[:-1])
print(listaDatos[:-2])
print(listaDatos[:-3])
print(listaDatos[:-4])

print(listaDatos[-4:-1])