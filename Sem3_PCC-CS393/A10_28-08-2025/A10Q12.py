"""
Q: Implement len() without using Python's built-in len.
"""

def length(lst):
    count = 0
    for _ in lst:
        count += 1
    return count
