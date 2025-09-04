"""
Q: Implement sum() without using Python's built-in sum.
"""

def summation(lst):
    total = 0
    for item in lst:
        total += item
    return total
