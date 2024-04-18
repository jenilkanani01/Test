from tkinter import *
import time

canvas_width = 600
canvas_height = 450
point_spacing = 5
scale_factor = 1.0

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
        print(event.x,event.y)
        flag = 1

def on_slider_change(value):
    global point_spacing
    point_spacing = int(value)

def on_mousewheel(event):
    global scale_factor
    if event.delta > 0:
        scale_factor *= 1.1  # Zoom in
    else:
        scale_factor /= 1.1  # Zoom out
    c.scale("all", event.x, event.y, scale_factor, scale_factor)


# Create the main window
master = Tk()
master.title('Painting in Python')

# Create the canvas
c = Canvas(master, width=canvas_width, height=canvas_height, bg='white')
c.pack(expand=YES, fill=BOTH)
c.bind('<B1-Motion>', paint)
c.bind("<MouseWheel>", on_mousewheel)

# Create the slider
slider = Scale(master, from_=5, to=100, orient=HORIZONTAL, command=on_slider_change)
slider.pack(side=BOTTOM, padx=20, pady=10)

# Label for the slider
slider_label = Label(master, text='Point Spacing')
slider_label.pack(side=BOTTOM)

# Draw X and Y axes
c.create_line(0, canvas_height / 2, canvas_width, canvas_height / 2, fill="black")  # X axis
c.create_line(canvas_width / 2, 0, canvas_width / 2, canvas_height, fill="black")  # Y axis

# Draw grid lines
for i in range(-10, 11):
    c.create_line(canvas_width / 2 + i * point_spacing * 10, 0, canvas_width / 2 + i * point_spacing * 10, canvas_height, fill="lightgray", dash=(2, 2))
    c.create_line(0, canvas_height / 2 + i * point_spacing * 10, canvas_width, canvas_height / 2 + i * point_spacing * 10, fill="lightgray", dash=(2, 2))


# Start the Tkinter event loop
master.mainloop()
