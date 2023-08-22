from Preoductos import Inventario
inventario = Inventario()

def Menu():
    print("---------------------------------------------------------")
    print("Oreld - Practica 1 - Lenguajes formales y de programacion")
    print("---------------------------------------------------------")
    print("Sistema de invientario: ")
    print("---------------------------------------------------------")
    print("1. Cargar inventario inicial")
    print("2. Cargar instrucciones de movimientos")
    print("3. Crear informe de inventario")
    print("4. Salir")
    print("--------------------------------------------------------")
    opcion = 0
    opcion = input("Ingrese el numero correspondiente a la opcion: ")
    
    if opcion == "1":
        print("---------------------------")
        print("Cargar inventario inicial")
        print("---------------------------")
        inventario.cargar_inventario(f'C:\Users\eliot\OneDrive\Escritorio\Documentos\Practica#1_LFP\inventario.inv')
        print("Inventario inicial cargado con exito")
        Menu()
        
    
    elif opcion == "2":
        print("---------------------------")
        print("Cargar instrucciones de movimientos")
        movimiento = input("Ingrese el moviento que desea hacer:")
        name = input("ingrese el nombre de el producto:")
        cantida= input("ingrese la cantidad de el producto:")
        price = input("ingrese la cantidad de el precio unitario:")
        ubication = input("ingrese la ubicacion de el producto:")
        with open(f'C:\Users\eliot\OneDrive\Escritorio\Documentos\Practica#1_LFP\movimiento.txt', 'a') as archivo:
            archivo.write('')
            archivo.write(f'\n{movimiento} {name};{cantida};{price};{ubication}')

        with open(f'{ruta}', 'r') as file:
            lineas = file.readlines()

        for linea in lineas:
            instruccion, resto = linea.strip().split(' ', 1)
            if instruccion == 'agregar_stock':
                nombre, cantidad, ubicacion = resto.split(';')
                exito = inventario.agregar_stock(nombre, cantidad, ubicacion)
                if exito:
                    with open(f'C:\Users\eliot\OneDrive\Escritorio\Documentos\Practica#1_LFP\movimientos.mov', 'a') as archivo:
                        archivo.write(f'\n{movimiento} {name};{cantida};{price};{ubication}')
                    print(f"Se agregaron {cantidad} unidades de {nombre} en {ubicacion}")
                else:
                    print(f"Error: Producto no encontrado en {ubicacion}")

            elif instruccion == 'vender_producto':
                nombre, cantidad, ubicacion = resto.split(';')
                exito = inventario.vender_producto(nombre, cantidad, ubicacion)
                if exito:
                    with open(f'C:\Users\eliot\OneDrive\Escritorio\Documentos\Practica#1_LFP\movimientos.mov', 'a') as archivo:
                        archivo.write(f'\n{movimiento} {name};{cantida};{price};{ubication}')
                    print(f"Se vendieron {cantidad} unidades de {nombre} en {ubicacion}")
                else:
                    print("Error: No se pudo vender el producto")
        print("---------------------------")
        print("movimiento cargado")
        Menu()
    
    
    elif opcion == "3":
        print("---------------------------")
        print("Crear informe de inventario")
        print("---------------------------")
        inventario.generar_informe('informe.txt')
        print("Informe generado exitosamente")
        Menu()
    
    elif opcion == "4":
        print("---------------------------")
        print("Salinedo....")
        print("---------------------------")

   
    else:
        print("---------------------------")
        print("Opcion invalida")
        print("---------------------------")
        Menu()

Menu()