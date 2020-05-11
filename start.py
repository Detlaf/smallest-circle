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
import matplotlib.pyplot as plt
from classes import Point, Circle
from points import all_points

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

def find_smallest_circle(points: list) -> Circle:
    bounding_circle = ritter_initial_ball(points)
    for point in points:
        d = point.calculate_distance_to(bounding_circle.centre)
        if  d > bounding_circle.radius:
            bounding_circle.radius += d / 16
            bounding_circle.centre += point / 16
    return bounding_circle

def draw_circle_points(c: Circle, points: list):
    fig, ax = plt.subplots()
    ax.set_xlim(left=c.centre.x - 2*c.radius, right=c.centre.x + 2*c.radius)
    ax.set_ylim(bottom=c.centre.y - 2*c.radius, top=c.centre.y + 2*c.radius)
    plt.scatter(c.centre.x, c.centre.y, c='r')
    for point in points:
        plt.scatter(point.x, point.y, c='b')
    circle = plt.Circle((c.centre.x, c.centre.y), c.radius, fill=False)
    ax.add_artist(circle)
    plt.show()

if __name__ == '__main__':

    points = all_points()
    c = find_smallest_circle(points)
    draw_circle_points(c, points)
        
        
