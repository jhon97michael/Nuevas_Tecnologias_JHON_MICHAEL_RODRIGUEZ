
#variables
age = int (input("Ingrese su edad: "))

height = int (input("Ingrese su estatura: "))

#Condicion IF estructura simple
if height <= 100 and age <= 10: 
    print("El niño puede ingresar.") #Esto retorna un TRUE cuando el valor de las variables son AGE=10 y HEIGHT=100

if height <= 100 and age <= 10: #Esto retorna un FALSE cuando el valor de las variables son AGE=10 y HEIGHT=110
    print("El niño puede ingresar.")

if height <= 100 and age <= 10: #Esto retorna un FALSE cuando el valor de las variables son AGE=11 y HEIGHT=100
    print("El niño puede ingresar.")

if height <= 100 and age <= 10: #Esto retorna un FALSE cuando el valor de las variables son AGE=11 y HEIGHT=110
    print("El niño puede ingresar.")
#Fin del AND

if height <= 100 or age <= 10: #Esto retorna un TRUE cuando el valor de las variables son AGE=10 y HEIGHT=100
    print("El niño puede ingresar.")

if height <= 100 or age <= 10: #Esto retorna un TRUE cuando el valor de las variables son AGE=10 y HEIGHT=110
    print("El niño puede ingresar.")

if height <= 100 or age <= 10: #Esto retorna un TRUE cuando el valor de las variables son AGE=11 y HEIGHT=100
    print("El niño puede ingresar.")

if height <= 100 or age <= 10: #Esto retorna un FALSE cuando el valor de las variables son AGE=11 y HEIGHT=110
    print("El niño puede ingresar.")

#Condicional con IF con ELSE
if height >= 150 and age >= 18:
    print("Puede ingresar al martillo.")
else:
    print("No cumple la edad ni la altura requerida")