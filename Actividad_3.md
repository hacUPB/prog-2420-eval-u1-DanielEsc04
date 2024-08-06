# Problema 6 
Se desea saber cuántos años, meses y días tiene actualmente una persona, basándose en su fecha de nacimiento. Además, le gustaría saber si ya ha cumplido años este año o aún no, y si hoy es su cumpleaños para celebrarlo. Cada una de las fechas está conformada por 3 variables: día, mes y año
## Variables
    Año_Nacimiento: Se usa para saber el año de nacimiento del usuario
    Mes_Nacimiento: Se usa para saber el mes de nacimiento del usuario
    Dia_Nacimiento: Se usa para saber el dia de nacimiento del usuario

    Año_Actual: Se toma informacion de calendario del año actual
    Mes_Actual: Se toma informacion de calendario del mes actual
    Dia_Actual: Se toma informacion de calendario del dia actual
    
    Edad_Años: Diferencia Años
    Edad_Mes: Diferencia Meses
    Edad_Dia: Diferencia Dias
    Edad_Real: Edad del usuario en la fecha actual.

` ` ` 
Inicio
    Leer Año_Nacimiento
    Leer Mes_Nacimiento
    Leer Dia_Nacimiento
    Leer Año_Actual
    Leer Mes_Actual
    Leer Dia_Actual
    
    Edad_Años: Año_Actual-Año_Nacimiento
    Edad_Mes: Mes_Actual-Mes_Nacimiento
    Edad_Dia: Dia_Actual-Dia_Nacimiento
    
    Si Edad_Mes=0 y Edad_Dias=0
        Imprimr: "Feliz" Edad_Años " cumpleaños"

    Si Edad_Mes < 0 
        Edad_Real= Edad_Años-1
    Si no
        Si Edad_Dias < 0
            Edad_Real= Edad_Años-1
        Si no 
        Imprimir Edad_Real
Fin
` ` ` 