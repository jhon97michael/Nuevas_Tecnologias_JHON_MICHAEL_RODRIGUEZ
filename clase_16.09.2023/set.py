# los conjuntos son inmutables
# son desordenados, quiere decir que cuando se llama no se tiene certeza en el orden que los mostrará
# no son indexados
# NO permite duplicados de elementos

vocales = {"a","e","i","o","u"}

print(len(vocales))
print(type(vocales))

# PAra recorrer los conjutos set  se usa in

for i in vocales:
    print(vocales)
print("-------------------------------")

for i in vocales:
    print(vocales)
print("-------------------------------")
for i in vocales:
    print(vocales)
print("-------------------------------")

#Tiene el metodo add y el metodo remove

vocales.add("g")

for i in vocales:
    print(vocales)

#podemos remover elementos

vocales.remove("g")

for i in vocales:
    print(vocales)

