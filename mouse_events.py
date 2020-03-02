from tkinter import *
from tkinter import ttk

#root
root = Tk()

#adjust opacity
root.attributes('-alpha', 0.9)

top = Frame(root)
top.pack(side = TOP)



# outputs mouseclick information
def mouse_press(event):
    global prev
    prev = event

# draws a red line
def drawred(event):
    global prev
    canvas.create_line(prev.x, prev.y, event.x, event.y, width=4, fill = 'red')
    prev = event

# draws a orange line
def draworange(event):
    global prev
    canvas.create_line(prev.x, prev.y, event.x, event.y, width=4, fill = 'orange')
    prev = event

# draws a yellow line
def drawyellow(event):
    global prev
    canvas.create_line(prev.x, prev.y, event.x, event.y, width=4, fill = 'yellow')
    prev = event

# draws a green line
def drawgreen(event):
    global prev
    canvas.create_line(prev.x, prev.y, event.x, event.y, width=4, fill = 'green')
    prev = event

# draws a blue line
def drawblue(event):
    global prev
    canvas.create_line(prev.x, prev.y, event.x, event.y, width=4, fill = 'blue')
    prev = event

# draws a indigo line
def drawindigo(event):
    global prev
    canvas.create_line(prev.x, prev.y, event.x, event.y, width=4, fill = 'indigo')
    prev = event

# draws a black line
def drawblack(event):
    global prev
    canvas.create_line(prev.x, prev.y, event.x, event.y, width=4, fill = 'black')
    prev = event





#change pen colour to red
def redpen():
    canvas.bind('<B1-Motion>', drawred)

#change pen colour to orange
def orangepen():
    canvas.bind('<B1-Motion>', draworange)

#change pen colour to yellow
def yellowpen():
    canvas.bind('<B1-Motion>', drawyellow)

#change pen colour to green
def greenpen():
    canvas.bind('<B1-Motion>', drawgreen)

#change pen colour to blue
def bluepen():
    canvas.bind('<B1-Motion>', drawblue)

#change pen colour to indigo
def indigopen():
    canvas.bind('<B1-Motion>', drawindigo)

#change pen colour to black
def blackpen():
    canvas.bind('<B1-Motion>', drawblack)





#button to change to red
redpenbutton = Button(root, text = u'\u270E', command = redpen, bg = 'red')

#button to change to orange
orangepenbutton = Button(root, text = u'\u270E', command = orangepen, bg = 'orange')

#button to change to yellow
yellowpenbutton = Button(root, text = u'\u270E', command = yellowpen, bg = 'yellow')

#button to change to green
greenpenbutton = Button(root, text = u'\u270E', command = greenpen, bg = 'green')

#button to change to blue
bluepenbutton = Button(root, text = u'\u270E', command = bluepen, bg = 'blue')

#button to change to indigo
indigopenbutton = Button(root, text = u'\u270E', command = indigopen, bg = 'indigo')

#button to change to black
blackpenbutton = Button(root, text = u'\u270E', command = blackpen, bg = 'black', fg = 'white')



#button to close window
class quitButton(Button):
    def __init__(self, parent):
        Button.__init__(self, parent)
        self['text'] = u'\u274C'
        self['bg'] = 'red'
        self['command'] = parent.destroy
        self.pack(in_ = top, side = RIGHT)

quitButton(root)



#clears the screen
def clearscreen():
    canvas.delete("all")

#button to clear screen
clearscrbutton = Button(root, text = 'CLEAR', command = clearscreen, bg = 'white')


#packs buttons
blackpenbutton.pack(in_ = top, side = LEFT)
redpenbutton.pack(in_ = top, side = LEFT)
orangepenbutton.pack(in_ = top, side = LEFT)
yellowpenbutton.pack(in_ = top, side = LEFT)
greenpenbutton.pack(in_ = top, side = LEFT)
bluepenbutton.pack(in_ = top, side = LEFT)
indigopenbutton.pack(in_ = top, side = LEFT)
clearscrbutton.pack(in_ = top, side = LEFT)



#canvas init
canvas = Canvas(root, width=1920, height=1080, background='white')

canvas.pack()
canvas.bind('<ButtonPress>', mouse_press)
canvas.bind('<B1-Motion>', drawblack)

if __name__ == '__main__':
    root.mainloop()
