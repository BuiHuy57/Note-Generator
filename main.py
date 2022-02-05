import tkinter as tk
from tkinter import *
from random import randint


class defaultWindow(Frame):
    def __init__(self):
        root = tk.Tk()
        tk.Frame.__init__(self)
        self.pack()
        self.master.title("Note Generator")
        self.button1 = Button(self, text="Generate Notes",
                              width=25, command=self.generateNotes)
        self.button1.grid(row=0, column=1, columnspan=2, sticky=W+E+N+S)

    def generateNotes(self):
        notes = ["Ab", "A", "A#", "Bb", "B", "B#", "Cb", "C", "C#", "Db",
                 "D", "D#", "Eb", "E", "E#", "Fb", "F", "F#", "Gb", "G", "G#"]

        generatedNotes = []

        for i in range(0, len(notes)):
            value = randint(0, len(notes) - 1)
            generatedNotes.append(notes[value])

        print(generatedNotes)


def main():
    defaultWindow().mainloop()


if __name__ == "__main__":
    main()
