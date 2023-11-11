


class Persona():
    def __init__(self, id, nombre, apellido, correo, password):
        self._id = id
        self._nombre = nombre
        self._apellido = apellido
        self._correo = correo
        self._password = password

        # Instanciamiento de ID
        @id.setter
        def id(self,id):
            self._id = id

        @property
        def id(self):
            return self._id
        
        # Instanciamiento de Nombre
        @nombre.setter
        def nombre(self,nombre):
            self._nombre = nombre

        @property
        def nombre(self):
            return self._nombre
        
        # Instanciamiento de Apellido
        @apellido.setter
        def apellido(self,apellido):
            self._apellido = apellido

        @property
        def apellido(self):
            return self._apellido
        
        # Instanciamiento de Correo
        @correo.setter
        def correo(self,correo):
            self._correo = correo

        @property
        def correo(self):
            return self._correo
        
        # Instanciamiento de Password
        @password.setter
        def password(self,password):
            self._password = password

        @property
        def password(self):
            return self._password
        
        def registrar_usuario(self):
            id = input("Ingrese su identificación: ")
            nombre = input("Ingrese su nombre: ")
            apellido = input("Ingrese sus apellidos: ")
            correo = input("Ingrese su correo electronico: ")
            password = input("Ingrese una contraseña para el usuario: ")


        def imprimirPersona(self):
            print(f"ID: {self._id} Nombre: {self._nombre} Apellido: {self._apellido} ")

