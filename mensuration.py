"""
MENSURATION (AREA,PERIMETER,DIAGONAL,VOLUME,TOTAL SURFACE AREA OF PLANE FIGURE OR SOLID) \n
All functions start with name of the plane figure or solid
"""

import math


def rectangle_area(length, breadth):
    return length * breadth


def rectangle_perimeter(length, breadth):
    return 2 * (length + breadth)


def rectangle_diagonal(length, breadth):
    diagonal = math.sqrt(length * length + breadth * breadth)
    return diagonal.__round__(2)


def square_area(side):
    return side * side


def square_perimeter(side):
    return 4 * side


def square_diagonal(side):
    diagonal = math.sqrt(2 * side * side)
    return diagonal.__round__(2)


def circle_area(radius):
    area = math.pi * radius * radius
    return area.__round__(2)


def circle_circumference(radius):
    circumference = math.pi * 2 * radius
    return circumference.__round__(2)


def parallelogram_area(base, height):
    return base * height


def rhombus_area(diagonal1, diagonal2):
    area = 1 / 2 * diagonal1 * diagonal2
    return area


def rhombus_perimeter(side):
    return 4 * side


def trapezium_area(side1, side2, height):
    """
    side1: The First Parallel Side \n
    side2: The Second Parallel Side \n
    height:The Distance Between Parallel Sides
    """

    area = 1 / 2 * (side1 + side2) * height
    return area


def triangle_area_hb(base, height):
    """ Using Height And Base"""
    area = 1 / 2 * base * height
    return area


def triangle_area_sides(side1, side2, side3):
    """
    Using Sides Of The Triangle \n
    side1 :The First Side \n
    side2 :The Second Side \n
    side3 :The Third Side \n
    """

    s = (side1 + side2 + side3) / 2  # semi-perimeter
    area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))
    return area


def triangle_area_equilateral(side):
    area = math.sqrt(3) / 4 * side * side
    return area.__round__(2)


def triangle_area_isosceles(side, base):
    """
    side :The Length Of Equal Side \n
    base :The Length Of Base
    """
    area = 1 / 4 * base * math.sqrt(4 * side * side - base * base)
    return area


def cuboid_volume(length, width, height):
    return length * width * height


def cuboid_ts_area(length, width, height):
    ts_area = 2 * (length * width + width * height + height * length)
    return ts_area


def cuboid_diagonal(length, width, height):
    diagonal = math.sqrt(length * length + width * width + height * height)
    return diagonal.__round__(2)


def cube_volume(edge):
    volume = math.pow(edge, 3)
    return volume


def cube_ts_area(edge):
    ts_area = 6 * edge * edge
    return ts_area


def cube_diagonal(edge):
    diagonal = edge * math.sqrt(3)
    return diagonal.__round__(2)


def sphere_volume(radius):
    volume = 4 / 3 * math.pi * math.pow(radius, 3)
    return volume.__round__(2)


def sphere_ts_area(radius):
    ts_area = 4 * math.pi * math.pow(radius, 2)
    return ts_area.__round__(2)


def cone_volume(radius, height):
    volume = 1 / 3 * math.pi * math.pow(radius, 2) * height
    return volume.__round__(2)


def cone_ts_area(radius, height):
    ts_area = math.pi * radius * (radius + math.sqrt(height * height + radius * radius))
    return ts_area.__round__(2)


def cylinder_volume(radius, height):
    volume = math.pi * math.pow(radius, 2) * height
    return volume.__round__(2)


def cylinder_ts_area(radius, height):
    ts_area = 2 * math.pi * radius * (radius + height)
    return ts_area.__round__(2)
