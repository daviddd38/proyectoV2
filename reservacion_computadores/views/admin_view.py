import tkinter as tk
from tkinter import ttk
from reservacion_computadores.controllers.admin_controller import AdminController

class AdminView(tk.Frame):
    def __init__(self, master, user):
        super().__init__(master)
        self.master = master
        self.user = user
        self.admin_controller = AdminController()

        self.create_widgets()

    def create_widgets(self):
        self.welcome_label = tk.Label(self, text=f"Bienvenido, {self.user.nombre} (Administrador)")
        self.welcome_label.pack(pady=10)

        # Pestaña de gestión de computadores
        self.notebook = ttk.Notebook(self)
        self.computer_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.computer_frame, text='Gestión de Computadores')

        # Lista de computadores
        self.computer_list = tk.Listbox(self.computer_frame, width=50)
        self.computer_list.pack(pady=10)

        # Botones para gestionar computadores
        self.add_computer_button = tk.Button(self.computer_frame, text="Añadir Computador", command=self.add_computer)
        self.add_computer_button.pack(pady=5)
        self.update_computer_button = tk.Button(self.computer_frame, text="Actualizar Estado", command=self.update_computer_status)
        self.update_computer_button.pack(pady=5)

        # Pestaña de gestión de reservaciones
        self.reservation_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.reservation_frame, text='Gestión de Reservaciones')

        # Lista de reservaciones
        self.reservation_list = tk.Listbox(self.reservation_frame, width=50)
        self.reservation_list.pack(pady=10)

        # Botones para gestionar reservaciones
        self.approve_reservation_button = tk.Button(self.reservation_frame, text="Aprobar Reservación", command=self.approve_reservation)
        self.approve_reservation_button.pack(pady=5)
        self.cancel_reservation_button = tk.Button(self.reservation_frame, text="Cancelar Reservación", command=self.cancel_reservation)
        self.cancel_reservation_button.pack(pady=5)

        self.notebook.pack(expand=1, fill="both")

        # Cargar datos iniciales
        self.load_computers()
        self.load_reservations()

    def load_computers(self):
        computers = self.admin_controller.get_all_computers()
        self.computer_list.delete(0, tk.END)
        for computer in computers:
            self.computer_list.insert(tk.END, f"{computer.nombre} - {computer.estado}")

    def load_reservations(self):
        reservations = self.admin_controller.get_all_reservations()
        self.reservation_list.delete(0, tk.END)
        for reservation in reservations:
            self.reservation_list.insert(tk.END, f"ID: {reservation.id_reservacion} - Estado: {reservation.estado}")

    def add_computer(self):
        # Aquí iría la lógica para abrir una ventana de diálogo para añadir un nuevo computador
        pass

    def update_computer_status(self):
        # Aquí iría la lógica para actualizar el estado de un computador seleccionado
        pass

    def approve_reservation(self):
        # Aquí iría la lógica para aprobar una reservación seleccionada
        pass

    def cancel_reservation(self):
        # Aquí iría la lógica para cancelar una reservación seleccionada
        pass