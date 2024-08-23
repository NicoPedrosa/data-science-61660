#Tienes una lista de temperaturas máximas registradas durante una semana en una ciudad. 
#El objetivo es identificar los días en los que la temperatura fue superior a la del día anterior, 
# y calcular cuántos grados subió.

Dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
Temperaturas = [18, 20, 22, 21, 23, 25, 24]

# Variable para contar los días en los que la temperatura aumentó
dias_con_aumento = 0

for i in range(1, len(Temperaturas)):
    Dia_actual = Dias[i]
    Dia_anterior = Dias[i-1]
    Temperatura_actual = Temperaturas[i]
    Temperatura_anterior = Temperaturas[i-1]
    Temperatura_diferencia = Temperatura_actual - Temperatura_anterior

    if Temperatura_actual > Temperatura_anterior:
        print(f'El día {Dia_actual}, la temperatura fue superior al día {Dia_anterior}, por una diferencia de {Temperatura_diferencia} grados')
        dias_con_aumento += 1

# Resumen final
print(f'Hubo un aumento de temperatura en {dias_con_aumento} días de la semana.')
    