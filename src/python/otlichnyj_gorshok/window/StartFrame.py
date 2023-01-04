import tkinter as tk


class StartFrame(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.image = tk.PhotoImage(file="X:\$PyProjects\Otlichnyj-Gorshok\\test.png")
        self.label = tk.Label(self, image=self.image)
        self.label.pack()
