
# Creamos una clase con el mismo nombre del archivo
class Persona:
    # Creamos un constructor
    def __init__(self, id, nombre,apellido,correo,contrasena): #en el self se definen los atributos
        # despues se generan las variables iguales a los atributos y le agregamos un guion bajo para encapsularlo despues
        self._id = id
        self._nombre = nombre
        self._apellido = apellido
        self._correo = correo
        self._contrasena = contrasena

    #Vamos a generar Getter and Setter

    # esto es un GET
    @property
    def id(self):
        return self._id
    #fin del GET

    # esto es el SET
    @id.setter
    def id(self, id):
        self._id = id
    #Fin del SET

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def apellido(self):
        return self._nombre

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def correo(self):
        return self._correo

    @correo.setter
    def correo(self, correo):
        self._correo = correo

    @property
    def contrasena(self):
        return self._contrasena

    @contrasena.setter
    def contrasena(self, contrasena):
        self._contrasena = contrasena


    # Vamos a generar los metodos para registrar los usuarios e imprimir el registro

    def registrar_usuario(self):
        id = input(f"Ingrese su identificacion: ")
        nombre = input(f"Ingrese su nombre: ")
        apellido = input(f"Ingrese su apellido: ")
        correo = input(f"Ingrese su correo: ")
        contrasena = input(f"Ingrese su contraseña: ")


    def imprimir_registro(self):
        print(f"id: {self._id} Nombre: {self._nombre} Apellido: {self._apellido} Correo: {self._correo} Contraseña: {self._contrasena}")