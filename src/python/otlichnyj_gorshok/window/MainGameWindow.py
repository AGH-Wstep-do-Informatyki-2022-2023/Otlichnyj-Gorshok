import tkinter as tk
from src.python.otlichnyj_gorshok.util import Cons
from src.python.otlichnyj_gorshok.window.CharacterFrame import CharacterFrame
from src.python.otlichnyj_gorshok.window.MapFrame import MapFrame
from src.python.otlichnyj_gorshok.window.SkillsFrame import SkillsFrame
from src.python.otlichnyj_gorshok.window.StartFrame import StartFrame


class MainGameWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.geometry("1182x1024")

        # Tworzenie paska po lewej stronie
        left_frame = tk.Frame(self, width=250, height=1024, bg="green")
        left_frame.pack(side="left", fill="both", expand=True)

        # Tworzenie paska po prawej stronie
        if Cons.USER_FILE['quest'] == 'TQ1':
            self.right_frame = StartFrame(self, width=1024, height=1024)
            self.right_frame.pack(side="right", fill="both", expand=True)
        else:
            self.right_frame = tk.Frame(self, width=1024, height=1024, bg="red")
            self.right_frame.pack(side="right", fill="both", expand=True)

        # Tworzenie przycisków
        character_button = tk.Button(left_frame, text="Postać", command=self.show_character_frame)
        map_button = tk.Button(left_frame, text="Mapa", command=self.show_map_frame)
        skills_button = tk.Button(left_frame, text="             Umiejętności             ", command=self.show_skills_frame)
        character_button.pack()
        map_button.pack()
        skills_button.pack()

        # Tworzenie ramki dla każdego okna
        self.character_frame = CharacterFrame(self.right_frame)
        self.map_frame = MapFrame(self.right_frame)
        self.skills_frame = SkillsFrame(self.right_frame)

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
