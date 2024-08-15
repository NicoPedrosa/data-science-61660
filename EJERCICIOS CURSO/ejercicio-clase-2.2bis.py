
Productos = ['Leche', 'Pan', 'Huevos', 'Queso', 'Manteca', 'Café', 'Azúcar']
Stock  = [20, 5, 0, 12, 6, 0, 3]

for i in range(0, len(Stock)):
    
    Producto_actual = Productos[i]
    Stock_actual = Stock[i]
    
    if Stock_actual == 0:
        print(f"El producto {Producto_actual} está fuera de stock")
    elif Stock_actual < 5:
        print(f"El producto {Producto_actual} está bajo en stock")
    else:   
        print(f"El producto {Producto_actual} está normal de stock")