# Reciban el valor de una compra
#Que puedan ingresar el valor de cuotas que pagaran
#Calcular el valor de la cuota 
#Usando While queremos que imprima el plan de pago y le muestre el cupo liberado con cada pago

compra = int(input("Valor compra: "))
cuotas = int(input("A cuantas cuotas va a pagar: "))
ValorCuota = compra / cuotas
print ("El valor de la cuota es:", ValorCuota)

while compra !=0:
    if cuotas !=0:
        compra -= ValorCuota
        print ("Su saldo restante es: ",compra)
    else:
        break

