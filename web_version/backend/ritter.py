#!/usr/bin/env python3

from classes import Point, Circle
from points import all_points

def ritter_initial_ball() -> Circle:
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
    points = all_points()
    p1 = points[0]
    p2 = p1.find_farthest_from(points)
    p3 = p2.find_farthest_from(points)

    diameter = p2.calculate_distance_to(p3)
    x_c = (p2.x + p3.x) / 2
    y_c = (p2.y + p3.y) / 2
    centre = Point((x_c, y_c))

    c = Circle(centre, diameter / 2)

    return c.radius
        
        
