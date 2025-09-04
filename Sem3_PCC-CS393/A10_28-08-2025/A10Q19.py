"""
Q: Implement enumerate() without using Python's built-in enumerate.
"""

def enumerate_custom(iterable, start=0):
    result = []
    index = start
    for item in iterable:
        result += [(index, item)]
        index += 1
    return result
