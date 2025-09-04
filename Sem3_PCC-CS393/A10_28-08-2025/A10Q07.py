"""
Q: Implement index(x[, start[, end]]) without using Python's built-in index.
"""

def index(lst, x, start=0, end=None):
    if end is None:
        end = len(lst)
    for i in range(start, end):
        if lst[i] == x:
            return i
    raise ValueError("Value not found in list")
