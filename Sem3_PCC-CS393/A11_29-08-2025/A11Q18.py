"""
Q: Flatten a 3D list into a 1D list using list comprehension.
"""
arr = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
flat = [x for block in arr for row in block for x in row]
print(flat)
# Output: [1, 2, 3, 4, 5, 6, 7, 8]