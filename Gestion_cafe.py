class Persona:
    def __init__(self, nombre, correo):
        self.nombre = nombre
        self.correo = correo

class Cliente(Persona):
    def __init__(self, nombre, correo):
        super().__init__(nombre, correo)
        self.historial_pedidos = []

    def realizar_pedido(self, pedido):
        self.historial_pedidos.append(pedido)

    def consultar_historial(self):
        historial = []
        for pedido in self.historial_pedidos:
            productos = [producto.nombre for producto in pedido.productos]
            historial.append(productos)
        return historial

class Empleado(Persona):
    def __init__(self, nombre, correo, rol):
        super().__init__(nombre, correo)
        self.rol = rol

    def actualizar_ingrediente(self, inventario, ingrediente, cantidad):
        inventario.ingredientes[ingrediente] = cantidad
        print(f"Ingrediente actualizado: {ingrediente} - Cantidad: {cantidad}")

    def consultar_disponibilidad(self, inventario, ingrediente, cantidad):
        disponible = ingrediente in inventario.ingredientes and inventario.ingredientes[ingrediente] >= cantidad
        print(f"Disponibilidad de {ingrediente}: {'Suficiente' if disponible else 'Insuficiente'}")
        return disponible

class ProductoBase:
    def __init__(self, nombre, precio, tipo_producto):
        self.nombre = nombre
        self.precio = precio
        self.tipo_producto = tipo_producto

class Bebida(ProductoBase):
    def __init__(self, nombre, precio, tamaño, tipo, opciones_personalizables):
        super().__init__(nombre, precio, "bebida")
        self.tamaño = tamaño
        self.tipo = tipo
        self.opciones_personalizables = opciones_personalizables

class Postre(ProductoBase):
    def __init__(self, nombre, precio, vegano, sin_gluten):
        super().__init__(nombre, precio, "postre")
        self.vegano = vegano
        self.sin_gluten = sin_gluten

class Inventario:
    def __init__(self):
        self.ingredientes = {}

class Pedido:
    def __init__(self):
        self.productos = []
        self.estado = 'pendiente'
        self.total = 0

    def agregar_producto(self, producto):
        self.productos.append(producto)
        self.total += producto.precio
        print(f"Producto agregado: {producto.nombre}")

    def calcular_total(self):
        return self.total

class Promocion:
    def __init__(self, condicion, descuento):
        self.condicion = condicion
        self.descuento = descuento

    def aplicar_descuento(self, pedido):
        for producto in pedido.productos:
            if producto.tipo_producto == "postre" and producto.nombre == "Tiramisú":
                pedido.total -= self.descuento
                print(f"Promoción aplicada: {self.condicion}")
                break

Cliente1 = Cliente("Max", "g@gmail.com")
Empleado1 = Empleado("Emma", "emma@gmail.com", "barista")
Bebida1 = Bebida("Americano", 50, "grande", "caliente", ["leche de almendra", "sin azúcar"])
Bebida2 = Bebida("Latte", 65, "grande", "caliente", ["leche deslactosada", "poca azúcar"])
Postre1 = Postre("Pastel de chocolate", 30, True, False)
Postre2 = Postre("Tiramisú", 40, False, False)
Inventario1 = Inventario()
Empleado1.actualizar_ingrediente(Inventario1, "leche de almendra", 100)
Empleado1.actualizar_ingrediente(Inventario1, "azúcar", 50)
Pedido1 = Pedido()
Pedido1.agregar_producto(Bebida1)
Pedido1.agregar_producto(Postre2)
Promo = Promocion("Descuento especial Tiramisú", 10)
Promo.aplicar_descuento(Pedido1)

Cliente1.realizar_pedido(Pedido1)

print(f"Total del pedido: {Pedido1.calcular_total()}")
print(f"Historial de pedidos del cliente: {Cliente1.consultar_historial()}")