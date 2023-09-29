#La aplicacion debe permitir registrar ingresos y contar el saldo de estos
#Debe permitir registrar egresos y mostrar el saldo 
#Si el egresos es mayor que el saldo no debe permitir hacer el retiro y mostrara un mensaje 
#de saldo insuficiente
#la aplicacion llevara registro de los movimientos indicando el numero de ingresos y 
#egresos.

saldo= 0
acumIngresos = 0
acumEgresos = 0

isOn=int(input("Ingrese 1 para inicializar el servicio: "))

while isOn !=0:

    opc=int(input("1. Para registrar un ingreso: \n 2. Egreso: \n 3. Salir."))

    if opc==1:
        ingreso = int(input("Registre el ingreso: "))

        saldo = saldo + ingreso

        print(f"Su saldo es ${saldo}")
        acumIngresos +=1
        print(f"Total depositos: ${acumIngresos}")
    elif opc ==2:
        egreso= int(input("Registre el monto a retirar: "))

        saldo = saldo - egreso

        if saldo <10:
            print("Fondos insuficientes.")
            saldo = saldo + egreso
            print(saldo)
            
        else:
            print(f"Su saldo es: ${saldo}")
        acumEgresos +=1
        print(f"Total retiros: ${acumEgresos}")

    elif opc ==3:
        print("Salir")
        isOn =0
    else:
        print("Ingrese una opcion valida.")