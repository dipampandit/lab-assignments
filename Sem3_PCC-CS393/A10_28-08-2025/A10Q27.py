"""
Q: Implement the '==' operator without using Python's built-in '=='.
"""

def equal(a, b):
    if len(a) != len(b):
        return False
    for i in range(len(a)):
        if a[i] != b[i]:
            return False
    return True
