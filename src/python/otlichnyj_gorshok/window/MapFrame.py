import tkinter as tk


class MapFrame(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.configure(bg="blue", width=1024, height=1024)

    def pack(self, *args, **kwargs):
        for widget in self.parent.winfo_children():
            widget.pack_forget()
        super().pack(*args, **kwargs)
