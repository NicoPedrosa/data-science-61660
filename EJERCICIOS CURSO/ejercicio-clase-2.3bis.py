Productos = ['Leche', 'Pan', 'Huevos', 'Queso', 'Manteca', 'Café', 'Azúcar']
Precios = [150, 60, 120, 200, 80, 250, 50]

# Calcular la sumatoria y el promedio de los precios
Sumatoria_precios = sum(Precios)
Promedio_precios = Sumatoria_precios / len(Precios)

# Recorremos las listas y comparamos los precios con el promedio
for i in range(len(Precios)):
    Precio_actual = Precios[i]
    Producto_actual = Productos[i]
    
    if Precio_actual > Promedio_precios:
        print(f'El precio del producto {Producto_actual} es mayor que el precio promedio')
    elif Precio_actual < Promedio_precios:
        print(f'El precio del producto {Producto_actual} es menor que el precio promedio')

# Imprimir la sumatoria de los precios
print(f'El precio total de todos los productos es de {Sumatoria_precios}')