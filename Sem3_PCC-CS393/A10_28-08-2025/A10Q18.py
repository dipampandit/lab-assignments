"""
Q: Implement any() without using Python's built-in any.
"""

def any_true(iterable):
    for item in iterable:
        if item:
            return True
    return False
