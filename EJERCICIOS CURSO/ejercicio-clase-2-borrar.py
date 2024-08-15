Empleados = ['Juan', 'Ana', 'Carlos', 'Marta', 'Lucía', 'Pedro', 'Sofía']
Horas_trabajadas = [40, 35, 50, 20, 45, 38, 60]

# Calcular el total de horas trabajadas
Total_Horas_trabajadas = sum(Horas_trabajadas)

# Calcular el promedio de horas trabajadas
Promedio_Horas_trabajadas = Total_Horas_trabajadas / len(Horas_trabajadas)

# Listas para empleados que trabajaron más y menos horas que el promedio
Empleados_mas_horas = []
Empleados_menos_horas = []

# Identificar empleados que trabajaron más o menos horas que el promedio
for i in range(len(Empleados)):
    Empleado_actual = Empleados[i]
    Horas_trabajadas_actual = Horas_trabajadas[i]
    
    if Horas_trabajadas_actual > Promedio_Horas_trabajadas:
        Empleados_mas_horas.append((Empleado_actual, Horas_trabajadas_actual))
    elif Horas_trabajadas_actual < Promedio_Horas_trabajadas:
        Empleados_menos_horas.append((Empleado_actual, Horas_trabajadas_actual))

# Imprimir los resultados
print(f'El total de horas trabajadas es: {Total_Horas_trabajadas}')
print(f'El promedio de horas trabajadas es: {Promedio_Horas_trabajadas:.2f}')

if Empleados_mas_horas:
    print("\nEmpleados que trabajaron más horas que el promedio:")
    for emp, hs in Empleados_mas_horas:
        print(f'- {emp}: {hs} horas')

if Empleados_menos_horas:
    print("\nEmpleados que trabajaron menos horas que el promedio:")
    for emp, hs in Empleados_menos_horas:
        print(f'- {emp}: {hs} horas')