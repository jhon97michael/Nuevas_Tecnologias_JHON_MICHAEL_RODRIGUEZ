# Para crear una clase en python, usamos la palabra


class Persona:
    # ahora vamos a crear un metodo constructor
    def __int__(self, id,nombre,apellido,correo,password):
        self._id=id
        self._nombre=nombre
        self._apellido=apellido
        self._correo=correo
        self._pass=password
        #Este contiene la palabra reservada SELF,
        #Similar a THIS en JAVA, por ejemplo

        #Esto es encapsulamiento con Python

        #Se usa un underscore al principio de la variable
        #para indicar que será encapsulada

        #esto es un setter

        @id.setter
        def id(self, id):
            self._id=id

        #esto es un getter
        @property
        def id(self):
            return self._id
        #Vamos a hacer lo mismo para cada uno de los atributos
        #instanciamos
        @nombre.setter
        def nombre(self, nombre):
            self._nombre=nombre

        @property
        def nombre(self):
            return self._nombre

        @apellido.setter
        def apellido(self, apellido):
            self._apellido=apellido

        @property
        def apellido(self):
            return self._apellido

        @correo.setter
        def correo(self,correo):
            self._correo=correo

        @property
        def correo(self):
            return self._correo

        @password.setter
        def password(self, password):
            self._pass=password

        @property
        def password(self):
            return self._pass

