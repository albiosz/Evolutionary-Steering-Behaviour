from tkinter import *
import time
import math

from Vehicle import Vehicle
from Entity import Entity
from Edibles import Edibles
from MyPackages.GeometryPackage.vector_class import Vector
from Constants import *


def test_bool():
    if test_bool.bool:
        test_bool.bool = False
        return True
    else:
        return False


def set_bool():
    test_bool.bool = True

test_bool.bool = False

window = Tk()
but = Frame(window)
but.pack(side=TOP)
can = Frame(window)
can.pack(side=BOTTOM)

window.title("Evolutionary autonomous vehicles")
window.geometry(f'{WIN_WIDTH}x{WIN_HEIGHT}')

window.bind("<space>", func=lambda e: window.destroy())
Button(window, text="Quit", command=window.destroy).pack(in_=but, side=LEFT)
Button(window, text="Restart", command=set_bool).pack(in_=but, side=LEFT)

canvas = Canvas(window, height=WIN_WIDTH, width=WIN_HEIGHT-50, bg='#333333')
canvas.pack(in_=can,side=BOTTOM)

while True:
    veh = Vehicle(canvas, '#007700')
    veh.random_dna()
    type(veh)
    veh.draw()
    veh.draw_range()
    eatable = Edibles(canvas)
    eatable.create_random(NUM_OF_FOOD, HEALING_FACTOR, FOOD_COLOR, "FOOD")
    eatable.create_random(NUM_OF_POISON, POISONING_FACTOR, POISON_COLOR, "POISON")
    eatable.draw_all()

    while not test_bool():
        window.update_idletasks()
        window.update()
        veh.collide_with_entities(eatable.entities)
        veh.interact_with_entities(eatable.entities)
        veh.update()
        veh.update_draw()
        veh.update_range()
        eatable.update_draw()
        print(veh.vel)
        time.sleep(0.01)

    canvas.delete("all")






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

