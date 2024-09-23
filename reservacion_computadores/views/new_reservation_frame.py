import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime, timedelta
from .computer_button import ComputerButton

class NewReservationFrame(ttk.Frame):
    def __init__(self, master, user_controller, user_id, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.user_controller = user_controller
        self.user_id = user_id
        self.selected_computer = None
        self.create_widgets()

    def create_widgets(self):
        # Frame para los computadores
        self.computers_frame = ttk.Frame(self)
        self.computers_frame.pack(pady=20)

        # Scrollbar para los computadores
        self.computers_canvas = tk.Canvas(self.computers_frame)
        self.computers_scrollbar = ttk.Scrollbar(self.computers_frame, orient="vertical", command=self.computers_canvas.yview)
        self.scrollable_frame = ttk.Frame(self.computers_canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.computers_canvas.configure(
                scrollregion=self.computers_canvas.bbox("all")
            )
        )

        self.computers_canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.computers_canvas.configure(yscrollcommand=self.computers_scrollbar.set)

        self.computers_canvas.pack(side="left", fill="both", expand=True)
        self.computers_scrollbar.pack(side="right", fill="y")

        # Frame para los elementos de la nueva reservación
        self.new_reservation_elements = ttk.Frame(self)
        self.new_reservation_elements.pack(pady=20)

        # Selector de fecha
        self.date_label = tk.Label(self.new_reservation_elements, text="Fecha de Reservación:")
        self.date_label.grid(row=0, column=0, sticky="w", pady=5)
        self.date_var = tk.StringVar()
        self.date_dropdown = ttk.Combobox(self.new_reservation_elements, textvariable=self.date_var, width=12, state="readonly")
        self.date_dropdown['values'] = [datetime.now().strftime("%Y-%m-%d"), (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")]
        self.date_dropdown.set(datetime.now().strftime("%Y-%m-%d"))
        self.date_dropdown.grid(row=0, column=1, sticky="w", pady=5)

        # Selector de hora de inicio
        self.start_time_label = tk.Label(self.new_reservation_elements, text="Hora de Inicio:")
        self.start_time_label.grid(row=1, column=0, sticky="w", pady=5)
        self.start_hour_var = tk.StringVar()
        self.start_minute_var = tk.StringVar()
        self.start_ampm_var = tk.StringVar()
        self.start_hour_dropdown = ttk.Combobox(self.new_reservation_elements, textvariable=self.start_hour_var, width=5)
        self.start_hour_dropdown['values'] = [f"{i:02d}" for i in range(1, 13)]
        self.start_hour_dropdown.grid(row=1, column=1, sticky="w", pady=5)
        self.start_minute_dropdown = ttk.Combobox(self.new_reservation_elements, textvariable=self.start_minute_var, width=5)
        self.start_minute_dropdown['values'] = [f"{i:02d}" for i in range(0, 60, 5)]
        self.start_minute_dropdown.grid(row=1, column=2, sticky="w", pady=5)
        self.start_ampm_dropdown = ttk.Combobox(self.new_reservation_elements, textvariable=self.start_ampm_var, width=5)
        self.start_ampm_dropdown['values'] = ['AM', 'PM']
        self.start_ampm_dropdown.grid(row=1, column=3, sticky="w", pady=5)

        # Selector de hora de fin
        self.end_time_label = tk.Label(self.new_reservation_elements, text="Hora de Fin:")
        self.end_time_label.grid(row=2, column=0, sticky="w", pady=5)
        self.end_hour_var = tk.StringVar()
        self.end_minute_var = tk.StringVar()
        self.end_ampm_var = tk.StringVar()
        self.end_hour_dropdown = ttk.Combobox(self.new_reservation_elements, textvariable=self.end_hour_var, width=5)
        self.end_hour_dropdown['values'] = [f"{i:02d}" for i in range(1, 13)]
        self.end_hour_dropdown.grid(row=2, column=1, sticky="w", pady=5)
        self.end_minute_dropdown = ttk.Combobox(self.new_reservation_elements, textvariable=self.end_minute_var, width=5)
        self.end_minute_dropdown['values'] = [f"{i:02d}" for i in range(0, 60, 5)]
        self.end_minute_dropdown.grid(row=2, column=2, sticky="w", pady=5)
        self.end_ampm_dropdown = ttk.Combobox(self.new_reservation_elements, textvariable=self.end_ampm_var, width=5)
        self.end_ampm_dropdown['values'] = ['AM', 'PM']
        self.end_ampm_dropdown.grid(row=2, column=3, sticky="w", pady=5)

        # Botón para hacer reservación
        self.make_reservation_button = tk.Button(self.new_reservation_elements, text="Hacer Reservación", command=self.make_reservation)
        self.make_reservation_button.grid(row=3, column=0, columnspan=4, pady=20)

        self.load_all_computers()

    def load_all_computers(self):
        computers = self.user_controller.get_all_computers()
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        for i, computer in enumerate(computers):
            computer_button = ComputerButton(self.scrollable_frame, computer, self.user_controller)
            computer_button.grid(row=i//5, column=i%5, padx=10, pady=10)
            computer_button.bind("<Button-1>", lambda e, c=computer: self.select_computer(c))

    def select_computer(self, computer):
        status, end_time = self.user_controller.get_computer_status(computer.id_computador)
        if status != "disponible":
            if end_time and status == "reservado":
                messagebox.showwarning("Advertencia", f"El computador {computer.nombre} estará disponible a partir de: {end_time.strftime('%I:%M %p')}")
            else:
                messagebox.showwarning("Advertencia", f"El computador {computer.nombre} no está disponible para reservar.")
            return
        self.selected_computer = computer
        messagebox.showinfo("Selección", f"Has seleccionado el computador {computer.nombre}")

    def make_reservation(self):
        if not self.selected_computer:
            messagebox.showwarning("Advertencia", "Por favor, seleccione un computador")
            return
        date_str = self.date_var.get()
        start_hour = self.start_hour_var.get()
        start_minute = self.start_minute_var.get()
        start_ampm = self.start_ampm_var.get()
        end_hour = self.end_hour_var.get()
        end_minute = self.end_minute_var.get()
        end_ampm = self.end_ampm_var.get()
        if not start_hour or not start_minute or not start_ampm or not end_hour or not end_minute or not end_ampm:
            messagebox.showwarning("Advertencia", "Por favor, seleccione horas válidas")
            return
        try:
            fecha_inicio = datetime.strptime(f"{date_str} {start_hour}:{start_minute} {start_ampm}", "%Y-%m-%d %I:%M %p")
            fecha_fin = datetime.strptime(f"{date_str} {end_hour}:{end_minute} {end_ampm}", "%Y-%m-%d %I:%M %p")
            if fecha_fin <= fecha_inicio:
                messagebox.showwarning("Advertencia", "La hora de fin debe ser posterior a la hora de inicio")
                return
        except ValueError:
            messagebox.showerror("Error", "Formato de fecha u hora inválido")
            return
        success = self.user_controller.make_reservation(self.user_id, self.selected_computer.id_computador, fecha_inicio, fecha_fin)
        if success:
            messagebox.showinfo("Éxito", "Reservación creada correctamente")
            self.load_all_computers()
            self.selected_computer = None
        else:
            messagebox.showerror("Error", "No se pudo crear la reservación")