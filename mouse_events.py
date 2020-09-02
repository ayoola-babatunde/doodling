# A simple drawing program

from tkinter import *
from tkinter import ttk
from tkinter import colorchooser 

#options to adjust
opacity = 0.7
canvas_height = 600
canvas_width = 1500

root = Tk()
root.attributes('-alpha', opacity)

top = Frame(root)
top.pack(side = TOP)

global canvas
canvas = Canvas(root, width = canvas_width, height = canvas_height, background = 'white')

#clears the screen
def clearscreen():
    canvas.delete("all")

clearscrbutton = Button(root, text ="CLEAR", command = clearscreen)

# outputs mouseclick information
def mouse_press(event, print = False):
    """
    If print = True, the coordinates for actions on the canvas
    will show up in the terminal
    """
    global prev
    prev = event

    if print:
        print('type: {}'.format(event.type))
        print('widget: {}'.format(event.widget))
        print('num: {}'.format(event.num))
        print('x: {}'.format(event.x))
        print('y: {}'.format(event.y))
        print('x root: {}'.format(event.x_root))
        print('y root: {}'.format(event.y_root))

#close the program
class quitButton(Button):
    def __init__(self, parent):
        Button.__init__(self, parent)
        self['text'] = u'\u274C' #unicode ❌ symbol
        self['bg'] = 'red'
        self['command'] = parent.destroy
        self.pack(anchor = 'ne')

quitButton(root)


#draws a line
def draw(event, colour = 'black', line_width = 4):
    global prev
    canvas.create_line(prev.x, prev.y, event.x, event.y, width = line_width, fill = colour)
    prev = event

#change pen colour
def pen(real_col, l_width = 4):
    canvas.bind('<B1-Motion>', lambda event, x = real_col: draw(event, colour = x, line_width = l_width))
    
#set a random color by picking    
def color1():
    color = colorchooser.askcolor()[1]
    return color

#slider for pen size
w1 = Scale(root, from_ = 1, to = 25, orient = HORIZONTAL, label = 'Pen Size')
w1.set(10)
w1.pack(in_ = top, side = RIGHT)

#initializing buttons
blackpenbutton = Button(root, text = u'\u270E', command = lambda x = 'black': pen(real_col = x, l_width = w1.get()), bg = 'black', fg = 'white')
redpenbutton = Button(root, text = u'\u270E', command = lambda x = 'red': pen(real_col = x, l_width = w1.get()), bg = 'red')
orangepenbutton = Button(root, text = u'\u270E', command = lambda x = 'orange': pen(real_col = x, l_width = w1.get()), bg = 'orange')
yellowpenbutton = Button(root, text = u'\u270E', command = lambda x = 'yellow': pen(real_col = x, l_width = w1.get()), bg = 'yellow')
greenpenbutton = Button(root, text = u'\u270E', command = lambda x = 'green': pen(real_col = x, l_width = w1.get()), bg = 'green')
bluepenbutton = Button(root, text = u'\u270E', command = lambda x = 'blue': pen(real_col = x, l_width = w1.get()), bg = 'blue')
indigopenbutton = Button(root, text = u'\u270E', command = lambda x = 'indigo': pen(real_col = x, l_width = w1.get()), bg = 'indigo')
#choose_a_color = colorchooser.askcolor()[1]
#chosen_color = choose_a_color[1]    #to pick up the color name in HTML notation, i.e. the 2nd element of the tuple returned by the colorchooser

brownpenbutton = Button(root, text = u'\u270E', command = lambda x = 'brown': pen(real_col = x, l_width = w1.get()), bg = 'brown')
whitepenbutton = Button(root, text = u'\u270E', command = lambda x = 'white': pen(real_col = x, l_width = w1.get()), bg = 'white')

#adding buttons to canvas
blackpenbutton.pack(in_ = top, side = LEFT)
redpenbutton.pack(in_ = top, side = LEFT)
orangepenbutton.pack(in_ = top, side = LEFT)
yellowpenbutton.pack(in_ = top, side = LEFT)
bluepenbutton.pack(in_ = top, side = LEFT)
greenpenbutton.pack(in_ = top, side = LEFT)
indigopenbutton.pack(in_ = top, side = LEFT)
brownpenbutton.pack(in_ = top, side = LEFT)
whitepenbutton.pack(in_ = top, side = LEFT)

clearscrbutton.pack(in_ = top, side = LEFT)





canvas.pack()
canvas.bind('<ButtonPress>', mouse_press)

canvas.bind('<B1-Motion>', lambda event, x = 'black': draw(event, colour = x))

if __name__ == '__main__':
    root.mainloop()
