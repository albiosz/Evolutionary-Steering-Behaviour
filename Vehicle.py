import math
import random
from collections import defaultdict

from Entity import Entity
from MyPackagesCopy.GeometryPackage.vector_class import Vector
from MyPackagesCopy.GeometryPackage.point_class import Point
from Constants import *
from Control_functions import *


class Vehicle(Entity):
    def __init__(self, canvas, color, x=rand_on_screen('x'), y=rand_on_screen('y')):
        Entity.__init__(self, canvas, color, x, y)

        self.seeking = False
        self.hp = 1
        self.dead = False
        self.fit_points = 0
        self.dna = self.random_dna()

        self.vertices = [Vector(self.pos.ret_cor()["x1"] - self.r, self.pos.ret_cor()["y1"] - self.r),
                         Vector(self.pos.ret_cor()["x1"] + self.r, self.pos.ret_cor()["y1"] - self.r),
                         Vector(self.pos.ret_cor()["x1"], self.pos.ret_cor()["y1"] + self.r * 2)]

        self.vel = Vector(0, 1).set_mag(MAX_SPEED).set_angle(random.random()*2*math.pi)
        self.acc = Vector(0, 0)
        self.r = VEH_SIZE
        self.target = Entity(canvas, TARGET_COLOR)

    def update(self, fit_pts):
        if self.dead:
            return

        self.change_hp(HP_DEC_PER_FRAME, fit_pts)

        dsq = self.pos.p1.dsq(self.target.pos.p1)
        if dsq < pow(self.r, 4) + 1:
            self.target.set_pos(rand_on_screen('x'), rand_on_screen('y'))
            self.target.pos_changed = True

        if not self.seeking:
            self.acc += self.seek(self.target.pos)

        self.acc.set_mag(self.vel.mag() * FORCE_COEFFICIENT)
        self.vel += self.acc
        self.vel.limit(MAX_SPEED)
        self.acc.set_mag(0)
        self.move()

        self.seeking = False

    def seek(self, target):
        return (target.copy() - self.pos).set_mag(MAX_SPEED) - self.vel

    def interact_with_entities(self, entities):
        if self.dead:
            return

        sum_acc = Vector(0, 0)
        for e in entities:
            ds = self.pos.p1.dsq(e.pos.p1)
            if ds < pow(self.dna["RADIUS"][e.type], 2):
                sum_acc + ((self.seek(e.pos) * self.dna["ACC_MUL"][e.type]) * (
                            1 / pow(ds, self.dna["DIST_POW"][e.type] / 2)))
                self.seeking = True

        self.acc + sum_acc

    def collide_with_entities(self, entities, fit_pts):
        if self.dead:
            return

        for e in entities:
            if e.dead:
                continue
            dsq = self.pos.p1.dsq(e.pos.p1)
            if dsq < pow(self.r * 2 + e.r, 2):
                e.set_pos(rand_on_screen('x'), rand_on_screen('y'))
                e.pos_changed = True
                self.change_hp(e.healing_factor, fit_pts)

    def change_hp(self, value, fit_pts):
        self.hp += value

        if self.hp <= 0:
            self.dead_routine()
            self.dead = True
            self.fit_points = fit_pts
        elif self.hp > 1:
            self.hp = 1

    def dead_routine(self):
        self.canvas.delete(self.ranges_draw.get('POISON'))
        self.canvas.delete(self.ranges_draw.get('FOOD'))
        self.canvas.delete(self.target.entity_draw)
        self.canvas.itemconfig(self.entity_draw, fill=VEH_DEAD)

    def random_dna(self):
        temp = defaultdict(dict)
        for key1 in LIMITS:
            for key2 in EDIBLE:
                if key1 == "RADIUS":
                    temp[key1][key2] = random.random()*LIMITS[key1]
                else:
                    temp[key1][key2] = random.random()*2*LIMITS[key1] - LIMITS[key1]

        return temp

    def mutate(self):
        for key1 in LIMITS:
            for key2 in EDIBLE:
                if random.random() < MUTATION_RATE:
                    self.dna[key1][key2] += (2*random.random() - 1) * MUTATION_IMPACT*LIMITS[key1]
                    if key1 == 'RADIUS' and self.dna[key1][key2] < 0:
                        self.dna[key1][key2] = 0

                    if random.random() < MUTATION_RATE:
                        self.dna[key1][key2] = self.random_dna()[key1][key2]

