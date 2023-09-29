# Bancolombia quiere calcular los salarios de su nueva start up PAGUI debe:
# 1. Registrar nombre, apellido, cargo, area, y salario.
# 2. Requiere listar a los empleados.
# 3. Requiere calcular el salario neto, teniendo en cuenta que si gana menos de dos SMLV se le paga auxilio de transporte
# 4. Requiere imprimir la colilla de pago.
# 5. Un empleado podrá ingresar al sistema y podrá imprimir su colilla de pago e imprimirlo.
# 6. Y un analista de recursos humanos podrá visualizar todos los empleados y todas las colillas y ademas podrá registrar los empleados.
# 7. El de recursos humanos puede visualizar el total del pago de la nomina.

# simular base de datos

# Definir una clase Empleado para representar a los empleados
class Empleado:
    def __init__(self, nombre, apellido, cargo, area, salario):
        self.nombre = nombre
        self.apellido = apellido
        self.cargo = cargo
        self.area = area
        self.salario = salario
        self.auxilio_transporte = 0

    def calcular_salario_neto(self):
        # Calcular el salario neto
        smlv = 908526  # Salario Mínimo Legal Vigente en 2021
        if self.salario <= 2 * smlv:
            self.auxilio_transporte = 106454
        salario_neto = self.salario - self.auxilio_transporte
        return salario_neto

    def imprimir_colilla_pago(self):
        # Imprimir la colilla de pago
        salario_neto = self.calcular_salario_neto()
        print("Colilla de Pago:")
        print(f"Nombre: {self.nombre} {self.apellido}")
        print(f"Cargo: {self.cargo}")
        print(f"Área: {self.area}")
        print(f"Salario Bruto: {self.salario}")
        print(f"Auxilio de Transporte: {self.auxilio_transporte}")
        print(f"Salario Neto: {salario_neto}")
        print("-" * 30)

# Definir una lista para almacenar a los empleados
empleados = []

# Función para listar a los empleados
def listar_empleados():
    print("Lista de Empleados:")
    for empleado in empleados:
        print(f"{empleado.nombre} {empleado.apellido}")

# Función para registrar a un empleado
def registrar_empleado():
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    cargo = input("Cargo: ")
    area = input("Área: ")
    salario = float(input("Salario: "))
    empleado = Empleado(nombre, apellido, cargo, area, salario)
    empleados.append(empleado)
    print("Empleado registrado con éxito.")

# Función para visualizar todas las colillas de pago
def visualizar_colillas_pago():
    print("Colillas de Pago:")
    for empleado in empleados:
        empleado.imprimir_colilla_pago()

# Función para calcular el total del pago de la nómina
def calcular_total_nomina():
    total_nomina = sum(empleado.calcular_salario_neto() for empleado in empleados)
    print(f"Total de la Nómina: {total_nomina}")

# Programa principal
while True:
    print("Menú:")
    print("1. Listar Empleados")
    print("2. Registrar Empleado")
    print("3. Visualizar Colillas de Pago")
    print("4. Calcular Total de la Nómina")
    print("5. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        listar_empleados()
    elif opcion == "2":
        registrar_empleado()
    elif opcion == "3":
        visualizar_colillas_pago()
    elif opcion == "4":
        calcular_total_nomina()
    elif opcion == "5":
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
