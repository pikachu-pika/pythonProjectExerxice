# MENSURATION (AREA,PERIMETER,DIAGONAL,VOLUME,TOTAL SURFACE AREA)
# All functions start with name of the plane figure or solid

import math


def rectangle():
    print("If You Need 'Area' Enter 1")
    print("If You Need 'Perimeter' Enter 2")
    print("If You Need 'Diagonal' Enter 3")
    choice = int(input("Enter Your Choice :->"))

    if choice == 1 or 2 or 3:
        length = float(input("Enter The Length :->"))
        breadth = float(input("Enter The Breadth :->"))

    if choice == 1:
        area = length * breadth
        return area

    elif choice == 2:
        perimeter = 2 * (length + breadth)
        return perimeter

    elif choice == 3:
        diagonal = math.sqrt(length * length + breadth * breadth)
        return diagonal.__round__(2)

    else:
        print("Wrong Choice Entered")


def square():
    print("If You Need 'Area' Enter 1")
    print("If You Need 'Perimeter' Enter 2")
    print("If You Need 'Diagonal' Enter 3")
    choice = int(input("Enter Your Choice :->"))

    if choice == 1 or 2 or 3:
        side = float(input("Enter The Side :->"))

    if choice == 1:
        area = side * side
        return area

    elif choice == 2:
        perimeter = 4 * side
        return perimeter

    elif choice == 3:
        diagonal = math.sqrt(2 * side * side)
        return diagonal.__round__(2)

    else:
        print("Wrong Choice Entered")


def circle():
    print("If You Need 'Area' Enter 1")
    print("If You Need 'Circumference' Enter 2")
    choice = int(input("Enter Your Choice :->"))

    if choice == 1 or 2:
        radius = float(input("Enter The Radius :->"))

    if choice == 1:
        area = math.pi * radius * radius
        return area.__round__(2)

    elif choice == 2:
        circumference = math.pi * 2 * radius
        return circumference

    else:
        print("Wrong Choice Entered")


def parallelogram_area():
    base = float(input("Enter The Base :->"))
    height = float(input("Enter The Height :->"))

    area = base * height
    return area


def rhombus():
    print("If You Need 'Area' Enter 1")
    print("If You Need 'Perimeter' Enter 2")
    choice = int(input("Enter Your Choice :->"))

    if choice == 1:
        diagonal1 = float(input("Enter The First Diagonal :->"))
        diagonal2 = float(input("Enter The Second Diagonal :->"))

        area = 1 / 2 * diagonal1 * diagonal2
        return area

    elif choice == 2:
        side = float(input("Enter The Side :->"))
        perimeter = 4 * side
        return perimeter

    else:
        print("Wrong Choice Entered")


def trapezium_area():
    side1 = float(input("Enter The First Parallel Side :->"))
    side2 = float(input("Enter The Second Parallel Side :->"))
    height = float(input("Enter The Distance Between Parallel Sides :->"))

    area = 1 / 2 * (side1 + side2) * height
    return area


def triangle_area():
    print("If Height And Base Are Given Enter 1")
    print("If Sides Of The Triangle Are Given Enter 2")
    print("If Triangle Is Equilateral Enter 3")
    print("If Triangle Is Isosceles Enter 4")
    choice = int(input("Enter Your Choice :->"))

    if choice == 1:
        base = float(input("Enter The Base :->"))
        height = float(input("Enter The Height :->"))

        area = 1 / 2 * base * height
        return area

    elif choice == 2:
        side1 = float(input("Enter The First Side :->"))
        side2 = float(input("Enter The Second Side :->"))
        side3 = float(input("Enter The Third Side :->"))

        s = (side1 + side2 + side3) / 2  # semi-perimeter
        area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))
        return area

    elif choice == 3:
        side = float(input("Enter The Side :->"))

        area = math.sqrt(3) / 4 * side * side
        return area.__round__(2)

    elif choice == 4:
        side = float(input("Enter The Length Of Each Equal Side :->"))
        base = float(input("Enter The Length Of Base :->"))

        area = 1 / 4 * base * math.sqrt(4 * side * side - base * base)
        return area

    else:
        print("Wrong Choice Entered")


def cuboid():
    print("If You Need 'Volume' Enter 1")
    print("If You Need 'Total Surface Area' Enter 2")
    print("If You Need 'Diagonal' Enter 3")
    choice = int(input("Enter Your Choice :->"))

    if choice == 1 or 2 or 3:
        length = float(input("Enter The Length :->"))
        width = float(input("Enter The Width :->"))
        height = float(input("Enter The Height :->"))

    if choice == 1:
        volume = length * width * height
        return volume

    elif choice == 2:
        area = 2 * (length * width + width * height + height * length)
        return area

    elif choice == 3:
        diagonal = math.sqrt(length * length + width * width + height * height)
        return diagonal.__round__(2)

    else:
        print("Wrong Choice Entered")


def cube():
    print("If You Need 'Volume' Enter 1")
    print("If You Need 'Total Surface Area' Enter 2")
    print("If You Need 'Diagonal' Enter 3")
    choice = int(input("Enter Your Choice :->"))

    if choice == 1 or 2 or 3:
        edge = float(input("Enter The Length Of Edge :->"))

    if choice == 1:
        volume = math.pow(edge, 3)
        return volume

    elif choice == 2:
        area = 6 * edge * edge
        return area

    elif choice == 3:
        diagonal = edge * math.sqrt(3)
        return diagonal.__round__(2)

    else:
        print("Wrong Choice Entered")


def sphere():
    print("If You Need 'Volume' Enter 1")
    print("If You Need 'Total Surface Area' Enter 2")
    choice = int(input("Enter Your Choice :->"))

    if choice == 1 or 2:
        radius = float(input("Enter The Radius :->"))

    if choice == 1:
        volume = 4 / 3 * math.pi * math.pow(radius, 3)
        return volume.__round__(2)

    elif choice == 2:
        area = 4 * math.pi * math.pow(radius, 2)
        return area.__round__(2)

    else:
        print("Wrong Choice Entered")


def cone():
    print("If You Need 'Volume' Enter 1")
    print("If You Need 'Total Surface Area' Enter 2")
    choice = int(input("Enter Your Choice :->"))

    if choice == 1 or 2:
        radius = float(input("Enter The Radius :->"))
        height = float(input("Enter The Height :->"))

    if choice == 1:
        volume = 1 / 3 * math.pi * math.pow(radius, 2) * height
        return volume.__round__(2)

    elif choice == 2:
        area = math.pi * radius * (radius + math.sqrt(height * height + radius * radius))
        return area.__round__(2)

    else:
        print("Wrong Choice Entered")


def cylinder():
    print("If You Need 'Volume' Enter 1")
    print("If You Need 'Total Surface Area' Enter 2")
    choice = int(input("Enter Your Choice :->"))

    if choice == 1 or 2:
        radius = float(input("Enter The Radius :->"))
        height = float(input("Enter The Height :->"))

    if choice == 1:
        volume = math.pi * math.pow(radius, 2) * height
        return volume.__round__(2)

    elif choice == 2:
        area = 2 * math.pi * radius * (radius + height)
        return area.__round__(2)

    else:
        print("Wrong Choice Entered")

