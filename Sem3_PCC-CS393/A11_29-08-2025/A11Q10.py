"""
Q: Generate a list of tuples (number, square) for numbers from 1 to 10.
"""
pairs = [(x, x**2) for x in range(1, 11)]
print(pairs)
# Output: [(1, 1), (2, 4), (3, 9), (4, 16), (5, 25), (6, 36), (7, 49), (8, 64), (9, 81), (10, 100)]