import tkinter as tk
from views.login_view import LoginView
from views.user_view import UserView

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema de Reservación de Computadores")
        self.geometry("800x600")
        self.current_frame = None
        self.switch_frame(LoginView)

    def switch_frame(self, frame_class, *args, **kwargs):
        new_frame = frame_class(self, *args, **kwargs)
        if self.current_frame is not None:
            self.current_frame.destroy()
        self.current_frame = new_frame
        self.current_frame.pack(fill=tk.BOTH, expand=True)

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()