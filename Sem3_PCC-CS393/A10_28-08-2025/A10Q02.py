"""
Q: Implement extend(iterable) without using Python's built-in extend.
"""

def extend(lst, iterable):
    for item in iterable:
        lst = lst + [item]
    return lst