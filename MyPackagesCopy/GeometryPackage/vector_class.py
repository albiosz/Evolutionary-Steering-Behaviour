from MyPackages.GeometryPackage.point_class import Point
from copy import copy, deepcopy
import math


class Vector:
    def __init__(self, x1, y1, x0=0, y0=0):
        self.p0 = Point(x0, y0)
        self.p1 = Point(x1, y1)

    def __add__(self, vec):
        self.p0 + vec.p0
        self.p1 + vec.p1
        return self

    def __sub__(self, vec):
        self.p0 - vec.p0
        self.p1 - vec.p1
        return self

    def __mul__(self, m): # multiply length by number
        self.p1 *= m
        return self

    def __gt__(self, vec):  # check if greater
        return self.mag() > vec.mag()

    def __str__(self):
        return f"([({self.p0.x}, {self.p0.y}),({self.p1.x}, {self.p1.y})], len = {self.mag()})"
    
    def mag(self):
        return math.hypot(self.magx(), self.magy())

    def ret_cor(self):
        return {"x0": self.p0.x, "y0": self.p0.y, "x1": self.p1.x, "y1": self.p1.y}

    def magx(self):
        return abs(self.p0.x-self.p1.x)

    def magy(self):
        return abs(self.p0.y-self.p1.y)

    def normalize(self):
        self.p1 *= (1/self.mag())
        return self

    def set_mag(self, m):
        self.normalize()*m
        return self

    def angle(self):
        return math.atan2(self.p1.y - self.p0.y, self.p1.x - self.p0.x)
    
    def set_angle(self, angle):
        self.p1.x = self.mag() * math.cos(angle) + self.p0.x
        self.p1.y = self.mag() * math.sin(angle) + self.p0.y
        return self

    def rotate(self, a):
        new_ang = self.angle() + a
        self.p1.npos(self.mag() * math.cos(new_ang) + self.p0.x, self.mag() * math.sin(new_ang) + self.p0.y)
        return self

    def copy(self):
        return deepcopy(self)
    
    def limit(self, n):
        if self.mag() > n:
            self.set_mag(n)

