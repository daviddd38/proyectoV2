import tkinter as tk
from tkinter import ttk

class ReservationHistoryFrame(ttk.Frame):
    def __init__(self, master, user_controller, user_id):
        super().__init__(master)
        self.user_controller = user_controller
        self.user_id = user_id
        self.create_widgets()

    def create_widgets(self):
        # Lista de reservaciones del usuario
        self.reservation_list = tk.Listbox(self, width=70, height=10)
        self.reservation_list.pack(pady=10)

        # Botón para actualizar la lista de reservaciones
        self.refresh_button = tk.Button(self, text="Actualizar", command=self.load_reservations)
        self.refresh_button.pack(pady=10)

        self.load_reservations()

    def load_reservations(self):
        reservations = self.user_controller.get_user_reservations(self.user_id)
        self.reservation_list.delete(0, tk.END)
        for reservation in reservations:
            self.reservation_list.insert(tk.END, f"ID: {reservation.id_reservacion} - Computador: {reservation.id_computador} - Inicio: {reservation.fecha_inicio.strftime('%Y-%m-%d %H:%M')} - Fin: {reservation.fecha_fin.strftime('%Y-%m-%d %H:%M')} - Estado: {reservation.estado}")