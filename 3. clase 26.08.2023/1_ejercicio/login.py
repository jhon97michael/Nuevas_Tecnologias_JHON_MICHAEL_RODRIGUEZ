

name = input("Ingrese su nombre: ")
email = input("Ingrese su correo electronico: ")
password = input("Cree una contraseña: ")

#pregunta para validar
captchat = input("¿Cuantas letras tiene la palabra azul? ")


#Validar
if email == "jhon@gmail.com" and password == "12345" and captchat == "4":
    print ("Hola!!! Bienvendo.")
else:
    print("Usuario y/o contraseña incorrectos.")