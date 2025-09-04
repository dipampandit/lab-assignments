"""
Q: Flatten a 2D list (matrix) into a 1D list using list comprehension.
"""
matrix = [[1, 2], [3, 4], [5, 6]]
flat = [x for row in matrix for x in row]
print(flat)
# Output: [1, 2, 3, 4, 5, 6]