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

        # Open image and set as background
        image = Image.open((Cons.JUNGLE_BIND_IMAGES[Cons.CONFIG_FILE['starting_quest']])[0])
        image = image.resize((1024, 1024), Image.ANTIALIAS)
        self.background_image = ImageTk.PhotoImage(image)


        # Create label for background image
        background_label = tk.Label(self, image=self.background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Create frame for text and set background color to transparent
        self.text_frame = tk.Label(self, image=self.background_image)
        self.text_frame.place(relx=0.5, rely=0.75, relwidth=0.9, relheight=0.15, anchor="n")

        # Create list of texts to display
        self.texts = []
        for index in range(0, len(QuestYamlReader.get_quest_dialog(self.questYMLReader))):
            self.texts.append(QuestYamlReader.get_quest_dialog(self.questYMLReader)[index][0])
        self.current_text_index = 0

        # Create label to display text
        self.text_label = tk.Label(self.text_frame, font=("Arial", 16), anchor="nw", justify="left", bd=0,
                                   wraplength=900,fg='black')
        self.text_label.place(relwidth=1, relheight=1)

        # Start text animation
        self.animate_text()

    def animate_text(self):
        # Display next letter of text
        current_text = self.texts[self.current_text_index]
        if self.current_char_index < len(current_text):
            self.text_label.config(text=current_text[:self.current_char_index + 1])
            self.current_char_index += 1
            self.after(75, self.animate_text)
        else:
            # After displaying all text, wait 1 second and display next text or go to map
            self.current_char_index = 0
            if self.current_text_index < len(self.texts) - 1:
                self.current_text_index += 1
                self.after(2000, self.animate_text)
            else:
                self.parent.show_map_frame()


    def show_map_frame(self):
        self.pack_forget()
        self.parent.map_frame.pack(side="right", fill="both", expand=True)
