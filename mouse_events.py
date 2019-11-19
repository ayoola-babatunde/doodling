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


# draws a line
def draw(event):
    global prev

    canvas.create_line(prev.x, prev.y, event.x, event.y, width=4)
    prev = event



canvas = Canvas(root, width=1920, height=1080, background='white')
canvas.pack()

canvas.bind('<ButtonPress>', mouse_press)
canvas.bind('<B1-Motion>', draw)

if __name__ == '__main__':
    root.mainloop()
