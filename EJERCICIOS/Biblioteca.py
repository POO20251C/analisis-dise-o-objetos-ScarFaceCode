class Libro:
    def init(self, titulo, isbn, anio_publicacion):
        self.titulo = titulo
        self.isbn = isbn
        self.anio_publicacion = anio_publicacion

    def mostrar_informacion(self):
        print(f"Título: {self.titulo}, ISBN: {self.isbn}, Año: {self.anio_publicacion}")

class Lector:
    def init(self, numero_socio, fecha_registro):
        self.numero_socio = numero_socio
        self.fecha_registro = fecha_registro
        self.prestamos = []

    def registrar_prestamo(self, prestamo):
        self.prestamos.append(prestamo)

class Prestamo:
    def init(self, libro, lector, fecha_prestamo):
        self.libro = libro
        self.lector = lector
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = None

    def registrar_devolucion(self, fecha_devolucion):
        self.fecha_devolucion = fecha_devolucion
        print(f"Libro '{self.libro.titulo}' devuelto el {fecha_devolucion}.")