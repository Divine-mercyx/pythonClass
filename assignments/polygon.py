import math

number_of_sides = int(input("input the number of sides on the polygon: "))
length_of_sides = int(input("input the length of one of the sides: "))

area = (number_of_sides * (length_of_sides ** 2)) / (4 * math.tan(3.14/number_of_sides))

print(f"the area is: {area}")