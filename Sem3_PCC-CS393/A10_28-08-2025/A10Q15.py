"""
Q: Implement min() without using Python's built-in min.
"""

def minimum(lst):
    if not lst:
        raise ValueError("min() arg is an empty sequence")
    min_val = lst[0]
    for item in lst[1:]:
        if item < min_val:
            min_val = item
    return min_val
