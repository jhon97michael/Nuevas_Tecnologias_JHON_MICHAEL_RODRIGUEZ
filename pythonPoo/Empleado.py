
# Aqui importamos el archivo PERSONA para generar la HERENCIA
from Persona import Persona

#Creamos la clase Empleado y le damos la HERENCIA de persona
class Empleado(Persona):

    def __init__(self,id,nombre,apellido,correo,contrasena,cargo,salario,tipo_contrato):
        # de esta forma usamos los atributos de la clase padre
        super().__init__(id,nombre,apellido,correo,contrasena)
        # Aca declaramos los atributos que son especificos de la subclase empleado
        self._cargo =cargo
        self._salario = salario
        self._tipo_contrato = tipo_contrato


        # Despues hacemos el GET and SET para capturar los datos, pero son unicamente de los
        # atributos especificos de la subclase
    @property
    def cargo(self):
        return self._cargo

    @cargo.setter
    def cargo(self, cargo):
        self._cargo = cargo

    @property
    def salario(self):
        return self._salario

    @salario.setter
    def salario(self,salario):
        self._salario = salario

    @property
    def tipo_contrato(self):
        return self._tipo_contrato

    @tipo_contrato
    def tipo_contrato(self,tipo_contrato):
        self._tipo_contrato = tipo_contrato


    # Vamos a sobreescribir los metodos


    def registrar_usuario(self):
        id = input(f"Ingrese su identificacion: ")
        nombre = input(f"Ingrese su nombre: ")
        apellido = input(f"Ingrese su apellido: ")
        correo = input(f"Ingrese su correo: ")
        contrasena = input(f"Ingrese su contraseña: ")
        cargo = input(f"Ingrese el cargo del empleado: ")
        salario = float(input(f"Ingrese el salario: "))
        tipo_contrato = input(f"Ingrese el tipo de contrato: ")

    def imprimir_registro(self):
        super().imprimir_registro() #Otra forma de sobreescribir
        print(f"Cargo: {self._cargo} Salario: {self._salario} Tipo de contrato: {self._tipo_contrato}")

