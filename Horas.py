horas = int(input("¿Cuantas horas trabajó esta semana?"))
valor_hora = int(input("¿Cual es su salario por hora?"))
if horas > 50:
    print("Prohibido")
elif horas < 45:
    pago = (valor_hora) *40 + (valor_hora) *10 + valor_hora *3 *(horas-45)
elif horas < 40:
    pago = (valor_hora) *40 + (valor_hora)*2+(hora-40)
else:
    pago = valor_hora*horas
print (pago)
