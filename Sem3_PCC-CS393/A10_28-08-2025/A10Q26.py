"""
Q: Implement the '*' operator for lists/strings without using Python's built-in '*'.
"""

def repeat(seq, n):
    result = []
    for _ in range(n):
        for item in seq:
            result += [item]
    return result
