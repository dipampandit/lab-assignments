"""
Q: Implement list(iterable) without using Python's built-in list().
"""

def make_list(iterable):
    result = []
    for item in iterable:
        result += [item]
    return result
