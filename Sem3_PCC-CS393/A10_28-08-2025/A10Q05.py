"""
Q: Implement pop([i]) without using Python's built-in pop.
"""

def pop(lst, i=None):
    if not lst:
        raise IndexError("pop from empty list")
    if i is None:
        i = len(lst) - 1
    if i < 0 or i >= len(lst):
        raise IndexError("pop index out of range")
    popped = lst[i]
    new_list = [lst[j] for j in range(len(lst)) if j != i]
    return popped, new_list
