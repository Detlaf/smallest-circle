import re
import itertools
import numpy as np
from classes import Point

INPUT_FILE = "input.txt"

def generate_points(low=-5, high=5):
    num_points = np.random.randint(25, 60)
    x_rand = np.random.uniform(low, high, num_points)
    y_rand = np.random.uniform(low, high, num_points)

    return x_rand, y_rand

def get_input(filename):
    lst = []
    with open(filename, "r") as f:
        for line in f:
            row = line.strip('\n')
            coords = map(int, re.findall(r'\d+', row))
            lst.append(tuple(coords))
    return lst

def all_points():
    input_xy = get_input(INPUT_FILE)
    xs, ys = generate_points()
    rand_xy = list(zip(xs, ys))
    points = []
    for xy in itertools.chain(input_xy, rand_xy):
        points.append(Point(xy))
    return points
