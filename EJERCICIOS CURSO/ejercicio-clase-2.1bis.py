Productos = ['Leche', 'Pan', 'Huevos', 'Queso', 'Manteca', 'Café', 'Azúcar']
Precios = [150, 60, 120, 200, 80, 250, 50]

Umbral = 100

for i in range(0, len(Productos)):
    
    Precio_actual = Precios[i]
    Producto_actual = Productos[i]
    
    
    if Precio_actual > Umbral:
        
        print(f"El producto {Producto_actual} tiene un precio de {Precio_actual}, que es mayor que el umbral de {Umbral}")
    
    