import tkinter as tk


class MainWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.geometry("800x600")

        # Tworzenie paska po lewej stronie
        left_frame = tk.Frame(self, width=200, height=600, bg="green")
        left_frame.pack(side="left", fill="both", expand=True)

        # Tworzenie paska po prawej stronie
        right_frame = tk.Frame(self, width=600, height=600, bg="white")
        right_frame.pack(side="right", fill="both", expand=True)

        # Tworzenie przycisków
        character_button = tk.Button(left_frame, text="Postać", command=self.show_character_frame)
        map_button = tk.Button(left_frame, text="Mapa", command=self.show_map_frame)
        skills_button = tk.Button(left_frame, text="Umiejętności", command=self.show_skills_frame)
        character_button.pack()
        map_button.pack()
        skills_button.pack()

        # Tworzenie ramki dla każdego okna
        self.character_frame = tk.Frame(right_frame, width=600, height=600, bg="yellow")
        self.map_frame = tk.Frame(right_frame, width=600, height=600, bg="blue")
        self.skills_frame = tk.Frame(right_frame, width=600, height=600, bg="purple")

    def show_character_frame(self):
        self.character_frame.pack(side="right", fill="both", expand=True)
        self.map_frame.pack_forget()
        self.skills_frame.pack_forget()

    def show_map_frame(self):
        self.character_frame.pack_forget()
        self.map_frame.pack(side="right", fill="both", expand=True)
        self.skills_frame.pack_forget()

    def show_skills_frame(self):
        self.character_frame.pack_forget()
        self.map_frame.pack_forget()
        self.skills_frame.pack(side="right", fill="both", expand=True)


if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
