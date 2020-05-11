"""
    Merges randomly generated points and points from 
    the input file in a list of <Point>
"""

import re
import itertools
import numpy as np
from classes import Point

INPUT_FILE = "input.txt"

def generate_points(low=-15, high=15):
    """
        Generates random number ([25, 60)) of random 
        x and y coordinates

        Parameters
        ----------
        low = -15: int
            low limit for the generated coordinates
        high = 15 : int
            high limit for the generated coordinates

        Returns
        ----------
        x_rand, y_rand : ndarray 
            arrays of samples from parameterized uniform distribution
    """
    num_points = np.random.randint(25, 60)
    x_rand = np.random.uniform(low, high, num_points)
    y_rand = np.random.uniform(low, high, num_points)

    return x_rand, y_rand

def read_input(filename):
    """
        Reads list of coordinates from the given file

        Parameters
        ----------
        filename : str
            path to the file containing coordinates
        
        Returns
        ----------
        lst : list of <tuple>
            list of coordinates from the given file
    """
    lst = []
    with open(filename, "r") as f:
        for line in f:
            row = line.strip('\n')
            coords = map(int, re.findall(r'\d+', row))
            lst.append(tuple(coords))
    return lst

def all_points():
    """
        Merges lists with randomly generated points and points from the given file

        Parameters
        ----------
            none
        
        Returns
        ----------
        points : list of <Point>
            list of the coordinates for which should be calculated the smalles circle
    """
    input_xy = read_input(INPUT_FILE)
    xs, ys = generate_points()
    rand_xy = list(zip(xs, ys))
    points = []
    for xy in itertools.chain(input_xy, rand_xy):
        points.append(Point(xy))
    return points
