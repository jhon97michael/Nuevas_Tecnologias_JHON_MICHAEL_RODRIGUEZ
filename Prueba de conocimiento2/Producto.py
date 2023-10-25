class Producto:
    def __init__(self, id, nombre, descripcion, costo, cantidad, callback):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.costo = costo
        self.cantidad = cantidad
        self.precio_venta = None
        self.callback = callback  # Callback para calcular el precio de venta

    def calcular_precio_venta(self):
        if self.callback:
            self.precio_venta = self.costo / (1 - self.callback())

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Descripción: {self.descripcion}, " \
               f"Costo: {self.costo}, Cantidad: {self.cantidad}, Precio de Venta: {self.precio_venta}"

class RegistroProductos:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, producto):
        producto.calcular_precio_venta()
        self.productos[producto.id] = producto

    def imprimir_listado_productos(self):
        for producto_id, producto in self.productos.items():
            print(producto)

# Función para obtener el margen de venta del usuario
def obtener_margen_de_venta():
    try:
        margen = float(input("Ingrese el margen de venta como un número decimal (por ejemplo, 0.1 para 10%): "))
        return margen
    except ValueError:
        print("¡Debe ingresar un número decimal válido!")
        return obtener_margen_de_venta()

if __name__ == "__main__":
    registro = RegistroProductos()

    while True:
        try:
            id = int(input("Ingrese el ID del producto: "))
            nombre = input("Ingrese el nombre del producto: ")
            descripcion = input("Ingrese la descripción del producto: ")
            costo = float(input("Ingrese el costo del producto: "))
            cantidad = int(input("Ingrese la cantidad disponible: "))

            producto = Producto(id, nombre, descripcion, costo, cantidad, obtener_margen_de_venta)
            registro.agregar_producto(producto)

            continuar = input("¿Desea agregar otro producto? (S/N): ")
            if continuar.strip().lower() != 's':
                break

        except ValueError:
            print("¡Debe ingresar un valor válido!")

    registro.imprimir_listado_productos()
