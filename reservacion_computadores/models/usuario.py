from .database import Database

class Usuario:
    def __init__(self, id_usuario, nombre, apellido, email, contrasena):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.contrasena = contrasena

    @staticmethod
    def login(email, contrasena):
        db = Database()
        try:
            db.connect()
            query = "SELECT id_usuario, nombre, apellido, email, contrasena FROM Usuarios WHERE email = %s AND contrasena = %s"
            cursor = db.execute_query(query, (email, contrasena))
            user_data = cursor.fetchone()
            if user_data:
                return Usuario(*user_data)
            return None
        except Exception as e:
            print(f"Error en el login: {e}")
            return None
        finally:
            db.disconnect()

    @staticmethod
    def register(nombre, apellido, email, contrasena):
        db = Database()
        try:
            db.connect()
            query = "INSERT INTO Usuarios (nombre, apellido, email, contrasena) VALUES (%s, %s, %s, %s)"
            db.execute_query(query, (nombre, apellido, email, contrasena))
            db.commit()
            return True
        except Exception as e:
            print(f"Error al registrar usuario: {e}")
            db.rollback()
            return False
        finally:
            db.disconnect()