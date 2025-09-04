"""
Q: Implement the '!=' operator without using Python's built-in '!='.
"""

def not_equal(a, b):
    if len(a) != len(b):
        return True
    for i in range(len(a)):
        if a[i] != b[i]:
            return True
    return False
