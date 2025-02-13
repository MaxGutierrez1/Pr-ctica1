class Material:
    def __init__(self,título,editorial):
        self.título = título
        self.editorial = editorial
        self.disponibilidad = True

class Libro(Material):
    def __init__(self,título, editorial, autor,género,estado):
        super().__init__(título, editorial,)
        self.autor = autor
        self.género = género
        self.estado = estado
        

class Revista(Material):
    def __init__(self, título, editorial,edición,periodicidad,estado):
        super().__init__(título, editorial)
        self.edición = edición
        self.periodicidad = periodicidad
        self.estado = estado

class MaterialDigital(Material):
    def __init__(self, título, editorial,tipo_archivo,enlace_descarga):
        super().__init__(título, editorial)
        self.archivo = tipo_archivo
        self.enlace = enlace_descarga

class Préstamo:
    def __init__(self,usuario,material,fecha_préstamo,fecha_devolución):
        self.material = material
        self.usuario = usuario
        self.fecha_devolución = fecha_devolución
        self.fecha_préstamo = fecha_préstamo

class Persona:
    def __init__(self,nombre,correo):
        self.nombre = nombre
        self.correo = correo

class Usuario(Persona):
    def __init__(self, nombre, correo):
        super().__init__(nombre, correo)
        self.lista_préstamos = []   
        self.lista_multas = []
    
    def consultar_catálogo(self):
            print ("Materiales disponibles:")
            for n in Catálogo.lista_materiales_disponibles:
                print(n)
            print("Materiales no disponibles:")
            for i in Catálogo.lista_materiales_no_disponibles:
                print(i)
    
    def historial_multas(self):
        print(f"Historial de p penalizaciones del usuario {self.nombre}:")
        for i in self.lista_multas:
            print(i)
    
    def solicitar_préstamo(self,material):
        if material.estado == True:
            return material
        else:
            return f"El material que solicita no se encuentra disponible"
    
    def devolver_material(self,material):
        if material.estado == False:
            Catálogo.lista_materiales_no_disponibles.remove(f"título: {material.título}")
            Catálogo.lista_materiales_disponibles.append(f"título: {material.título}")
            print (f"Se ha devuelto el material: {material.título}")
        else:
            print("Elija un material válido")
             

class Bibliotecario(Persona,Préstamo):
    def __init__(self, nombre, correo):
        super().__init__(nombre, correo)
    
    def agregar_materiales(self,material,sucursal):
        if material.estado == True:
            Catálogo.lista_materiales_disponibles.append(f"título: {material.título}")
        else:
            Catálogo.lista_materiales_no_disponibles.append(f"título: {material.título}")
        sucursal.lista_materiales_sucursal.append(f"título: {material.título}")

    def gestionar_préstamos(self,usuario,material,fecha_préstamo,fecha_devolución):
        Préstamo.nuevo_préstamo = Préstamo(material,usuario,fecha_préstamo,fecha_devolución)
        print (f"Se le ha prestado el material: {self.nuevo_préstamo.material.título} al usuario {self.nuevo_préstamo.usuario.nombre}, con fecha de devolución para: {self.nuevo_préstamo.fecha_devolución}")
        Catálogo.lista_materiales_disponibles.remove(f"título: {self.nuevo_préstamo.material.título}")
        Catálogo.lista_materiales_no_disponibles.append(f"título: {self.nuevo_préstamo.material.título}")
        self.nuevo_préstamo.material.estado = False
    
    def transferir_material(self,material,sucursal_origen,sucursal_destino):
        if material.estado == True:
            sucursal_origen.lista_materiales_sucursal.remove(f"título: {material.título}") 
            sucursal_destino.lista_materiales_sucursal.append(f"título: {material.título}")
            print (f"Se ha Transferido el material: {material.título}")
        else:
            print("Elija un material válido")
    
    def penalizar(self,usuario,multa):
        usuario.lista_multas.append(f"-{multa.multa}")
        print(f"Se le ha aplicado la multa: {multa.multa} al usuario {usuario.nombre} por la devolución tardía del material")

class Sucursal:
    def __init__(self,nombre_sucursal):
        self.nombre_sucursal = nombre_sucursal
        self.lista_materiales_sucursal = []
   

class Penalización:
    def __init__(self,multa):
        self.multa = multa

class Catálogo:
    lista_materiales_disponibles = []
    lista_materiales_no_disponibles = []




 




multa1 = Penalización("El usuario de deberá pagar $20 exceder el tiempo de devolución más de 2 días")
multa2 = Penalización("El usuario deberá pagar $50 por excerder el tiempo de entrega en más de una semana")
Centro = Sucursal("Biblioteca central")
La_paz = Sucursal("Biblioteca de la facultad de filosfía e histora")
TierraLuna = Libro("De la tierra a la luna","Ghandi","Julio Verne","Novela",True)
DeAnimales = Libro("De animales a dioses","Ghandi","Yuval Noah Harari","Historia",False) 
DivinaCom = Libro("La divina comedia","Alianza editorial", " Dante Alighieri", "Epopeta",True)
Muy_int= Revista("¿Vivimos en una simulación?","MUY INTERESANTE", "457", "mensual",True)
Bibliotecario1 = Bibliotecario("Gil Scott", "Gil@gmail.com")
Usuario1 = Usuario("Alejandro Gutiérrez","A.G@gmail.com")
Usuario2 = Usuario("Emmanuel Hernández","Bherve@gmail.com")
Bibliotecario1.agregar_materiales(TierraLuna,Centro)
Bibliotecario1.agregar_materiales(DeAnimales,Centro)
Bibliotecario1.agregar_materiales(Muy_int,La_paz)
Bibliotecario1.agregar_materiales(DivinaCom,La_paz)
Usuario1.consultar_catálogo()
Bibliotecario1.gestionar_préstamos(Usuario1.solicitar_préstamo(TierraLuna),Usuario1,"11/02/2025", "15/02/2025")
Usuario1.devolver_material(TierraLuna)
Bibliotecario1.gestionar_préstamos(Usuario2.solicitar_préstamo(DivinaCom),Usuario2,"15/02/2025", "21/02/2025")
Bibliotecario1.transferir_material(Muy_int,La_paz,Centro)
Bibliotecario1.penalizar(Usuario2,multa1)
Bibliotecario1.penalizar(Usuario2,multa2)
Usuario2.historial_multas()

