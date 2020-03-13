import random

FOOD_COLOR = "#00BB00"
POISON_COLOR = "#BB0000"
TARGET_COLOR = "#FFFF66"
VEH_ALIVE = '#00FF00'
VEH_DEAD = '#FF0000'
HEALING_FACTOR = 0.4
POISONING_FACTOR = 0.4
NUM_OF_FOOD = 20
NUM_OF_POISON = 2

NUM_OF_VEHICLES = 10
DEFAULT_R = 4
VEH_SIZE = DEFAULT_R * 3
WIN_WIDTH = 1000  # 700
WIN_HEIGHT = 1050  # 750
MAX_SPEED = 3
FORCE_COEFFICIENT = 0.07
HP_DEC_PER_FRAME = -0.005

LIMIT_RADIUS = 200
LIMIT_ACC_MUL = 5
LIMIT_DIST_POW = 2

PADDING = 50
MENU_HEIGHT = 50
CALC_PER_REFRESH = 10


def rand_on_screen(coord=None):
    if coord == "x":
        return random.randint(PADDING, WIN_WIDTH - PADDING)
    elif coord == "y":
        return random.randint(PADDING, WIN_HEIGHT - PADDING - MENU_HEIGHT)
    else:
        return [random.randint(PADDING, WIN_WIDTH - PADDING), random.randint(PADDING, WIN_HEIGHT - PADDING - MENU_HEIGHT)]


def lerp_color(color0, color1, amount) -> str:
    r1 = (int(color1[1:3], 16) - int(color0[1:3], 16)) * amount + int(color0[1:3], 16)
    g1 = (int(color1[3:5], 16) - int(color0[3:5], 16)) * amount + int(color0[3:5], 16)
    b1 = (int(color1[5:7], 16) - int(color0[5:7], 16)) * amount + int(color0[5:7], 16)

    return "#{:0>2s}{:0>2s}{:0>2s}".format(hex(round(r1))[2:], str(hex(round(g1)))[2:], str(hex(round(b1)))[2:])


print(lerp_color("#aa9900", "#ff0000", 0.1))
