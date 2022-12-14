import tkinter as tk
from PIL import Image, ImageTk
from src.python.otlichnyj_gorshok.quests.QuestYamlReader import QuestYamlReader
from src.python.otlichnyj_gorshok.util import Cons


class StartFrame(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.current_char_index = 0
        self.parent = parent
        self.questYMLReader = QuestYamlReader()

        # Otwieranie zdjęcia i tworzenie tła
        image = Image.open((Cons.JUNGLE_BIND_IMAGES[Cons.CONFIG_FILE['starting_quest']])[0])
        image = image.resize((1024, 1024), Image.ANTIALIAS)
        self.background_image = ImageTk.PhotoImage(image)
        background_label = tk.Label(self, image=self.background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Tworzenie ramki do wyświetlania tekstu
        self.text_frame = tk.Frame(self, bg="white", bd=5)
        self.text_frame.place(relx=0.5, rely=0.7, relwidth=0.9, relheight=0.2, anchor="n")

        # Tworzenie listy tekstów do wyświetlenia
        self.texts = []
        for index in range(0, len(QuestYamlReader.get_quest_dialog(self.questYMLReader))):
            self.texts.append(QuestYamlReader.get_quest_dialog(self.questYMLReader)[index][0])
        self.current_text_index = 0

        # Tworzenie etykiety do wyświetlania tekstu
        self.text_label = tk.Label(self.text_frame, font=("Arial", 16), anchor="nw", justify="left", bd=0,
                                   wraplength=900)
        self.text_label.place(relwidth=1, relheight=1)

        # Odpalenie animacji tekstu
        self.animate_text()

    def animate_text(self):
        # Wyświetlenie kolejnej litery tekstu
        current_text = self.texts[self.current_text_index]
        if self.current_char_index < len(current_text):
            self.text_label.config(text=current_text[:self.current_char_index + 1])
            self.current_char_index += 1
            self.after(75, self.animate_text)
        else:
            # Po wyświetleniu całego tekstu, odczekaj 1 sekundę i wyświetl kolejny tekst lub przejdź do mapy
            self.current_char_index = 0
            if self.current_text_index < len(self.texts) - 1:
                self.current_text_index += 1
                self.after(2000, self.animate_text)
            else:
                self.parent.show_map_frame()

    def show_map_frame(self):
        self.pack_forget()
        self.parent.map_frame.pack(side="right", fill="both", expand=True)
