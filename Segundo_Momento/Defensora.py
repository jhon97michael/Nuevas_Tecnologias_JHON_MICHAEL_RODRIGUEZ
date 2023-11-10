

from Persona import Persona

class Defensora(Persona):
    def __init__(self, id, nombre, apellido, correo, password, cargo, salario, tipo_contrato):
        # de esta forma usamos los atributos de la clase padre
        super().__init__(id, nombre, apellido, correo, password)
        # Aca declaramos los atributos que son especificos de la subclase empleado
        self._cargo = cargo
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
    def salario(self, salario):
        self._salario = salario

    @property
    def tipo_contrato(self):
        return self._tipo_contrato

    @tipo_contrato.setter
    def tipo_contrato(self, tipo_contrato):
        self._tipo_contrato = tipo_contrato

    # Vamos a sobreescribir los metodos

    def registrar_usuario(self):
        self._id = input(f"Ingrese su identificacion: ")
        self._nombre = input(f"Ingrese su nombre: ")
        self._apellido = input(f"Ingrese su apellido: ")
        self._correo = input(f"Ingrese su correo: ")
        self._password = input(f"Ingrese su contraseña: ")
        self._cargo = input(f"Ingrese el cargo del empleado: ")
        self._salario = float(input(f"Ingrese el salario: "))
        self._tipo_contrato = input(f"Ingrese el tipo de contrato: ")

    def imprimir_registro(self):
        super().imprimir_registro()  # Otra forma de sobreescribir
        print(f"Cargo: {self._cargo} Salario: {self._salario} Tipo de contrato: {self._tipo_contrato}")

    def iniciar_sesion(self):
        correo_empleado = input("Ingrese el correo registrado: ")
        contrasena_empleado = input("Ingrese contraseña: ")

        if correo_empleado == self.correo and contrasena_empleado == self.password:
            return True

        else:
            return False

    def appEmpleado(self, iniciar_sesion, imprimir_registro):
        iniciar_sesion(True)
        print("Has iniciado sesion.")
        imprimir_registro()