"""
Q: Implement count(x) without using Python's built-in count.
"""

def count(lst, x):
    cnt = 0
    for item in lst:
        if item == x:
            cnt += 1
    return cnt
