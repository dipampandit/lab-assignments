"""
Q: Implement max() without using Python's built-in max.
"""

def maximum(lst):
    if not lst:
        raise ValueError("max() arg is an empty sequence")
    max_val = lst[0]
    for item in lst[1:]:
        if item > max_val:
            max_val = item
    return max_val
