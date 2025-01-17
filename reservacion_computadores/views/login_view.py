import tkinter as tk
from tkinter import messagebox
from reservacion_computadores.controllers.user_controller import UserController
from .user_view import UserView
from .register_view import RegisterView

class LoginView(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.user_controller = UserController()
        self.create_widgets()

    def create_widgets(self):
        self.email_label = tk.Label(self, text="Email:")
        self.email_label.grid(row=0, column=0, padx=10, pady=5)
        self.email_entry = tk.Entry(self)
        self.email_entry.grid(row=0, column=1, padx=10, pady=5)

        self.password_label = tk.Label(self, text="Contraseña:")
        self.password_label.grid(row=1, column=0, padx=10, pady=5)
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.grid(row=1, column=1, padx=10, pady=5)

        self.login_button = tk.Button(self, text="Iniciar sesión", command=self.login)
        self.login_button.grid(row=2, column=0, columnspan=2, pady=10)

        self.register_button = tk.Button(self, text="Registrarse", command=self.open_register_view)
        self.register_button.grid(row=3, column=0, columnspan=2, pady=10)

    def login(self):
        email = self.email_entry.get()
        password = self.password_entry.get()
        user = self.user_controller.login(email, password)
        if user:
            self.master.switch_frame(UserView, user=user)
        else:
            messagebox.showerror("Error", "Email o contraseña incorrectos")

    def open_register_view(self):
        RegisterView(self.master)