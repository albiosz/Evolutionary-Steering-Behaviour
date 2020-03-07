from tkinter import *
import time
import math

from Vehicle import Vehicle
from Entity import Entity
from Edibles import Edibles
from MyPackages.GeometryPackage.vector_class import Vector
from Constants import *
window = Tk()

window.title("Evolutionary autonomous vehicles")
window.geometry(f'{WIN_WIDTH}x{WIN_HEIGHT}')

window.bind("<space>", func=lambda e: window.destroy())
Button(window, text="Quit", command=window.destroy).pack()

canvas = Canvas(window, height=WIN_WIDTH, width=WIN_HEIGHT-50, bg='#333333')
canvas.pack()

veh = Vehicle(canvas, '#007700')
type(veh)
veh.draw()
eatable = Edibles(canvas)
eatable.create_random(NUM_OF_FOOD, HEALING_FACTOR, FOOD_COLOR)
eatable.create_random(NUM_OF_POISON, POISONING_FACTOR, POISON_COLOR)
eatable.draw_all()

while True:
    window.update_idletasks()
    window.update()
    veh.update()
    veh.update_draw()
    time.sleep(0.01)



# arc = c.create_arc(10, 50, 240, 210, extent=150, fill='red')
# l = canvas.create_line(vec.ret_cor(), width=3, fill='red')

# window.bind("<Motion>", veh.move(window.winfo_pointerx() - window.winfo_rootx(), window.winfo_pointery() - window.winfo_rooty()))
# x, y = 0, 0
# def motion(event):
#     global x, y
#     x, y = event.x, event.y
#
#
# window.bind("<Motion>", motion)

