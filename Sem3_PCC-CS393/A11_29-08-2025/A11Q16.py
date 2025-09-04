"""
Q: Create a multiplication table (1 to 10) as a list of lists using nested list comprehension.
"""
table = [[i * j for j in range(1, 11)] for i in range(1, 11)]
print(table)
