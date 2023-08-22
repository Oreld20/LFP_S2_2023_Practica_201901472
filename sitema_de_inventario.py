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
        inventario.cargar_inventario(r'C:\Users\eliot\OneDrive\Escritorio\Documentos\Practica#1_LFP\inventario.inv')
        print("--------------------------------------------------------")
        print("Inventario inicial cargado con exito")
        print("--------------------------------------------------------")
        inventario.mostrar_productos()
        print("--------------------------------------------------------")
        Menu()
        
    
    elif opcion == "2":
        print("---------------------------")
        print("Cargar instrucciones de movimientos")
        with open(r'C:\Users\eliot\OneDrive\Escritorio\Documentos\Practica#1_LFP\movimiento.txt', 'a') as coso:
            coso.write('')
        movimiento = input("Ingrese el moviento que desea hacer:")
        name = input("ingrese el nombre de el producto:")
        cantida= input("ingrese la cantidad de el producto:")
        ubication = input("ingrese la ubicacion de el producto:")
        

        with open(r'C:\Users\eliot\OneDrive\Escritorio\Documentos\Practica#1_LFP\movimiento.txt', 'w') as archi:
            archi.write(f'{movimiento};{name};{cantida};{ubication}')

        with open(r'C:\Users\eliot\OneDrive\Escritorio\Documentos\Practica#1_LFP\movimiento.txt', 'r') as file:
            lineas = file.readlines()

        for linea in lineas:
            if linea.strip():
                separador = linea.split(';')
                instruccion = separador[0]
                nombre= separador[1]
                cantidad = int(separador[2])
                ubicacion = separador[3]
                if instruccion == 'agregar_stock':
                    exito = inventario.agregar_stock(nombre, cantidad, ubicacion)
                    if exito:
                        with open(r'C:\Users\eliot\OneDrive\Escritorio\Documentos\Practica#1_LFP\movimientos.mov', 'a') as moviento_añadir:
                            moviento_añadir.write(f'{movimiento};{name};{cantida};{ubication}'+ '\n')
                        print("--------------------------------------------------------")
                        print(f"Se agregaron {cantidad} unidades de {nombre} en {ubicacion}")
                        print("--------------------------------------------------------")
                    else:
                        print(f"Error: Producto no encontrado en {ubicacion}")

                elif instruccion == 'vender_producto':
                    exito = inventario.vender_producto(nombre, cantidad, ubicacion)
                    if exito:
                        with open(r'C:\Users\eliot\OneDrive\Escritorio\Documentos\Practica#1_LFP\movimientos.mov', 'a') as moviento_vender:
                            moviento_vender.write(f'{movimiento};{name};{cantida};{ubication}'+ '\n')
                        print("--------------------------------------------------------")
                        print(f"Se vendieron {cantidad} unidades de {nombre} en {ubicacion}")
                        print("--------------------------------------------------------")
                    else:
                        print("Error: No se pudo vender el producto")
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