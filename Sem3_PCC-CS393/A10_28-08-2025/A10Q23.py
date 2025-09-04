"""
Q: Implement the 'in' operator without using Python's built-in 'in'.
"""

def contains(iterable, x):
    for item in iterable:
        if item == x:
            return True
    return False
