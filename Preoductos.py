class Producto:
    def __init__(self, nombre, cantidad, precio_unitario, ubicacion):
        self.nombre = nombre
        self.cantidad = int(cantidad)
        self.precio_unitario = float(precio_unitario)
        self.ubicacion = ubicacion

class Inventario:
    def __init__(self):
        self.productos = []

    def cargar_inventario(self, archivo):
        inventario = Inventario()
        with open(archivo, 'r') as f:
            for linea in f:
                if linea.strip():
                    instruccion, nombre, cantidad, precio_unitario, ubicacion = linea.strip().split(';')
                    if instruccion == 'crear_producto':
                        producto = Producto(nombre, int(cantidad), float(precio_unitario), ubicacion)
                        self.productos.append(producto)
        return inventario

    def agregar_stock(self, nombre, cantidad, ubicacion):
        for producto in self.productos:
            if producto.nombre == nombre and producto.ubicacion == ubicacion:
                producto.cantidad += int(cantidad)
                return True
        return False

    def vender_producto(self, nombre, cantidad, ubicacion):
        for producto in self.productos:
            if producto.nombre == nombre and producto.ubicacion == ubicacion:
                if producto.cantidad >= int(cantidad):
                    producto.cantidad -= int(cantidad)
                    return True
                else:
                    return False
        return False

    def generar_informe(self, archivo):
        with open(archivo, 'w') as file:
            file.write("Informe de Inventario:\n")
            file.write("Producto Cantidad Precio Unitario Valor Total Ubicacion\n")
            file.write("-" * 70 + "\n")
            for producto in self.productos:
                valor_total = producto.cantidad * producto.precio_unitario
                file.write(f"{producto.nombre} {producto.cantidad} ${producto.precio_unitario:.2f} ${valor_total:.2f} {producto.ubicacion}\n")

    def mostrar_productos(self):
        for producto in self.productos:
                print(f"{producto.nombre} {producto.cantidad} {producto.precio_unitario} {producto.ubicacion}")

