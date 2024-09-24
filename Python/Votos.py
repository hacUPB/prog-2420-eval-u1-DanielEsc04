votos_totales = 0
votos = 0
while votos != -1:
    votos = int(input ("Ingresar votos"))
    votos_totales = votos_totales + votos + 1
print (f"Se contaron {votos_totales} votos")
