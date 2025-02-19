class Mascota:
    def init(self, nombre, especie, fecha_nacimiento):
        self.nombre = nombre
        self.especie = especie
        self.fecha_nacimiento = fecha_nacimiento

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}, Especie: {self.especie}, Fecha de nacimiento: {self.fecha_nacimiento}")

class Dueño:
    def init(self, id_dueño, fecha_registro):
        self.id_dueño = id_dueño
        self.fecha_registro = fecha_registro
        self.mascotas = []

    def registrar_mascota(self, mascota):
        self.mascotas.append(mascota)

class Cita:
    def init(self, mascota, dueño, fecha_cita):
        self.mascota = mascota
        self.dueño = dueño
        self.fecha_cita = fecha_cita
        self.estado = "pendiente"

    def completar_cita(self):
        self.estado = "completada"
        print(f"Cita para {self.mascota.nombre} completada.")

Enviar mensaje a #general
