import tkinter


c = tkinter.Canvas(width = 801, height = 801, bg = "white")
c.pack()

class square:

    def __init__(self,x,y,color):
        self.x = x
        self.y = y
        self.color = color
        self.render()

    def cords (self):
        return (self.x,self.y)

    def render (self):
        c.create_rectangle(self.x,self.y,self.x+100,self.y+100, fill = self.color, outline = "")

squares = {}

h = -1
cntrl = -1
for y in range(0,800,100):
    cntrl = -cntrl
    for x in range(0,800,100):
        h = h+1
        if cntrl == 1:
                squares["square{}".format(h)] = square(x,y,"light grey")
        if cntrl == -1:
                squares["square{}".format(h)] = square(x,y,"light blue")
        cntrl = -cntrl

class pawn:

    def __init__ (self,x,y,color):
        self.x = x
        self.y = y
        self.color = color
        self.render()

    def render (self):
        self.body = c.create_polygon(self.x+25,self.y+75,self.x+75,self.y+75,self.x+50,self.y+25, fill = self.color)

    def cords(self):
        return (self.x,self.y)

    def move(self,x,y):
        self.x = x
        self.y = y
        c.delete(self.body)
        self.render()

    def delete(self):
        c.delete(self.body)
        


class rook:

    def __init__ (self,x,y,color):
        self.x = x
        self.y = y
        self.color = color
        self.render()

    def render (self):
        self.body = c.create_rectangle(self.x+25,self.y+10,self.x+75,self.y+90, fill = self.color, outline = "")

    def cords(self):
        return (self.x,self.y)

    def move(self,x,y):
        self.x = x
        self.y = y
        c.delete(self.body)
        self.render()

    def delete(self):
        c.delete(self.body)


class knight:

    def __init__ (self,x,y,color):
        self.x = x
        self.y = y
        self.color = color
        self.render()

    def render (self):
        self.body = c.create_oval(self.x+25,self.y+10,self.x+75,self.y+90, fill = self.color, outline = "")

    def cords(self):
        return (self.x,self.y)

    def move(self,x,y):
        self.x = x
        self.y = y
        c.delete(self.body)
        self.render()

    def delete(self):
        c.delete(self.body)


class bish:

    def __init__ (self,x,y,color):
        self.x = x
        self.y = y
        self.color = color
        self.render()

    def render (self):
        self.body = c.create_polygon(self.x+30,self.y+90,self.x+70,self.y+90,self.x+50,self.y+10, fill = self.color)

    def cords(self):
        return (self.x,self.y)

    def move(self,x,y):
        self.x = x
        self.y = y
        c.delete(self.body)
        self.render()

    def delete(self):
        c.delete(self.body)


class queen:

    def __init__ (self,x,y,color):
        self.x = x
        self.y = y
        self.color = color
        self.render()

    def render (self):
        self.body = c.create_polygon(self.x+10,self.y+50,self.x+30,self.y+85,self.x+70,self.y+85,self.x+90,self.y+50,self.x+70,self.y+15,self.x+30,self.y+15, fill = self.color, outline = "")

    def cords(self):
        return (self.x,self.y)

    def move(self,x,y):
        self.x = x
        self.y = y
        c.delete(self.body)
        self.render()

    def delete(self):
        c.delete(self.body)


class king:

    def __init__ (self,x,y,color):
        self.x = x
        self.y = y
        self.color = color
        self.render()

    def render (self):
        self.body = c.create_polygon(self.x+10,self.y+50,self.x+50,self.y+90,self.x+90,self.y+50,self.x+50,self.y+10, fill = self.color, outline = "")

    def cords(self):
        return (self.x,self.y)

    def move(self,x,y):
        self.x = x
        self.y = y
        c.delete(self.body)
        self.render()

    def delete(self):
        c.delete(self.body)


figurky = {}

for y in range(100, 700, 500):
    for x in range (0,800,100):
        if y == 100:
            figurky["blackpawn{}".format(x/100+1)] = pawn(x,y,"black")
        else:
            figurky["whitepawn{}".format(x/100+1)] = pawn(x,y,"white")

for y in range (0,800,700):
    for x in range(0,800,700):
        if y == 0:
            figurky["blackrook{}".format(x/100+1)] = rook(x,y,"black")
        else:
            figurky["whiterook{}".format(x/100+1)] = rook(x,y,"white")


for y in range (0,800,700):
    for x in range(200,600,300):
        if y == 0:
            figurky["blackbish{}".format(x/100+1)] = bish(x,y,"black")
        else:
            figurky["whitebish{}".format(x/100+1)] = bish(x,y,"white")
            


for y in range (0,800,700):
    for x in range(100,700,500):
        if y == 0:
            figurky["blackknight{}".format(x/100+1)] = knight(x,y,"black")
        else:
            figurky["whiteknight{}".format(x/100+1)] = knight(x,y,"white")

for y in range (0,800,700):
    for x in range(300,500,300):
        if y == 0:
            figurky["blackqueen{}".format(x/100+1)] = queen(x,y,"black")
        else:
            figurky["whitequeen{}".format(x/100+1)] = queen(x,y,"white")


for y in range (0,800,700):
    for x in range(400,500,400):
        if y == 0:
            figurky["blackking{}".format(x/100+1)] = king(x,y,"black")
        else:
            figurky["whiteking{}".format(x/100+1)] = king(x,y,"white")



global selected
global carrier
selected =  False
carrier = ""



def click(event):
    x,y = event.x, event.y
    global selected
    global carrier
    if selected != True:
        carrier = ""
        for i in figurky.keys():
            cno = figurky[i].cords()
            if cno[0] - x < 0 and cno[0] - x > -100:
                if cno[1] - y < 0 and cno[1] - y > -100:
                    carrier = i
                    selected = True
    elif selected == True:
        for i in figurky.keys():
            cno = figurky[i].cords()
            if cno[0] - x < 0 and cno[0] - x > -100:
                if cno[1] - y < 0 and cno[1] - y > -100:
                    if figurky[i].cords == figurky[carrier]. cords:
                        break
                    else:
                        figurky[i].delete()
                        del figurky[i]
                        break
        for i in squares.keys():
            cno = squares[i].cords()
            if cno[0] - x < 0 and cno[0] - x > -100:
                if cno[1] - y < 0 and cno[1] - y > -100:
                    figurky[carrier].move(cno[0],cno[1])
                    selected = False
                    carrier = ""
        
        




c.bind('<Button-1>', click)

