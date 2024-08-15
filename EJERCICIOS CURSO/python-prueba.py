#Estamos explicando datos simples

dato_num = 8
dato_float = 10.22
dato_booleano_1 = True
dato_booleano_2 = False
dato_string = "Soy Nico"

print(dato_float)
print(type(dato_string), type(dato_num))

#vamos a explorar datos estructurados

persona = {'Nombre': 'Nicolas', 'Edad': '18' , 'Profesion': 'PAS'}

print(persona['Edad'])

#En este apartado vamos a entender como es la sintaxis para ejecutar distintas estructuras de control

#* **for: es la estructura para hacer bucles**


#FOR

rango = range(1,10)
print('Primer elemento:', rango[0])
print('Primer elemento:', rango[-1])

#Programomos el bucle

for i in rango:
    a = i + 1
    b = a * i
    print(a)
    print(b)

#Programomos un bucle sin sentido

for i in rango:
    a = 2 + 2
    print(a)
    
#recorrer una lista

for i in persona:
    print(i)

# while

s = 1
while s <= 10:
    print(s)
    s = s + 2
    
# if

prueba = 10
if prueba < 5:
    print ('Es menor a 5')
elif prueba < 9:
    print ('Es menor a 9')
else:
    print ('Es mayor o igual a 9')
    
# for + if

for i in rango:
    if i <= 4:
        print('Primer grupo', i)
    elif i <= 6:
        print('Otra cosa', i*2)
    else:
        print('Final', i**2)
        

def mi_funcion(argumento_1,argumento_2):
    resultado_1 = argumento_1 * 2
    resultado_2 = argumento_2 / 3
    resultado_final = resultado_1 - resultado_2
    return resultado_final

mi_funcion(argumento_1=10,argumento_2=4)


