Dias = ['Lunes','Martes','Miercoles','Jueves','Viernes','Sabado','Domingo']

Valor_acciones = [200,225,232,221,243,256,255]


for i in range(1, len(Dias)):
    dia_actual = Dias[i]
    dia_anterior = Dias[i-1]
    valor_actual = Valor_acciones[i]
    valor_anterior = Valor_acciones[i-1]
    valor_diferencia = valor_anterior - valor_actual 
    
    if valor_actual < valor_anterior:
        print(f"El valor de las acciones bajó el día {dia_anterior} hacia el {dia_actual} en {valor_diferencia} unidades")
       