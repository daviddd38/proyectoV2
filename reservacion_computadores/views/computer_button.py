import tkinter as tk

class ComputerButton(tk.Canvas):
    def __init__(self, master, computer, user_controller, *args, **kwargs):
        super().__init__(master, width=100, height=100, *args, **kwargs)
        self.computer = computer
        self.user_controller = user_controller
        self.draw()
        self.bind("<Enter>", self.show_description)
        self.bind("<Leave>", self.hide_description)

    def draw(self):
        color = self.get_status_color()
        self.create_oval(10, 10, 90, 90, fill=color, outline="")
        self.create_text(50, 50, text=self.computer.id_computador, fill="white", font=("Helvetica", 16, "bold"))
        self.create_text(50, 95, text=self.computer.nombre, fill="black", font=("Helvetica", 10))

    def get_status_color(self):
        status, _ = self.user_controller.get_computer_status(self.computer.id_computador)
        if status == "disponible":
            return "green"
        elif status == "reservado":
            return "orange"
        elif status == "en_mantenimiento":
            return "red"
        else:
            return "gray"

    def show_description(self, event):
        x = self.winfo_rootx() + event.x
        y = self.winfo_rooty() + event.y
        self.tooltip = tk.Toplevel(self)
        self.tooltip.wm_overrideredirect(True)
        self.tooltip.wm_geometry(f"+{x}+{y}")
        status, end_time = self.user_controller.get_computer_status(self.computer.id_computador)
        description = f"{self.computer.descripcion}\nEstado: {status}"
        if end_time and status == "reservado":
            description += f"\nDisponible a partir de: {end_time.strftime('%I:%M %p')}"
        label = tk.Label(self.tooltip, text=description, background="lightyellow", relief="solid", borderwidth=1)
        label.pack()

    def hide_description(self, event):
        if hasattr(self, 'tooltip'):
            self.tooltip.destroy()