from tkinter import *
import time
import math

from Vehicle_draw import VehicleDraw
from Entity import Entity
from Group import Group
from Vehicles import Vehicles
from MyPackagesCopy.GeometryPackage.vector_class import Vector
from Constants import *
from Control_functions import *

stop.st = False
show_range.range = False
test_bool.restart = False

window = Tk()
but = Frame(window)
but.pack(side=TOP)
can = Frame(window)
can.pack(side=BOTTOM)

window.title("Evolutionary autonomous vehicles")
window.geometry(f'{CANVAS_WIDTH}x{CANVAS_HEIGHT+35}')

window.bind("<space>", func=lambda e: stop())
label = Label(window, text="Calculations per frame").pack(in_=but, side=LEFT)
entry = Entry(window)
entry.insert(0, str(CALC_PER_FRAME))
entry.pack(in_=but, side=LEFT)
Button(window, text="Quit", command=window.destroy).pack(in_=but, side=LEFT)
# Button(window, text="Restart", command=restart).pack(in_=but, side=LEFT)
label1 = Label(window, text="Press 'Space' to pause").pack(in_=but, side=LEFT)

canvas = Canvas(window, height=CANVAS_HEIGHT, width=CANVAS_WIDTH, bg='#333333')
canvas.pack(in_=can, side=BOTTOM)

vehicles = Vehicles(canvas, NUM_OF_VEHICLES, VEH_ALIVE)
time_sim_best = -1
time_sim = 0
while True:
    vehicles.draw_all()
    vehicles.draw_range()
    eatable = Group(canvas)
    eatable.create_random(NUM_OF_FOOD, EDIBLE['FOOD'], FOOD_COLOR, "FOOD")
    eatable.create_random(NUM_OF_POISON, EDIBLE['POISON'], POISON_COLOR, "POISON")
    eatable.draw_all()

    if time_sim > time_sim_best:
        time_sim_best = time_sim
    time_text = canvas.create_text(CANVAS_WIDTH - 10, 2, anchor=NE, font=("Purisa", 40), text=time_sim_best, fill="#6a65d6")
    num_veh_text = canvas.create_text(10, 2, anchor=NW, font=("Purisa", 40), text=vehicles.num_alive, fill="#6a65d6")

    time_sim = 0
    end = False
    while not test_bool():
        # CALCULATIONS
        for n in range(CALC_PER_FRAME):
            vehicles.collide_with_entities(eatable.entities, time_sim)
            vehicles.interact_with_entities(eatable.entities)
            vehicles.update(time_sim)
            time_sim += 1
            if vehicles.all_dead():
                vehicles.populate()
                restart()
                end = True
                break

        # UPDATE DRAW
        while not end:
            window.update_idletasks()
            window.update()
            vehicles.update_draw()
            vehicles.update_range()
            eatable.update_draw()
            if time_sim > time_sim_best:
                time_sim_best = time_sim
            canvas.itemconfig(num_veh_text, text=vehicles.calc_alive())
            if not stop.st:
                break

        try:
            CALC_PER_FRAME = int(entry.get())
        except:
            CALC_PER_FRAME = 1

        time.sleep(1/FPS)

    canvas.delete("all")

