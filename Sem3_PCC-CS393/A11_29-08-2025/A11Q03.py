"""
Q: Generate a list of cubes of odd numbers between 1 and 20.
"""
cubes = [x**3 for x in range(1, 21) if x % 2 != 0]
print(cubes)
# Output: [1, 27, 125, 343, 729, 1331, 2197, 3375, 4913, 6859]