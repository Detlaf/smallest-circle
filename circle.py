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

class Point():
    def __init__(self, coordinates):
        self.x = coordinates[0]
        self.y = coordinates[1]

    def __repr__(self):
        return ("({:.2f}, {:.2f})".format(self.x, self.y))

    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y

        return Point((new_x, new_y))

    def calculate_distance_to(self, p):
        x12 = (self.x - p.x)**2
        y12 = (self.y - p.y)**2
        euclidean_distance = math.sqrt(x12 + y12)

        return euclidean_distance

    def find_farthest_from(self, points):
        p = max(points, key=lambda p: self.calculate_distance_to(p))

        return p

class Circle():
    def __init__(self, centre: Point, radius: float):
        self.centre = centre
        self.radius = radius

def ritter_initial_ball(points: list) -> Circle:
    p1 = points[0]
    p2 = p1.find_farthest_from(points)
    p3 = p2.find_farthest_from(points)

    diameter = p2.calculate_distance_to(p3)
    x_c = (p2.x + p3.x) / 2
    y_c = (p2.y + p3.y) / 2
    centre = Point((x_c, y_c))

    c = Circle(centre, diameter / 2)

    return c

def generate_points(low=-5, high=5):
    num_points = np.random.randint(25, 60)
    x_rand = np.random.uniform(low, high, num_points)
    y_rand = np.random.uniform(low, high, num_points)

    return x_rand, y_rand

def draw_circle_points(c: Circle, xr, yr):
    fig, ax = plt.subplots()
    ax.set_xlim(left=c.centre.x - 2*c.radius, right=c.centre.x + 2*c.radius)
    ax.set_ylim(bottom=c.centre.y - 2*c.radius, top=c.centre.y + 2*c.radius)
    plt.scatter(c.centre.x, c.centre.y)
    plt.scatter(xr, yr)
    circle = plt.Circle((c.centre.x, c.centre.y), c.radius, fill=False)
    ax.add_artist(circle)
    plt.show()

def find_smallest_circle(points: list) -> Circle:
    bounding_circle = ritter_initial_ball(points)
    for point in points:
        d = point.calculate_distance_to(bounding_circle.centre)
        if  d > bounding_circle.radius:
            bounding_circle.radius += d / 2
            bounding_circle.centre += point
    return bounding_circle

if __name__ == '__main__':

    xs, ys = generate_points()
    points = [Point(p) for p in list(zip(xs, ys))]
    c = find_smallest_circle(points)
    draw_circle_points(c, xs, ys)
        
        
