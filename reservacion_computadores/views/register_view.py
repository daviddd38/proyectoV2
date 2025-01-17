import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from reservacion_computadores.controllers.user_controller import UserController

class RegisterView(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Registro de Usuario")
        self.geometry("300x250")
        self.resizable(False, False)
        self.user_controller = UserController()

        self.create_widgets()

    def create_widgets(self):
        # Nombre
        tk.Label(self, text="Nombre:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.nombre_entry = tk.Entry(self)
        self.nombre_entry.grid(row=0, column=1, padx=10, pady=5)

        # Apellido
        tk.Label(self, text="Apellido:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.apellido_entry = tk.Entry(self)
        self.apellido_entry.grid(row=1, column=1, padx=10, pady=5)

        # Correo electrónico
        tk.Label(self, text="Correo electrónico:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.email_entry = tk.Entry(self)
        self.email_entry.grid(row=2, column=1, padx=10, pady=5)

        # Contraseña
        tk.Label(self, text="Contraseña:").grid(row=3, column=0, padx=10, pady=5, sticky="e")
        self.contrasena_entry = tk.Entry(self, show="*")
        self.contrasena_entry.grid(row=3, column=1, padx=10, pady=5)

        # Confirmar contraseña
        tk.Label(self, text="Confirmar contraseña:").grid(row=4, column=0, padx=10, pady=5, sticky="e")
        self.confirm_contrasena_entry = tk.Entry(self, show="*")
        self.confirm_contrasena_entry.grid(row=4, column=1, padx=10, pady=5)

        # Botón de registro
        self.register_button = tk.Button(self, text="Registrarse", command=self.register)
        self.register_button.grid(row=5, column=0, columnspan=2, pady=20)

    def register(self):
        nombre = self.nombre_entry.get()
        apellido = self.apellido_entry.get()
        email = self.email_entry.get()
        contrasena = self.contrasena_entry.get()
        confirm_contrasena = self.confirm_contrasena_entry.get()

        if not all([nombre, apellido, email, contrasena, confirm_contrasena]):
            messagebox.showerror("Error", "Por favor, complete todos los campos.")
            return

        if contrasena != confirm_contrasena:
            messagebox.showerror("Error", "Las contraseñas no coinciden.")
            return

        success = self.user_controller.register_user(nombre, apellido, email, contrasena)
        if success:
            messagebox.showinfo("Éxito", "Usuario registrado correctamente.")
            self.destroy()
        else:
            messagebox.showerror("Error", "No se pudo registrar el usuario. Por favor, intente de nuevo.")