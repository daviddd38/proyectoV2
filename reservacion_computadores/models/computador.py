from .database import Database

class Computador:
    ESTADOS_VALIDOS = ['disponible', 'reservado', 'en_mantenimiento']

    def __init__(self, id_computador=None, nombre=None, descripcion=None, estado=None):
        self.id_computador = id_computador
        self.nombre = nombre
        self.descripcion = descripcion
        self.estado = estado if estado in self.ESTADOS_VALIDOS else 'disponible'

    @staticmethod
    def get_all():
        db = Database()
        db.connect()
        query = "SELECT * FROM Computadores"
        cursor = db.execute_query(query)
        computadores = [Computador(*row) for row in cursor.fetchall()]
        db.disconnect()
        return computadores

    @staticmethod
    def get_available():
        db = Database()
        db.connect()
        query = "SELECT * FROM Computadores WHERE estado = 'disponible'"
        cursor = db.execute_query(query)
        computadores = [Computador(*row) for row in cursor.fetchall()]
        db.disconnect()
        return computadores

    @staticmethod
    def update_status(id_computador, new_status):
        if new_status not in Computador.ESTADOS_VALIDOS:
            raise ValueError(f"Estado no válido. Debe ser uno de: {', '.join(Computador.ESTADOS_VALIDOS)}")
        db = Database()
        db.connect()
        query = "UPDATE Computadores SET estado = %s WHERE id_computador = %s"
        db.execute_query(query, (new_status, id_computador))
        db.disconnect()

    @staticmethod
    def get_by_id(id_computador):
        db = Database()
        db.connect()
        query = "SELECT * FROM Computadores WHERE id_computador = %s"
        cursor = db.execute_query(query, (id_computador,))
        result = cursor.fetchone()
        db.disconnect()
        if result:
            return Computador(*result)
        return None