import random

vidas = 5
puntos = 0

#si sale 0 pierde vidas
#Si se general cualquier otro numero dentro del rango establecido, gana puntos.

while vidas !=0:
    num=random.randint(0,9)

    if num !=0:
        puntos+=1 #El incremento es +=
        print("Tienes ",puntos," puntos.")
    else:
        vidas -=1 #Este -= se usa para disminuir 
        print("Te quedan ",vidas," vidas.")
        
