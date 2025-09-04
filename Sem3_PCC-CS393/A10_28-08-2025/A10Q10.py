"""
Q: Implement reverse() without using Python's built-in reverse.
"""

def reverse(lst):
    new_list = []
    for i in range(len(lst) - 1, -1, -1):
        new_list += [lst[i]]
    return new_list
