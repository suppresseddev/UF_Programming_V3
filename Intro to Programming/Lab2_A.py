# Program A
# Program A will classify triangles based on their side lengths.
# An equilateral triangle has 3 equal sides
# An isosceles triangle has 2 equal sides
# A scalene triangle has no equal sides.

def classifyTri():
    #Ask for side lengths.
    side1 = float(input('Side length 1: '))
    side2 = float(input('Side length 2: '))
    side3 = float(input('Side length 3: '))
    #Check how many are the same:
    equalsides = 0
    if side1 == side2:
        equalsides = 2
        if side1 == side3:
            equalsides = 3
    if side2 == side3:
        equalsides = 2
        if side3 == side1:
            equalsides = 3
    if side3 == side1:
        equalsides = 2
        if side1 == side2:
            equalsides = 3
    #Interpret result:
    if equalsides == 3:
        print("This is an equilateral triangle!")
    elif equalsides == 2:
        print("This is an isosceles triangle!")
    elif equalsides == 0:
        print("This is a scalene triangle!")


classifyTri()