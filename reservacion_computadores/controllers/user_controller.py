from reservacion_computadores.models.usuario import Usuario
from reservacion_computadores.models.reservacion import Reservacion
from reservacion_computadores.models.computador import Computador
from datetime import datetime

class UserController:
    def login(self, email, contrasena):
        return Usuario.login(email, contrasena)

    def register_user(self, nombre, apellido, email, contrasena):
        return Usuario.register(nombre, apellido, email, contrasena)

    def get_user_reservations(self, user_id):
        return Reservacion.get_user_reservations(user_id)

    def get_all_computers(self):
        return Computador.get_all()

    def get_computer_status(self, computer_id):
        computer = Computador.get_by_id(computer_id)
        if computer:
            current_reservation = Reservacion.get_current_reservation(computer_id)
            if current_reservation:
                return "reservado", current_reservation.fecha_fin
            elif computer.estado == "en_mantenimiento":
                return "en_mantenimiento", None
            else:
                return "disponible", None
        return "no_disponible", None

    def make_reservation(self, user_id, computer_id, start_time, end_time):
        return Reservacion.create(user_id, computer_id, start_time, end_time)

    def cancel_reservation(self, reservation_id):
        return Reservacion.cancel(reservation_id)

    def check_and_update_reservations(self):
        current_time = datetime.now()
        active_reservations = Reservacion.get_active_reservations()
        for reservation in active_reservations:
            if reservation.fecha_fin <= current_time:
                Reservacion.end_reservation(reservation.id_reservacion)
                Computador.update_status(reservation.id_computador, "disponible")