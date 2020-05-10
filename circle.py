'''
    Ritter's bounding sphere:
        1. Pick a point x from P
        2. Search for a point y in P, which has the maximum distance from x
        3. Search for a point z in P, which has the maximum distance from y
        4. Set up an initial ball B, with its centre at the midpoint of y and z, 
            the radius as half of the distance between y and z
        5. If all points in P are within the ball B, then we get the bounding sphere
        5a. Otherwise, let p be the point outside the ball, which is at distance d from the border of B.
            Move the centre of B towards p by d/2 and increase radius by d/2 to get a new ball.
'''

import math
import numpy as np
import matplotlib.pyplot as plt

class Circle():
    def __init__(self, centre, radius):
        self.centre= centre
        self.radius = radius

    def ritter(points, start):
        p1 = start
        p2 = find_farthest_from(p1, points)
        p3 = find_farthest_from(p2, points)

        diameter = calculate_distance(p2, p3)
        x_c = (p2[0] + p3[0]) / 2
        y_c = (p2[1] + p3[1]) / 2

        self.radius = diameter / 2
        self.centre = (x_c, y_c)

def generate_points(low=-5, high=5):
    num_points = np.random.randint(25, 60)
    x_rand = np.random.uniform(low, high, num_points)
    y_rand = np.random.uniform(low, high, num_points)

    return x_rand, y_rand

def draw_circle_points(center, radius, xr, yr):
    fig, ax = plt.subplots()
    ax.set_xlim(left=center[0] - 2*radius, right=center[0] + 2*radius)
    ax.set_ylim(bottom=center[1] - 2*radius, top=center[1] + 2*radius)
    plt.scatter(center[0], center[1])
    plt.scatter(xr, yr)
    circle = plt.Circle(center, radius, fill=False)
    ax.add_artist(circle)
    plt.savefig('img/circle_{}_{}_{}.png'.format(int(center[0]), int(center[1]), int(radius)))

def calculate_distance(p1, p2):
    x12 = (p1[0] - p2[0])**2
    y12 = (p1[1] - p2[1])**2
    euclidean_distance = math.sqrt(x12 + y12)

    return euclidean_distance

def find_farthest_from(start, points):
    max_dist = 0
    for point in points:
        dist = calculate_distance(point, start)
        if dist > max_dist:
            farthest = point
            max_dist = dist
    return farthest

def check_points_covered(points, circle):
    r = circle['radius']
    center = circle['center'][0], circle['center'][1]

    for point in points:
        dist_center = calculate_distance(center, point)
        if dist_center > r:
            return dist_center
    return None

def find_smallest_circle(points):
    for point in points:
        circle = ritter(points, point)
        while check_points_covered(points, circle) is not None:
            outlier_distance = check_points_covered(points, circle)
            circle['radius'] += outlier_distance / 2
            circle['center'][0] += outlier_distance / 2
            circle['center'][1] += outlier_distance / 2
        return circle

if __name__ == '__main__':

    for i in range(10):
        xs, ys = generate_points(60)
        points = list(zip(xs, ys))
        circle = find_smallest_circle(points)
        center = circle['center']
        radius = circle['radius']
        draw_circle_points(center, radius, xs, ys)
