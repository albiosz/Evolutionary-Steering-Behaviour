import math

from MyPackagesCopy.GeometryPackage.vector_class import Vector
from MyPackagesCopy.GeometryPackage.point_class import Point
from Group import Group
from Constants import *
from Vehicle_draw import VehicleDraw
from copy import copy, deepcopy
from Control_functions import *


class Vehicles(Group):
    def __init__(self, canvas, num=0, color=VEH_ALIVE):
        Group.__init__(self, canvas)
        self.num_alive = num

        for n in range(num):
            veh = VehicleDraw(canvas, color,  rand_on_screen('x'), rand_on_screen('y'))
            veh.random_dna()
            self.add_en(veh)

    def update_draw(self):
        for en in self.entities:
            en.update_draw()

    def draw_range(self):
        for en in self.entities:
            en.draw_range()

    def update_range(self):
        for en in self.entities:
            en.update_range()

    def interact_with_entities(self, entities):
        for en in self.entities:
            en.interact_with_entities(entities)

    def collide_with_entities(self, entities, time_sim):
        for en in self.entities:
            en.collide_with_entities(entities, time_sim)

    def update(self, fit_pts):
        for en in self.entities:
            en.update(fit_pts)

    def all_dead(self):
        for en in self.entities:
            if not en.dead:
                return False

        return True

    def calc_alive(self):
        alive = 0
        for en in self.entities:
            if not en.dead:
                alive += 1

        self.num_alive = alive
        return alive

    def create_random(self, color=VEH_ALIVE):
        for n in range(num):
            obj = Vehicle(self.canvas, color, rand_on_screen('x'), rand_on_screen('y'))
            self.entities.append(obj)

    def populate(self):
        fit_sum = 0
        partition = []
        for en in self.entities:
            fit_sum += math.floor(math.sqrt(en.fit_points))
            partition.append(fit_sum)

        old_population = self.entities[:]
        self.entities = []
        for el in old_population:
            veh = VehicleDraw(self.canvas, VEH_ALIVE)
            for key1 in veh.dna:
                for key2 in veh.dna[key1]:
                    r_num = math.floor(random.random()*fit_sum)
                    idx = 0
                    for par in partition:
                        if r_num > par:
                           idx += 1

                    veh.dna[key1][key2] = old_population[idx].dna[key1][key2]

            veh.mutate()
            self.add_en(veh)