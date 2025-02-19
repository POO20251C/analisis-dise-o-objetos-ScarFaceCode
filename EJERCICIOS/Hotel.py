class Habitacion:
    def init(self, numero, tipo, tarifa_noche):
        self.numero = numero
        self.tipo = tipo
        self.tarifa_noche = tarifa_noche

    def mostrar_informacion(self):
        print(f"Número: {self.numero}, Tipo: {self.tipo}, Tarifa por noche: {self.tarifa_noche}")

class Huésped:
    def init(self, id_huesped, fecha_registro):
        self.id_huesped = id_huesped
        self.fecha_registro = fecha_registro
        self.reservas = []

    def realizar_reserva(self, reserva):
        self.reservas.append(reserva)

class Reserva:
    def init(self, habitacion, huesped, fecha_inicio, fecha_fin):
        self.habitacion = habitacion
        self.huesped = huesped
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.estado = "pendiente"

    def actualizar_estado(self, estado):
        self.estado = estado
        print(f"Reserva para habitación {self.habitacion.numero} actualizada a '{estado}'.")