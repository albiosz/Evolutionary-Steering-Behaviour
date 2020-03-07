import math
import random

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

        self.vertices = [Vector(self.pos.ret_cor()["x1"] - self.r, self.pos.ret_cor()["y1"] - self.r),
                         Vector(self.pos.ret_cor()["x1"] + self.r, self.pos.ret_cor()["y1"] - self.r),
                         Vector(self.pos.ret_cor()["x1"], self.pos.ret_cor()["y1"] + self.r * 2)]

    def draw(self):
        self.entity_draw = self.canvas.create_polygon(list(self.vertices[0].ret_cor().values())[2:4] \
                                                      + list(self.vertices[1].ret_cor().values())[2:4] \
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
            print(self.vertices[num])
            self.vertices[num] = Vector(self.vertices[num].ret_cor()['x1'] - self.pos.ret_cor()['x1'],
                                        self.vertices[num].ret_cor()['y1'] - self.pos.ret_cor()['y1']) \
                                        .set_angle(angle + el[0]) \
                                        .set_mag(el[1]) \
                                        + self.pos
            print(self.vertices[num])

    def move(self):
        self.pos += self.vel
        for num in range(len(self.vertices)):
            self.vertices[num] += self.vel

    def update_draw(self):
        self.set_angle(self.vel.angle())
        self.move()
        self.canvas.coords(self.entity_draw, list(self.vertices[0].ret_cor().values())[2:4] \
                           + list(self.vertices[1].ret_cor().values())[2:4] \
                           + list(self.vertices[2].ret_cor().values())[2:4])

    def update(self):
        if self.dead:
            return

        dsq = self.pos.p1.dsq(self.target.pos.p1)
        if dsq < pow(self.r, 4) + 1:
            self.target.set_pos(random.randint(0, WIN_WIDTH), random.randint(0, WIN_HEIGHT)).update_draw()

        if not self.seeking:
            self.acc += self.seek(self.target.pos)

        self.acc.set_mag(self.vel.mag() / 20)
        self.vel += self.acc
        self.vel.limit(MAX_SPEED)
        self.acc.set_mag(0)

        self.seeking = False

    def seek(self, target):
        return (target.copy() - self.pos).set_mag(MAX_SPEED) - self.vel

    def interact_with_entities(self):
        self.acc.add(self.target + self.pos.rotate(math.pi))
        self.acc = self.target.copy().add.pos.pos()
