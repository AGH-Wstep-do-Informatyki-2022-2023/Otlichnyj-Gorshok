import tkinter as tk


class SkillsFrame(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.configure(bg="purple", width=600, height=600)

    def pack(self, *args, **kwargs):
        for widget in self.parent.winfo_children():
            widget.pack_forget()
        super().pack(*args, **kwargs)
