class Persona:
    def __init__(self, id, nombre, apellido, correo, password):
        self._id = id
        self._nombre = nombre
        self._apellido = apellido
        self._correo = correo
        self._password = password

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        self._nombre = value

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, value):
        self._apellido = value

    @property
    def correo(self):
        return self._correo

    @correo.setter
    def correo(self, value):
        self._correo = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = value

    def registrar_usuario(self):
        self._id = input("Ingrese su identificación: ")
        self._nombre = input("Ingrese su nombre: ")
        self._apellido = input("Ingrese sus apellidos: ")
        self._correo = input("Ingrese su correo electrónico: ")
        self._password = input("Ingrese una contraseña para el usuario: ")

    def imprimirPersona(self):
        print(f"ID: {self._id}, Nombre: {self._nombre}, Apellido: {self._apellido}")


