from Entity import Edible
import random
from Constants import *
from Control_functions import *


class Group:
    def __init__(self, canvas):
        self.entities = []
        self.canvas = canvas

    def add_en(self, en):
        self.entities.append(en)

    def draw_all(self):
        for en in self.entities:
            if not en.dead:
                en.draw()

    def update_draw(self):
        for en in self.entities:
            if en.pos_changed:
                en.update_draw()

    def create_random(self, num, hf, color, edible_type):
        for n in range(num):
            obj = Edible(self.canvas, hf, color, edible_type, rand_on_screen('x'), rand_on_screen('y'))
            self.entities.append(obj)

