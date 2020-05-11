import matplotlib.pyplot as plt
from classes import Point, Circle
from points import all_points

def ritter_initial_ball(points: list) -> Circle:
    """
        Implements steps 1-4 of the Ritter's bounding sphere algorithm

        Parameters
        ----------
        points : list of <Point>
            array of points for which to calculate the smallest circle

        Returns
        ----------
        Circle
            initial ball with its centre at the midpoint of p2 and p3,
            the radius as half of the distance between p2 and p3    
    """
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
    """
        Implements steps 5-6 of the Ritter's bounding sphere algorithm

        Parameters
        ----------
        points : list of <Point>
            array of points for which to calculate the smallest circle
        
        Returns
        ----------
        Circle
            the smallest bounding circle for the given array of points
    """
    bounding_circle = ritter_initial_ball(points)
    for point in points:
        d = point.calculate_distance_to(bounding_circle.centre)
        alpha = 8
        while  d > bounding_circle.radius:
            bounding_circle.radius += d / alpha
            bounding_circle.centre += point / alpha
            alpha *= 2
    return bounding_circle

def draw_circle_points(c: Circle, points: list):
    """
        Draws given points, the calculated bounding circle and its centre

        Parameters
        ----------
        c : Circle
            calculated bounding circle defined by center and radius
        points : list of <Point>
            array of points for which to calculate the smallest circle

        Returns
        ----------
        nothing
    """
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
        
        
