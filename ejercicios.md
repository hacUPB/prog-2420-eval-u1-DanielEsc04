# Ejemplo en clase 
Parqueadero 
Primeras 2 horas = 5$
Despues de la tercera hora = 4$
Despues de la quinta hora = 3$
Despues de la decima hora = 2$
## Variables
Entrada: Hora entrada
Salida: Hora salida
horas: cantidad de horas
valor: El valor del parqueadero en funcion de las horas.

` ` `
Inicio
Leer Entrada
Leer Salida
horas = Salida - Entrada
Si horas <= 2 
    valor = horas*5
fin si
Si 2 < horas <= 5 
    valor = ((horas - 2)*4)+10
fin si
Si 5 < horas <= 10
    valor = ((horas - 5)*3)+22
fin si
Si horas > 10 
    valor = horas*2
fin si
imprimir valor
Fin
` ` `

# Ejercicio tarjeta de credito
# Variables:
Cuotas: se indica la cantidad de cuotas
Intereses: se indica el porcentaje de intereses 
Deuda: el valor total de la deuda 
Subtotal: la deuda sobre la cantidad de cuotas 
Pago_mensual: pago total por mes

Inicio
    Leer Cuotas
    Leer intereses
    Leer deuda
    Mientras Deuda > 0
        Subtotal = Deuda/Cuotas
        Intereses_mes = Subtotal * (intereses/100)
        Pago_mensual = intereses_mes + Subtotal
        Cuotas = Cuotas - 1
        Deuda = Deuda - Subtotal
        Imprimir Pago_mensual
    Si Deuda > 0 
        Repetir mientras
Fin