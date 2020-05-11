import math

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
    def __init__(self, centre: Point, radius: float):
        self.centre = centre
        self.radius = radius