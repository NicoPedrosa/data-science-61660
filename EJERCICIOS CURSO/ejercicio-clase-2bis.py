
#Tienes una lista de ciudades y sus temperaturas máximas registradas en una semana:
#Escribe un código en Python que recorra las listas Ciudades y Temperaturas_maximas y determine en qué 
# ciudades la temperatura máxima disminuyó respecto a la ciudad anterior en la lista. 
# El programa debe imprimir los nombres de las ciudades donde ocurrió esta disminución.

Ciudades = ['Buenos Aires', 'Córdoba', 'Rosario', 'Mendoza', 'La Plata', 'Tucumán', 'Mar del Plata']
Temperaturas_maximas = [28, 30, 29, 33, 31, 32, 30]

for i in range (1, len(Ciudades)):
    Ciudad_actual = Ciudades[i]
    Ciudad_anterior = Ciudades[i-1]
    Temp_max_actual = Temperaturas_maximas[i]
    Temp_max_anterior = Temperaturas_maximas[i-1]
    
    if Temp_max_actual < Temp_max_anterior:
        
        print(f"La temperatura máxima disminuyó en {Ciudad_actual} con respecto a {Ciudad_anterior}")
    