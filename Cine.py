class Persona:
    lista = []

    def __init__(self, nombre, correo):
        self.nombre = nombre
        self.correo = correo

    def registrar(self):
        Persona.lista.append(self)
        print(f"La persona {self.nombre} ha sido registrada con el correo {self.correo}")

    def actualizar_datos(self, nombre, correo):
        self.nombre = nombre
        self.correo = correo
        print(f"Los datos han sido actualizados")

    @classmethod
    def personas_registradas(cls):
        print("Personas registradas: ")
        for persona in cls.lista:
            print(f"- {persona.nombre} - {persona.correo}")

class Empleado(Persona):
    peliculas = {}

    def __init__(self, nombre, correo, rol):
        super().__init__(nombre, correo)
        self.rol = rol

    def agregar_pelicula(self, titulo, duracion):
        Empleado.peliculas[titulo] = {
            'titulo': titulo,
            'duracion': duracion,
            'funciones': []
        }
        print(f"Pelicula agregada: {titulo} con duración de {duracion} minutos")
        return Empleado.peliculas[titulo]

    def agregar_funcion(self, titulo_pelicula, horario, sala):
        if titulo_pelicula in Empleado.peliculas:
            funcion = {
                'horario': horario,
                'sala': sala,
                'reservas': []
            }
            Empleado.peliculas[titulo_pelicula]['funciones'].append(funcion)
            print(f"Función agregada para la película {titulo_pelicula} a las {horario} en la sala {sala.identificador}")
            return funcion
        else:
            print(f"No se encontró la película {titulo_pelicula}")
            return None

    def agregar_promocion(self, descuento, condiciones):
        nueva_promo = Promocion(descuento, condiciones)
        print(f"Se ha agregado la promoción: {nueva_promo.descuento}%, {nueva_promo.condiciones}")

    def modificar_promocion(self, promocion, nuevo_descuento, nuevas_condiciones):
        promocion.descuento = nuevo_descuento
        promocion.condiciones = nuevas_condiciones
        print(f"Promoción modificada: {nuevo_descuento}% de descuento. {nuevas_condiciones}.")

    def agregar_productos(self, zona, productos, precios):
        zona.menu_productos.append({"Producto": productos, "Precios": precios})
        print(f"Se ha agregado el producto: {productos} al menú de la zona {zona.identificador}")

class Pelicula:
    def __init__(self, titulo, duracion, clasificacion, genero):
        self.titulo = titulo
        self.duracion = duracion
        self.clasificacion = clasificacion
        self.genero = genero

    def detalles(self):
        return f"Título de la película: {self.titulo}, duración: {self.duracion}, clasificación: {self.clasificacion}, género: {self.genero}"

class Funcion:
    def __init__(self, pelicula, sala, hora, asientos_disponibles=None):
        self.pelicula = pelicula
        self.sala = sala
        self.hora = hora
        self.asientos_disponibles = asientos_disponibles or sala.capacidad

class Espacio:
    def __init__(self, capacidad, identificador):
        self.capacidad = capacidad
        self.identificador = identificador

    def descripcion(self):
        print(f"El edificio tiene tamaño {self.capacidad} y tiene id {self.identificador}")

class Zona_de_comida(Espacio):
    def __init__(self, capacidad, identificador):
        super().__init__(capacidad, identificador)
        self.menu_productos = []

    def agregar_productos(self, productos, precios):
        self.menu_productos.append({"Producto": productos, "Precios": precios})
        print(f"Se ha agregado el producto: {productos} al menú")

    def menu(self):
        print("Menú de productos:")
        for i in self.menu_productos:
            print(f"{i['Producto']}: ${i['Precios']}")

class Sala(Espacio):
    def __init__(self, capacidad, identificador, tipo):
        super().__init__(capacidad, identificador)
        self.tipo = tipo
        self.disponibilidad = True

    def consultar_disponibilidad(self):
        if self.disponibilidad:
            print("La sala está disponible")
        else:
            print("La sala está ocupada")

class Reservar(Pelicula):
    def __init__(self, titulo, duracion, clasificacion, genero, usuario, funcion, asiento):
        super().__init__(titulo, duracion, clasificacion, genero)
        self.usuario = usuario
        self.funcion = funcion
        self.asiento = asiento

class Usuario(Persona):
    def __init__(self, nombre, correo):
        super().__init__(nombre, correo)
        self.historial_reservas = []

    def reservar(self, titulo_pelicula, horario, nombre_usuario):
        if titulo_pelicula in Empleado.peliculas:
            for funcion in Empleado.peliculas[titulo_pelicula]['funciones']:
                if funcion['horario'] == horario:
                    funcion['reservas'].append(nombre_usuario)
                    self.historial_reservas.append({
                        "titulo_pelicula": titulo_pelicula,
                        "horario": horario,
                        "sala": funcion['sala']
                    })
                    print(f"Reserva realizada para {nombre_usuario} en la película '{titulo_pelicula}' a las {horario}.")
                    return True
        print(f"No se encontró la función para la película '{titulo_pelicula}' a las {horario}.")
        return False

    def cancelar_reserva(self, funcion):
        reserva = next((r for r in self.historial_reservas if r["funcion"] == funcion), None)
        if reserva:
            funcion.asientos_disponibles += reserva["asientos"]
            self.historial_reservas.remove(reserva)
            print(f"Reserva cancelada para '{funcion.pelicula.titulo}'.")
        else:
            print("No tienes una reserva para esta función.")



class Promocion:
    def __init__(self, descuento, condiciones):
        self.descuento = descuento
        self.condiciones = condiciones

    def mostrar(self):
        print(f"Promoción: {self.descuento}% de descuento. Condiciones: {self.condiciones}")

    def aplicar_promo(self):
        pass

Zona1 = Zona_de_comida(100, "Zona 1")
Zona1.agregar_productos("Palomitas", 90)

pelicula1 = Pelicula("Whiplash", 153.5, "pg-13", "musical")
sala1 = Sala(50, "Sala 1", "IMAX")
sala2 = Sala(35, "Sala 2", "4DX")
funcion1 = Funcion(pelicula1, sala1, "15:30")

Empleado1 = Empleado("Gaby", "godNamj00n@gmail.com", "Gerente")
Empleado1.agregar_pelicula("Whiplash", 153.5)
Empleado1.agregar_funcion("Whiplash", "15:30", sala1)
promocion1 = Promocion(20, "Válido de lunes a jueves.")
promocion1.mostrar()
Usuario1 = Usuario("Emmanuel", "bhervema@gmail.com")
Usuario2 = Usuario("MaxGut", "gmaxcraftq@gmail.com")
Usuario3 = Usuario("Toño", "dibujosan@gmail.com")
Empleado1.agregar_pelicula("tron", 135)
Empleado1.agregar_funcion("tron", "9:00", sala1)
Empleado1.agregar_promocion(30, "En la compra de 2 palomitas grandes")
Empleado1.agregar_productos(Zona1, "Nachos con queso", 80)
Usuario1.registrar()
Usuario2.registrar()
Empleado1.registrar()
Usuario1.reservar("Whiplash", "15:30", "Emmanuel")
Usuario2.reservar("Whiplash", "15:30", "MaxGut")
Usuario3.reservar("tron", "9:00", "Toño")
Zona1.menu()
Persona.personas_registradas()