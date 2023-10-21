
from Persona import Persona
from Empleado import Empleado

empleado = Empleado(id=None,
                    nombre=None,
                    apellido=None,
                    correo=None,
                    contrasena=None,
                    cargo=None,
                    salario=None,
                    tipo_contrato=None)



def menuApp():

    print("Inicialice con 1: ")

    init = int(input("Escriba 1: "))

    while init!=0:

        print("Seleccione 1 para registra empleado\n",
              "Seleccione 2 para iniciar sesión\n",
              "Seleccione 3 para salir")

        opcion = int(input("Ingrese una opción: "))

        if opcion ==1:
            empleado.registrar_usuario()
        elif opcion ==2:
            empleado.iniciar_sesion()
            empleado.imprimir_registro()
            empleado.appEmpleado(empleado.iniciar_sesion, empleado.imprimir_registro)
        elif opcion ==3:
            print("Salir.")
            init=0


menuApp()