"""
Q: Implement all() without using Python's built-in all.
"""

def all_true(iterable):
    for item in iterable:
        if not item:
            return False
    return True
