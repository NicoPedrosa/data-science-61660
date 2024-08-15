Empleados = ['Juan', 'Ana', 'Carlos', 'Marta', 'Lucía', 'Pedro', 'Sofía']
Horas_trabajadas = [40, 35, 50, 20, 45, 38, 60]

#Calcular el total de horas trabajadas: Suma todas las horas trabajadas por los empleados.

Total_Horas_trabajadas = sum(Horas_trabajadas)

#Identificar a los empleados que trabajaron más horas que el promedio: Calcula el promedio de horas trabajadas 
# y luego identifica qué empleados trabajaron más que ese promedio.

Promedio_Horas_trabajadas = sum(Horas_trabajadas) / len(Horas_trabajadas)

#Listas de empleados con mas y menos hs. que el Promedio

Mas_hs_que_promedio= []
Menos_hs_que_promedio= []

for i in range(0, len(Empleados)):
    Empleado_actual = Empleados[i]
    Horas_trabajadas_actual = Horas_trabajadas[i]
    
    if Horas_trabajadas_actual > Promedio_Horas_trabajadas:
        Mas_hs_que_promedio.append((Empleado_actual, Horas_trabajadas_actual))
        
    elif Horas_trabajadas_actual < Promedio_Horas_trabajadas:
        Menos_hs_que_promedio.append((Empleado_actual, Horas_trabajadas_actual))
        
 
print(f'1. El total de hs. trabajadas es de: {Total_Horas_trabajadas} ') 
print(f'2. El promedio de hs. trabajadas es de: {Promedio_Horas_trabajadas}')
if Mas_hs_que_promedio:
    print(f'3. Los empleados que trabajaron mas hs. que el promedio son: ')
    for empleado, horas in Mas_hs_que_promedio:
        print(f'- {empleado}: {horas} horas')
if Menos_hs_que_promedio:
    print(f'4. Los empleados que trabajaron menos hs. que el promedio son: ')
    for empleado, horas in Menos_hs_que_promedio:
        print(f'- {empleado}: {horas} horas')
        