"""
Q: Implement the 'not in' operator without using Python's built-in 'not in'.
"""

def not_contains(iterable, x):
    for item in iterable:
        if item == x:
            return False
    return True
