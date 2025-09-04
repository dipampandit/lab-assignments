"""
Q: Implement the '<=' operator for sequences without using Python's built-in '<='.
"""

def less_equal(a, b):
    n = min(len(a), len(b))
    for i in range(n):
        if a[i] < b[i]:
            return True
        elif a[i] > b[i]:
            return False
    return len(a) <= len(b)
