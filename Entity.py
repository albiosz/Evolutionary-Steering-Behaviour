from MyPackages.GeometryPackage.vector_class import Vector
from MyPackages.GeometryPackage.point_class import Point
from Constants import *
import random
import time
from tkinter import *
random.seed(time.clock())


class Entity:
    def __init__(self, canvas, color, x=random.randint(0, WIN_WIDTH), y=random.randint(0, WIN_HEIGHT)):
        self.pos = Vector(x, y)
        self.color = color
        self.r = DEFAULT_R
        self.canvas = canvas
        self.entity_draw = 0
        self.pos_changed = False

    def draw(self):
        x1 = self.pos.ret_cor()["x1"]
        y1 = self.pos.ret_cor()["y1"]
        r = self.r

        self.entity_draw = self.canvas.create_oval([x1 - r, y1 - r, x1 + r, y1 + r], fill=self.color, outline=self.color)

    def set_pos(self, x, y):
        self.pos = Vector(x, y)
        return self

    def update_draw(self):
        x1 = self.pos.ret_cor()["x1"]
        y1 = self.pos.ret_cor()["y1"]
        r = self.r

        self.canvas.coords(self.entity_draw, [x1 - r, y1 - r, x1 + r, y1 + r])


class Edible(Entity):
    def __init__(self, canvas, hf, color, edible_type, x=random.randint(0, WIN_WIDTH), y=random.randint(0, WIN_HEIGHT)):
        Entity.__init__(self, canvas, color, x, y)
        self.type = edible_type
        self.healing_factor = hf
        self.dead = False
