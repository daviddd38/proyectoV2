from .database import Database
from datetime import datetime

class Reservacion:
    def __init__(self, id_reservacion, id_usuario, id_computador, fecha_inicio, fecha_fin, estado):
        self.id_reservacion = id_reservacion
        self.id_usuario = id_usuario
        self.id_computador = id_computador
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.estado = estado

    @staticmethod
    def get_user_reservations(user_id):
        db = Database()
        try:
            db.connect()
            query = """
            SELECT id_reservacion, id_usuario, id_computador, fecha_inicio, fecha_fin, estado
            FROM Reservaciones
            WHERE id_usuario = %s
            ORDER BY fecha_inicio DESC
            """
            cursor = db.execute_query(query, (user_id,))
            reservations = [Reservacion(*row) for row in cursor.fetchall()]
            return reservations
        except Exception as e:
            print(f"Error al obtener las reservaciones del usuario: {e}")
            return []
        finally:
            db.disconnect()

    @staticmethod
    def create(id_usuario, id_computador, fecha_inicio, fecha_fin):
        db = Database()
        try:
            db.connect()
            query = """
            INSERT INTO Reservaciones (id_usuario, id_computador, fecha_inicio, fecha_fin, estado)
            VALUES (%s, %s, %s, %s, 'activa')
            """
            db.execute_query(query, (id_usuario, id_computador, fecha_inicio, fecha_fin))
            db.commit()
            return True
        except Exception as e:
            print(f"Error al crear la reservación: {e}")
            db.rollback()
            return False
        finally:
            db.disconnect()

    @staticmethod
    def cancel(id_reservacion):
        db = Database()
        try:
            db.connect()
            query = "UPDATE Reservaciones SET estado = 'cancelada' WHERE id_reservacion = %s"
            db.execute_query(query, (id_reservacion,))
            db.commit()
            return True
        except Exception as e:
            print(f"Error al cancelar la reservación: {e}")
            db.rollback()
            return False
        finally:
            db.disconnect()

    @staticmethod
    def get_active_reservations():
        db = Database()
        try:
            db.connect()
            query = """
            SELECT id_reservacion, id_usuario, id_computador, fecha_inicio, fecha_fin, estado
            FROM Reservaciones
            WHERE estado = 'activa' AND fecha_fin > NOW()
            """
            cursor = db.execute_query(query)
            reservations = [Reservacion(*row) for row in cursor.fetchall()]
            return reservations
        except Exception as e:
            print(f"Error al obtener las reservaciones activas: {e}")
            return []
        finally:
            db.disconnect()

    @staticmethod
    def end_reservation(id_reservacion):
        db = Database()
        try:
            db.connect()
            query = "UPDATE Reservaciones SET estado = 'finalizada' WHERE id_reservacion = %s"
            db.execute_query(query, (id_reservacion,))
            db.commit()
            return True
        except Exception as e:
            print(f"Error al finalizar la reservación: {e}")
            db.rollback()
            return False
        finally:
            db.disconnect()

    @staticmethod
    def get_current_reservation(id_computador):
        db = Database()
        try:
            db.connect()
            query = """
            SELECT id_reservacion, id_usuario, id_computador, fecha_inicio, fecha_fin, estado
            FROM Reservaciones
            WHERE id_computador = %s AND estado = 'activa' AND NOW() BETWEEN fecha_inicio AND fecha_fin
            LIMIT 1
            """
            cursor = db.execute_query(query, (id_computador,))
            reservation_data = cursor.fetchone()
            if reservation_data:
                return Reservacion(*reservation_data)
            return None
        except Exception as e:
            print(f"Error al obtener la reservación actual: {e}")
            return None
        finally:
            db.disconnect()