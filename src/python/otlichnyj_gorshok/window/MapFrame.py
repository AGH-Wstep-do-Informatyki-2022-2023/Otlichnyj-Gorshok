import tkinter as tk
from PIL import Image, ImageTk
from src.python.otlichnyj_gorshok.util import Cons


class MapFrame(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent

        # Otwieranie zdjęcia i tworzenie tła
        image = Image.open(Cons.OTHER_BIND_IMAGES['map'])
        image = image.resize((1024, 1024), Image.ANTIALIAS)
        self.background_image = ImageTk.PhotoImage(image)
        background_label = tk.Label(self, image=self.background_image)
        background_label.pack(fill='both', expand=True)

    def pack(self, *args, **kwargs):
        for widget in self.parent.winfo_children():
            widget.pack_forget()
        super().pack(*args, **kwargs)
