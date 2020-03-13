
from MyPackages.GeometryPackage.vector_class import Vector
from MyPackages.GeometryPackage.point_class import Point
from Group import Group
from Constants import *


class Vehicles(Group):
    def __init__(self, canvas):
        Group.__init__(self, canvas)

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

    def collide_with_entities(self, entities):
        for en in self.entities:
            en.collide_with_entities(entities)

    def update(self):
        for en in self.entities:
            en.update()

    def all_dead(self):
        for en in self.entities:
            if not en.dead:
                return False
        return True
