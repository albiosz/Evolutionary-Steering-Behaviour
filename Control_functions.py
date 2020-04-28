import random

from Constants import *

def test_bool() -> bool:
    if test_bool.restart:
        test_bool.restart = False
        return True
    else:
        return False


def restart():
    test_bool.restart = True


def show_range():
    show_range.range = True


def stop():
    if stop.st:
        stop.st = False
    else:
        stop.st = True


def rand_on_screen(coord=None):
    if coord == "x":
        return random.randint(PADDING, CANVAS_WIDTH - PADDING)
    elif coord == "y":
        return random.randint(PADDING, CANVAS_HEIGHT - PADDING)
    else:
        return [random.randint(PADDING, CANVAS_WIDTH - PADDING), random.randint(PADDING, CANVAS_HEIGHT - PADDING)]


def lerp_color(color0, color1, amount) -> str:
    r1 = (int(color1[1:3], 16) - int(color0[1:3], 16)) * amount + int(color0[1:3], 16)
    g1 = (int(color1[3:5], 16) - int(color0[3:5], 16)) * amount + int(color0[3:5], 16)
    b1 = (int(color1[5:7], 16) - int(color0[5:7], 16)) * amount + int(color0[5:7], 16)

    return "#{:0>2s}{:0>2s}{:0>2s}".format(hex(round(r1))[2:], str(hex(round(g1)))[2:], str(hex(round(b1)))[2:])




# arc = c.create_arc(10, 50, 240, 210, extent=150, fill='red')
# l = canvas.create_line(vec.ret_cor(), width=3, fill='red')
# window.bind("<Motion>", veh.move(window.winfo_pointerx() - window.winfo_rootx(), window.winfo_pointery() - window.winfo_rooty()))
# x, y = 0, 0
# def motion(event):
#     global x, y
#     x, y = event.x, event.y
#
#
# window.bind("<Motion>", motion)


# self.dna["RADIUS"]["FOOD"] = LIMIT_RADIUS
# self.dna["RADIUS"]["POISON"] = LIMIT_RADIUS / 2
# self.dna["ACC_MUL"]["FOOD"] = LIMIT_ACC_MUL
# self.dna["ACC_MUL"]["POISON"] = - LIMIT_ACC_MUL
# self.dna["DIST_POW"]["FOOD"] = LIMIT_DIST_POW
# self.dna["DIST_POW"]["POISON"] = -LIMIT_DIST_POW
