import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, val):
        self.x += val.x
        self.y += val.y
        return self

    def __sub__(self, val):
        self.x -= val.x
        self.y -= val.y
        return self
    
    def __mul__(self, m):
        self.x *= m
        self.y *= m
        return self

    def pos(self):
        return self.x, self.y

    def npos(self, x, y=0):
        self.x = x
        self.y = y
        return self

    def move(self, x, y=0):
        self.x += x
        self.y += y
        return self
    
    def dsq(self, point):
        return (self.x - point.x)**2 +  (self.y - point.y)**2