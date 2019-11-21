# A simple drawing program

from tkinter import *
from tkinter import ttk

root = Tk()
root.attributes('-alpha', 0.3)

# outputs mouseclick information
def mouse_press(event):
    global prev
    prev = event

    print('type: {}'.format(event.type))
    print('widget: {}'.format(event.widget))
    print('num: {}'.format(event.num))
    print('x: {}'.format(event.x))
    print('y: {}'.format(event.y))
    print('x root: {}'.format(event.x_root))
    print('y root: {}'.format(event.y_root))


#draws a black
def drawblack(event):
    global prev

    canvas.create_line(prev.x, prev.y, event.x, event.y, width=4, fill = 'black')
    prev = event

# draws a red line
def drawred(event):
    global prev

    canvas.create_line(prev.x, prev.y, event.x, event.y, width=4, fill = 'red')
    prev = event


#close the program
class quitButton(Button):
    def __init__(self, parent):
        Button.__init__(self, parent)
        self['text'] = 'Good Bye'
        # Command to close the window (the destory method)
        self['command'] = parent.destroy
        self.pack(side=TOP)

quitButton(root)

#in progress
#change to red
#class changered(Button):
#    def __init__(self, parent):
#        Button.__init__(self, parent)
#        self['text'] = 'RED'
#        # Command to close the window (the destory method)
#        self['command'] =
#        self.pack(side=TOP)

#quitButton(root)

#clears the screen
def clearscreen():
    canvas.delete("all")

#button to clear screen
clearscrbutton = Button(root, text ="Cl", command = clearscreen)


#change pen colour
def redpen():
    canvas.bind('<B1-Motion>', drawred)

#button to change to red
redpenbutton = Button(root, text ="RED", command = redpen)


canvas = Canvas(root, width=1920, height=1080, background='white')
clearscrbutton.pack()
redpenbutton.pack()
#clearscrbutton.place(height=100, width=200)
canvas.pack()


canvas.bind('<ButtonPress>', mouse_press)
canvas.bind('<B1-Motion>', drawblack)

if __name__ == '__main__':
    root.mainloop()
