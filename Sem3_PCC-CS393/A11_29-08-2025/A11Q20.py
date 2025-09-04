"""
Q: Generate Pascal’s Triangle up to n rows using nested list comprehension.
"""
n = 5
pascal = [[1 if j == 0 or j == i else 0 for j in range(i + 1)] for i in range(n)]
pascal = [[1 if j == 0 or j == i else pascal[i-1][j-1] + pascal[i-1][j] for j in range(i + 1)] for i in range(n)]
print(pascal)
# Output: [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]