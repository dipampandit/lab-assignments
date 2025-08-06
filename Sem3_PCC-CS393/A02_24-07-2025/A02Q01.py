import math

# Rectangle
length = 5
width = 3
rect_area = length * width
rect_perimeter = 2 * (length + width)
print(f"Rectangle, Area: {rect_area}, Perimeter: {rect_perimeter}")

# Triangle (using base & height for area, perimeter with 3 sides)
base = 4
height = 6
side1, side2, side3 = 4, 5, 6
tri_area = 0.5 * base * height
tri_perimeter = side1 + side2 + side3
print(f"Triangle, Area: {tri_area}, Perimeter: {tri_perimeter}")

# Circle
radius = 7
circle_area = math.pi * radius**2
circle_perimeter = 2 * math.pi * radius
print(f"Circle, Area: {circle_area:.2f}, Perimeter: {circle_perimeter:.2f}")

# Rhombus (using diagonals d1, d2)
d1 = 8
d2 = 6
side = 5
rhombus_area = 0.5 * d1 * d2
rhombus_perimeter = 4 * side
print(f"Rhombus, Area: {rhombus_area}, Perimeter: {rhombus_perimeter}")
