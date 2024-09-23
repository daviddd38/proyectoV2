from reservacion_computadores.models.computador import Computador
from reservacion_computadores.models.reservacion import Reservacion

class AdminController:
    def get_all_computers(self):
        return Computador.get_all()

    def get_all_reservations(self):
        # Esta función necesitaría ser implementada en el modelo Reservacion
        # Por ahora, retornamos una lista vacía
        return []

    def add_computer(self, nombre, descripcion):
        # Esta función necesitaría ser implementada en el modelo Computador
        pass

    def update_computer_status(self, id_computador, new_status):
        computador = Computador(id_computador=id_computador)
        computador.update_status(new_status)

    def approve_reservation(self, id_reservacion):
        reservacion = Reservacion(id_reservacion=id_reservacion)
        reservacion.update_status('activa')

    def cancel_reservation(self, id_reservacion):
        reservacion = Reservacion(id_reservacion=id_reservacion)
        reservacion.update_status('cancelada')