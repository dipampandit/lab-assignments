"""
Q: Implement the '+' operator for lists/strings without using Python's built-in '+'.
"""

def concat(a, b):
    result = []
    for item in a:
        result += [item]
    for item in b:
        result += [item]
    return result
