from tkinter import *
import time
import math

from Vehicle import Vehicle
from Entity import Entity
from Group import Group
from Vehicles import Vehicles
from MyPackages.GeometryPackage.vector_class import Vector
from Constants import *

def test_bool() -> bool:
    if test_bool.restart:
        test_bool.restart = False
        return True
    else:
        return False


def restart():
    test_bool.restart = True


def show_range():
    show_range.range = True


show_range.range = False
test_bool.restart = False

window = Tk()
but = Frame(window)
but.pack(side=TOP)
can = Frame(window)
can.pack(side=BOTTOM)

window.title("Evolutionary autonomous vehicles")
window.geometry(f'{WIN_WIDTH}x{WIN_HEIGHT}')

test = True
window.bind("<space>", func=lambda e: window.destroy())
Button(window, text="Quit", command=window.destroy).pack(in_=but, side=LEFT)
Button(window, text="Restart", command=restart).pack(in_=but, side=LEFT)

canvas = Canvas(window, height=WIN_WIDTH, width=WIN_HEIGHT-MENU_HEIGHT, bg='#333333')
canvas.pack(in_=can, side=BOTTOM)

while True:
    vehicles = Vehicles(canvas)
    for n in range(NUM_OF_VEHICLES):
        veh = Vehicle(canvas, VEH_ALIVE, rand_on_screen('x'), rand_on_screen('y'))
        veh.random_dna()
        vehicles.add_en(veh)

    vehicles.draw_all()
    # vehicles.draw_range()
    eatable = Group(canvas)
    eatable.create_random(NUM_OF_FOOD, HEALING_FACTOR, FOOD_COLOR, "FOOD")
    eatable.create_random(NUM_OF_POISON, POISONING_FACTOR, POISON_COLOR, "POISON")
    eatable.draw_all()

    while not test_bool():
        # CALCULATIONS
        for n in range(CALC_PER_REFRESH):
            vehicles.collide_with_entities(eatable.entities)
            vehicles.interact_with_entities(eatable.entities)
            vehicles.update()

        # UPDATE DRAW
        window.update_idletasks()
        window.update()
        vehicles.update_draw()
        # vehicles.update_range()
        eatable.update_draw()

        if vehicles.all_dead():
            restart()

        time.sleep(0.1)

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

