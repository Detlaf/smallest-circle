import math

class Point():
    """
        A class used to represent point on 2D plane

        Attributes
        ----------
        x : float
            x-coordinate of the point
        y : float
            y-coordinate of the point

        Methods
        -------
        calculate_distance_to(p) -> float
            calculated euclidean distance from the given point to the point p
        find_farthest_from(points) -> Point 
            in the list of points finds a point which has the maximum distance from the current

        Overloaded operators
        --------

        __add__ (+) -> Point
            overloaded so that two points' coordinates could be added together
        __truediv__ (/) -> Point
            overloaded so that point's coordinates could be divided by some number
    """
    def __init__(self, coordinates):
        self.x = coordinates[0]
        self.y = coordinates[1]

    def __repr__(self):
        return ("({:.2f}, {:.2f})".format(self.x, self.y))

    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y

        return Point((new_x, new_y))

    def __truediv__(self, num):
        new_x = self.x / num
        new_y = self.y / num

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
    """
        A class used to represent circle on 2D plane

        Attributes
        ----------
        centre : Point
            (x, y) coordinates of the circle's centre
        radius : float
            circle's radius
    """
    def __init__(self, centre: Point, radius: float):
        self.centre = centre
        self.radius = radius