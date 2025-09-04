"""
Q: Implement del functionality without using Python's built-in del.
"""

def delete(lst, index):
    if index < 0 or index >= len(lst):
        raise IndexError("list index out of range")
    return [lst[i] for i in range(len(lst)) if i != index]
