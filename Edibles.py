from Entity import Edible
import random
from Constants import *


class Edibles:
    def __init__(self, canvas):
        self.entities = []
        self.canvas = canvas

    def add_en(self, en):
        self.entities.append(en)

    def draw_all(self):
        for en in self.entities:
            print(en.pos.ret_cor().values())
            en.draw()

    def create_random(self, num, hf, color):
        for n in range(num):
            obj = Edible(self.canvas, hf, color, random.randint(0, WIN_WIDTH), random.randint(0, WIN_HEIGHT))
            self.entities.append(obj)

