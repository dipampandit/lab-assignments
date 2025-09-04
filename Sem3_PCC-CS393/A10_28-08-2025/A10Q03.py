"""
Q: Implement insert(i, x) without using Python's built-in insert.
"""

def insert(lst, i, x):
    return lst[:i] + [x] + lst[i:]
