import math
import numpy as np
import matplotlib.pyplot as plt

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
    plt.show()

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

def ritter(points, start):
    p1 = start
    p2 = find_farthest_from(p1, points)
    p3 = find_farthest_from(p2, points)

    diameter = calculate_distance(p2, p3)
    x_c = (p2[0] + p3[0]) / 2
    y_c = (p2[1] + p3[1]) / 2

    circle = {}
    circle['radius'] = diameter / 2
    circle['center'] = []
    circle['center'].append(x_c)
    circle['center'].append(y_c)

    return circle

def check_points_covered(points, circle):
    r = circle['radius']
    center = circle['center'][0], circle['center'][1]

    for point in points:
        dist_center = calculate_distance(center, point)
        if dist_center > r:
            return False
    return True

def find_smallest_circle(points):
    for point in points:
        circle = ritter(points, point)
        if check_points_covered(points, circle):
            return circle
    return None

if __name__ == '__main__':
    xs, ys = generate_points(60)
    points = list(zip(xs, ys))

    circle = find_smallest_circle(points)
    if circle is not None:
        center = circle['center']
        radius = circle['radius']
        draw_circle_points(center, radius, xs, ys)
    else:
        print("No circle found!")
