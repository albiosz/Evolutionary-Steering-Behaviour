import math
import random
from collections import defaultdict

from Entity import Entity
from MyPackages.GeometryPackage.vector_class import Vector
from MyPackages.GeometryPackage.point_class import Point
from Constants import *


class Vehicle(Entity):
    def __init__(self, canvas, color, x=random.randint(0, WIN_WIDTH), y=random.randint(0, WIN_HEIGHT - 50)):
        Entity.__init__(self, canvas, color, x, y)

        self.r = VEH_SIZE

        self.vel = Vector(0, 1).set_mag(MAX_SPEED)
        self.acc = Vector(0, 0)

        # self.target = Vector(random.randint(0, WIN_WIDTH), random.randint(0, WIN_HEIGHT))
        self.target = Entity(canvas, TARGET_COLOR)
        self.seeking = False
        self.dead = False

        self.dna = defaultdict(dict)

        self.ranges_draw = {}

        self.vertices = [Vector(self.pos.ret_cor()["x1"] - self.r, self.pos.ret_cor()["y1"] - self.r),
                         Vector(self.pos.ret_cor()["x1"] + self.r, self.pos.ret_cor()["y1"] - self.r),
                         Vector(self.pos.ret_cor()["x1"], self.pos.ret_cor()["y1"] + self.r * 2)]

    def draw(self):
        self.entity_draw = self.canvas.create_polygon(list(self.vertices[0].ret_cor().values())[2:4]
                                                      + list(self.vertices[1].ret_cor().values())[2:4]
                                                      + list(self.vertices[2].ret_cor().values())[2:4],
                                                      fill=self.color)

        self.target.draw()

    def rotate(self, angle):
        for num in range(len(self.vertices)):
            self.vertices[num] = Vector(self.vertices[num].ret_cor()['x1'] - self.pos.ret_cor()['x1'],
                                        self.vertices[num].ret_cor()['y1'] - self.pos.ret_cor()['y1']) \
                                        .rotate(angle) \
                                        + self.pos

    def set_angle(self, angle):

        # difference of point angles with length
        angle_dif = [(3 * math.pi / 4, self.r), (-3 * math.pi / 4, self.r), (0, 2 * self.r)]

        for num, el in enumerate(angle_dif):
            self.vertices[num] = Vector(self.vertices[num].ret_cor()['x1'] - self.pos.ret_cor()['x1'],
                                        self.vertices[num].ret_cor()['y1'] - self.pos.ret_cor()['y1']) \
                                        .set_angle(angle + el[0]) \
                                        .set_mag(el[1]) \
                                        + self.pos

    def move(self):
        self.pos += self.vel
        for num in range(len(self.vertices)):
            self.vertices[num] += self.vel

    def update_draw(self):
        if self.target.pos_changed:
            self.target.update_draw()

        self.set_angle(self.vel.angle())
        self.move()
        self.canvas.coords(self.entity_draw, list(self.vertices[0].ret_cor().values())[2:4]
                           + list(self.vertices[1].ret_cor().values())[2:4]
                           + list(self.vertices[2].ret_cor().values())[2:4])

    def update(self):
        if self.dead:
            return

        dsq = self.pos.p1.dsq(self.target.pos.p1)
        if dsq < pow(self.r, 4) + 1:
            self.target.set_pos(random.randint(0, WIN_WIDTH), random.randint(0, WIN_HEIGHT))
            self.target.pos_changed = True

        if not self.seeking:
            self.acc += self.seek(self.target.pos)

        self.acc.set_mag(self.vel.mag() * FORCE_COEFFICIENT)
        self.vel += self.acc
        self.vel.limit(MAX_SPEED)
        self.acc.set_mag(0)

        self.seeking = False

    def seek(self, target):
        return (target.copy() - self.pos).set_mag(MAX_SPEED) - self.vel

    def interact_with_entities(self, entities):
        sum_acc = Vector(0, 0)
        for e in entities:
            ds = self.pos.p1.dsq(e.pos.p1)
            if ds < pow(self.dna["RADIUS"][e.type], 2):
                sum_acc + ((self.seek(e.pos) * self.dna["ACC_MUL"][e.type])*(1/pow(ds, self.dna["DIST_POW"][e.type] / 2)))
                self.seeking = True

        self.acc + sum_acc
        
    def collide_with_entities(self, entities):
        if self.dead:
            return

        for e in entities:
            if e.dead:
                continue
            dsq = self.pos.p1.dsq(e.pos.p1)
            if dsq < pow(self.r * 2 + e.r, 2):
                e.set_pos(random.randint(0, WIN_WIDTH), random.randint(0, WIN_HEIGHT))
                e.pos_changed = True
                # self.health += e.healing_factor

    def draw_range(self):
        radiuses = [[self.dna["RADIUS"]["FOOD"], FOOD_COLOR, "FOOD"],
                    [self.dna["RADIUS"]["POISON"], POISON_COLOR, "POISON"]]

        for el in radiuses:
            self.ranges_draw[el[2]] = self.canvas.create_oval([self.pos.p1.x-el[0], self.pos.p1.y-el[0],
                                                               self.pos.p1.x+el[0], self.pos.p1.y+el[0]],
                                                               outline=el[1])

    def update_range(self):
        radiuses = [[self.dna["RADIUS"]["FOOD"], FOOD_COLOR, "FOOD"],
                    [self.dna["RADIUS"]["POISON"], POISON_COLOR, "POISON"]]

        for el in radiuses:
            self.canvas.coords(self.ranges_draw[el[2]], [self.pos.p1.x-el[0], self.pos.p1.y-el[0],
                                                         self.pos.p1.x+el[0], self.pos.p1.y+el[0]])

    def random_dna(self):
        self.dna["RADIUS"]["FOOD"] = LIMIT_RADIUS
        self.dna["RADIUS"]["POISON"] = LIMIT_RADIUS /2
        self.dna["ACC_MUL"]["FOOD"] = LIMIT_ACC_MUL
        self.dna["ACC_MUL"]["POISON"] = - LIMIT_ACC_MUL
        self.dna["DIST_POW"]["FOOD"] = LIMIT_DIST_POW
        self.dna["DIST_POW"]["POISON"] = -LIMIT_DIST_POW

        # self.dna["RADIUS"]["FOOD"] = random.random()*LIMIT_RADIUS
        # self.dna["RADIUS"]["POISON"] = random.random()*LIMIT_RADIUS
        # self.dna["ACC_MUL"]["FOOD"] = random.random()*2*LIMIT_ACC_MUL - LIMIT_ACC_MUL
        # self.dna["ACC_MUL"]["POISON"] = random.random()*2*LIMIT_ACC_MUL - LIMIT_ACC_MUL
        # self.dna["DIST_POW"]["FOOD"] = random.random()*2*LIMIT_DIST_POW - LIMIT_DIST_POW
        # self.dna["DIST_POW"]["POISON"] = random.random()*2*LIMIT_DIST_POW - LIMIT_DIST_POW
