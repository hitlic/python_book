import numpy as np


def add(x, y):
    return x + y


def average(lst):
    return np.average(lst)


class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y


def distance(p1, p2):
    return np.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)
