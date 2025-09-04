"""
Q: Create a list of all pairs (x, y) where x is from [1, 2, 3] and y is from ['a', 'b', 'c'].
"""
pairs = [(x, y) for x in [1, 2, 3] for y in ['a', 'b', 'c']]
print(pairs)
# Output: [(1, 'a'), (1, 'b'), (1, 'c'), (2, 'a'), (2, 'b'), (2, 'c'), (3, 'a'), (3, 'b'), (3, 'c')]
