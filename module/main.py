import mymodule as mm
from mymodule import area_of_circle as aoc
from Matematika.circle import*
from Matematika.square import perimeter_of_square

area1 = mm.area_of_square(6)
print(f"Area of square with side = 6 is {area1}")

area1 = mm.area_of_square(12)
print(f"Area of square with side = 12 is {area1}")

area1= mm.area_of_triangle(4,5)
print(f"Area of triangle with base = 4, height = 5 is {area1}")

area1 = mm.area_of_circle(7)
print(f"area of circle with radius = 7 is {area1}")