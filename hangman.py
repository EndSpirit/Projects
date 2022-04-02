import tkinter as tk
import random

c = tk.Canvas(width = 800, height = 750, bg = "white")
c.pack()

class game:

    def __init__(self):
        c.create_text(400,680,text = "input a letter:")
        self.entry = tk.Entry(c, bg= "light grey", width = 10)
        c.create_window(400, 700, window = self.entry)
        button1 = tk.Button(text = "potvrdit", command = self.input_)
        c.create_window(760,725, window = button1)
        button2 = tk.Button(text = "znova", command = self.reset)
        c.create_window(40,725, window = button2)
        self.game_loop()

    def reset(self):
        c.delete("delete", "reset")
        c.update()
        self.game_loop()
            
    def game_loop(self):
        self.original = random.choice(("pomaranc", "banan", "auto", "skola", "ouagadougou",
        "citron", "melon","pocitac","krtko","maminka","pes","vankus","lopata","cintorin","magnet",
        "python","vozidlo","sopka","kura","pecivo","matematika","psychologia", "cicavec"))
        self. hang = 0
        self.won = False
        self.hanged = False
        self.word = []
        self.word_safe = list(self.original)
        for letter in self.original:
            self.word.append("_ ")
        c.create_text(400,650, text = ''.join(str(letter) for letter in self.word), font = 100, tag = "delete")
        c.update()
        self.update()

    def input_(self):
        self.update()
        x = str(self.entry.get()).lower()
        self.entry.delete(0, 'end')
        pocet = self.word_safe.count(x)
        if pocet > 0:
            for i in range(0,pocet):
                miesto = self.word_safe.index(x)
                self.word[miesto] = x
                self.word_safe[miesto] = "control_deletion"
                self.update()
            if self.word.count("_ ") == 0 and self.hanged != True:
                self.update()
                c.create_text(700,630, text = "vyhral si", tag = "reset")
                self.won = True
                
        else:
            self.update()
            c.create_text(700,650, text = "Toto pismeno nieje v slove", tag = "delete")
            self.hangman()            

    def update(self):
        c.delete("delete")
        c.create_text(400,650, text = ''.join(str(letter) for letter in self.word), font = 100, tag = "delete")

    def hangman(self):
        if self.won != True:
            if self.hang == 0:
                c.create_oval(300,300,500,500, fill = "white",tag = "reset")
                c.create_rectangle(300,400,500,500, fill= "white", outline = "white",tag = "reset")
            if self.hang == 1:
                c.create_line(400,300,400,100,tag = "reset")
            if self.hang == 2:
                c.create_line(400,100,500,100,tag = "reset")
                c.create_line(450,100,400,150,tag = "reset")
            if self.hang == 3:
                c.create_line(500,100,500,150,tag = "reset")
            if self.hang == 4:
                c.create_oval(475,150,525,200, fill = "white",tag = "reset")
            if self.hang == 5:
                c.create_line(500,200,500,275,tag = "reset")
            if self.hang == 6:
                c.create_line(500,275,525,310,tag = "reset")
                c.create_line(500,275,475,310,tag = "reset")
            if self.hang >=7:
                c.create_line(500,225,525,260,tag = "reset")
                c.create_line(500,225,475,260,tag = "reset")
                c.create_text(700,630, text = "Prehral si", tag = "reset")
                self.hanged = True
            self.hang += 1
      
game1 = game()





    
        

