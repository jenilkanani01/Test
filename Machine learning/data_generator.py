from tkinter import *
import time

canvas_width = 600
canvas_height = 450
point_spacing = 5
scale_factor = 1.0

flag, x1, y1, x2, y2 = 1, 0, 0, 0, 0
data = [[],[]]

def paint_continuous(event):
    global flag, x1, y1, x2, y2, data
    color = 'red'
    if flag == 1:
        x1, y1 = (event.x), (event.y)
        flag = 0
    x2, y2 = (event.x), (event.y)
    if ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (1 / 2) >= point_spacing:
        c.create_oval(event.x - 2, event.y - 2, event.x + 2, event.y + 2, fill=color, outline=color)
        data[0].append(event.x - canvas_width / 2)
        data[1].append(canvas_height / 2 - event.y)
        flag = 1

def paint_discrete(event):
    color = 'red'
    c.create_oval(event.x - 2, event.y - 2, event.x + 2, event.y + 2, fill=color, outline=color)
    data[0].append(event.x - canvas_width / 2)
    data[1].append(canvas_height / 2 - event.y)

def on_slider_change(value):
    global point_spacing
    point_spacing = int(value)


def on_mousewheel(event):
    global scale_factor
    if event.delta > 0:
        scale_factor += 0.1  # Zoom in
    else:
        scale_factor -= 0.1 # Zoom out
    print("scale: ",scale_factor)
    c.scale("all", event.x, event.y, 1, 1)
    c.scale("all", event.x, event.y, scale_factor, scale_factor)
    redraw_grid_and_axis()  # Redraw grid and axis

def redraw_grid_and_axis():
    c.delete("grid", "axis")  # Clear existing grid and axis
    draw_grid()
    draw_axis()


def toggle_state():
    if button.cget("text") == "Discrete":
        button.config(text="Continuous")
        c.bind('<B1-Motion>', paint_continuous)
    else:
        button.config(text="Discrete")
        c.bind('<ButtonRelease>', paint_discrete)

def draw_grid():
    global scale_factor
    for i in range(-100 * int((scale_factor) * 10), 100 * int((scale_factor) * 10) + 1,10):
        c.create_line(canvas_width / 2 + i * scale_factor, 0,
                      canvas_width / 2 + i * scale_factor, canvas_height,
                      fill="lightgray", dash=(2, 2), tag="grid")
        c.create_line(0, canvas_height / 2 + i * scale_factor,
                      canvas_width, canvas_height / 2 + i * scale_factor,
                      fill="lightgray", dash=(2, 2), tag="grid")

def draw_axis():
    c.create_line(0, canvas_height / 2, canvas_width, canvas_height / 2, fill="black", tag="axis")  # X axis
    c.create_line(canvas_width / 2, 0, canvas_width / 2, canvas_height, fill="black", tag="axis")  # Y axis


# Create the main window
master = Tk()
master.title('Painting in Python')

# Create the canvas
c = Canvas(master, width=canvas_width, height=canvas_height, bg='white')
c.pack(expand=YES, fill=BOTH)
c.bind('<ButtonRelease>', paint_discrete)
c.bind("<MouseWheel>", on_mousewheel)

# Create the slider
slider = Scale(master, from_=5, to=100, orient=HORIZONTAL, command=on_slider_change)
slider.pack(side=BOTTOM, padx=20, pady=10)

# Label for the slider
slider_label = Label(master, text='Point Spacing')
slider_label.pack(side=BOTTOM)

# Create the binary button
button = Button(master, text="Discrete", command=toggle_state)
button.pack(pady=20)

# Draw initial grid and axis
draw_grid()
draw_axis()

# Start the Tkinter event loop
master.mainloop()
print(data[0])
print(data[1])