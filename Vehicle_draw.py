import math


from Vehicle import Vehicle
from MyPackagesCopy.GeometryPackage.vector_class import Vector
from Constants import *
from Control_functions import *


class VehicleDraw(Vehicle):
    def __init__(self, canvas, color, x=rand_on_screen('x'), y=rand_on_screen('y')):
        Vehicle.__init__(self, canvas, color, x=rand_on_screen('x'), y=rand_on_screen('y'))

        self.ranges_draw = {}

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
        if self.dead:
            return

        if self.target.pos_changed:
            self.target.update_draw()

        self.set_angle(self.vel.angle())
        self.canvas.itemconfig(self.entity_draw, fill=lerp_color(VEH_DEAD, VEH_ALIVE, self.hp))
        self.canvas.coords(self.entity_draw, list(self.vertices[0].ret_cor().values())[2:4]
                           + list(self.vertices[1].ret_cor().values())[2:4]
                           + list(self.vertices[2].ret_cor().values())[2:4])

    def draw_range(self):
        for el in EDIBLE:
            r = self.dna["RADIUS"][el]
            self.ranges_draw[el] = self.canvas.create_oval([self.pos.p1.x - r, self.pos.p1.y - r,
                                                            self.pos.p1.x + r, self.pos.p1.y + r],
                                                           outline=RADIUS_COLOR[el])

    def update_range(self):
        for el in EDIBLE:
            r = self.dna["RADIUS"][el]
            self.canvas.coords(self.ranges_draw[el],
                               [self.pos.p1.x - r, self.pos.p1.y - r,
                               self.pos.p1.x + r, self.pos.p1.y + r])

    def draw_vectors(self):
        pass