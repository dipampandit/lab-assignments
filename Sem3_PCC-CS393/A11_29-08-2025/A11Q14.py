"""
Q: From a list of numbers, create a new list replacing negative numbers with 0.
"""
nums = [-3, 5, -7, 2, 0]
replaced = [x if x >= 0 else 0 for x in nums]
print(replaced)
# Output: [0, 5, 0, 2, 0]