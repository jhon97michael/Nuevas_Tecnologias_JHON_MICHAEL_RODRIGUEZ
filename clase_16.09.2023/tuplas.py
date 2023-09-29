# Son inmutables
# contienen distintos tipos de datos
# si se requiere añadir se debe convertir primero a una lista
# Se puede acceder la tupla indicando el indice de la misma, el cual comienza desde cero.
# Para recorrer la tupla usamos el ciclo for
# podemos hacer joins entre tuplas.
# Para conocer el tamaño usamos la funcion len()
# las tuplas permiten duplicados en los datos almacenados 

dias_semana=("lunes", "martes","miercoles","jueves","viernes","sabado","domingo")
print(type(dias_semana))

#Funcion len(dias_semana) -> mide el tamaño
print(len(dias_semana))

# imprimir 
print(dias_semana[0])
print(dias_semana[1])
print(dias_semana[2])
print(dias_semana[3])
print(dias_semana[4])
print(dias_semana[5])
print(dias_semana[6])

# Podemos hacer slicing indicando el rango quye queremos imprimir

print(dias_semana[:7])
print(dias_semana[0:])
print(dias_semana[-1:])
print(dias_semana[2:5])

# para recorrer la tupla usamos for para iterar por los indices

for i in range(len(dias_semana)):
    print(dias_semana[-i])

# para cambiar algun valor de la tupla o añadir debemos primero convertirla a una lista:

dias_semana_lista = list(dias_semana) #casteo de tipo

print(type(dias_semana_lista))

# Para agregar elemento en lista
dias_semana_lista.append("festivo")
print(dias_semana_lista[:8])

# Para eliminar ultimo elemento en lista
dias_semana_lista.pop()
print(dias_semana_lista[:8])

dias_semana = tuple(dias_semana_lista)

print(type(dias_semana))