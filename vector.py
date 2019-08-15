import pygame as pg
from math import pow, sqrt
vec = pg.math.Vector2


class Vector:
    def __init__(self, v, color, pos):
        self.v = v
        self.color = color
        self.pos = pos
        self.l = self.get_lenght()

    def draw(self, sur):
        pg.draw.line(sur, self.color, (self.pos.x, self.pos.y),
                     (self.pos.x + self.v.x, self.pos.y + self.v.y))

    def get_lenght(self):
        return sqrt(pow(self.v.x, 2) + pow(self.v.y, 2))

# class Vector:
#     def __init__(self, length, angle, color, pos):
#         self.length = length
#         self.angle = angle
#         self.color = color
#         self.pos = pos
#         self.v = vec(length, 0).rotate(-self.angle)
#
#     def draw(self, sur):
#         sur.draw.line(sur, self.color, (self.pos.x, self.pos.y),
#                       (self.pos.x + v.x, self.pos.y + v.y))
