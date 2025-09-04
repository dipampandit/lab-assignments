"""
Q: Generate the transpose of a matrix using list comprehension.
"""
matrix = [[1, 2, 3], [4, 5, 6]]
transpose = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(transpose)
# Output: [[1, 4], [2, 5], [3, 6]]
