from tkinter import *
import time

canvas_width = 600
canvas_height = 450
point_spacing = 5

flag, x1, y1, x2, y2 = 1, 0, 0, 0, 0

def paint(event):
    global flag, x1, y1, x2, y2
    color = 'red'
    if flag == 1:
        x1, y1 = (event.x), (event.y)
        flag = 0
    x2, y2 = (event.x), (event.y)
    if ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (1 / 2) >= point_spacing:
        c.create_oval(event.x - 2, event.y - 2, event.x + 2, event.y + 2, fill=color, outline=color)
        flag = 1

def on_slider_change(value):
    global point_spacing
    point_spacing = int(value)

# Create the main window
master = Tk()
master.title('Painting in Python')

# Create the canvas
c = Canvas(master, width=canvas_width, height=canvas_height, bg='white')
c.pack(expand=YES, fill=BOTH)
c.bind('<B1-Motion>', paint)

# Create the slider
slider = Scale(master, from_=5, to=100, orient=HORIZONTAL, command=on_slider_change)
slider.pack(side=BOTTOM, padx=20, pady=10)

# Label for the slider
slider_label = Label(master, text='Point Spacing')
slider_label.pack(side=BOTTOM)

# Start the Tkinter event loop
master.mainloop()
