import tkinter
import random

words = [
    "sur",
    "il",
    "dans",
    "à",
    "avec",
    "les",
    "va",
    "ami",
    "la",
    "elle",
]
phrases = [
    "C'est maman.",
    """Regarde!
C'est le papa.""",
    """Maman Regarde
papa.""",
    """Voici grand-
papa.""",
    """"C'est papa," dit
maman.""",
#     """ Maman a le petit 
# poisson rouge.""",
#     """Papa a le grand 
# lapin brun.""",
#     """"Voici le lapin," 
# dit maman""",
#     """Papa regarde 
# maman.""",
#     """Voici le petit 
# lapin orange.""",
#     """Regarde le 
# grand lit.""",
]

working_set = None
current_index = 0


def set_words():
    global working_set, current_index
    current_index = 0
    working_set = random.sample(words, len(words))


def set_phrases():
    global working_set, current_index
    current_index = 0
    working_set = random.sample(phrases, len(phrases))


set_words()


class App(tkinter.Frame):
    def __init__(self, master=None):
        tkinter.Frame.__init__(self, master)
        self.master = master
        self.label = tkinter.Label(text="", fg="Black", font=("Helvetica", 64))
        self.label.place(x=200, y=200)
        self.correct_button = tkinter.Button(text="Correct", command=self.correct)#.pack(pady=5)
        self.correct_button.place(x=100, y=800)

        self.wrong_button = tkinter.Button(root, text="Wrong", command=self.wrong)
        self.wrong_button.place(x=250, y=800)
        
        self.word_button = tkinter.Button(root, text="WORDS", command=self.set_words)
        self.word_button.place(x=100, y=100)
        self.phrase_button = tkinter.Button(root, text="PHRASES", command=self.set_phrases)
        self.phrase_button.place(x=250, y=100)
        
        self.correct()  # kick off the program

        # self.after(1000, self.update_clock)

    def correct(self):
        global current_index
        current_index += 1
        if current_index >= len(working_set):
            self.label.configure(text="You're all done!!!")
            return
        self.label.configure(text=working_set[current_index])
    def set_phrases(self):
        set_phrases()
        self.label.configure(text=working_set[current_index])
    def set_words(self):
        set_words()
        self.label.configure(text=working_set[current_index])

    def wrong(self):
        global current_index, working_set
        working_set.append(working_set[current_index])
        current_index += 1

        self.label.configure(text=working_set[current_index])


root = tkinter.Tk()
app = App(root)
root.wm_title("Milo's Sight Words")
root.geometry("200x200")
# root.after(1000, app.update_clock)
root.mainloop()
