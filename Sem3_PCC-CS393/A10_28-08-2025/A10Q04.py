"""
Q: Implement remove(x) without using Python's built-in remove.
"""

def remove(lst, x):
    new_list = []
    removed = False
    for item in lst:
        if item == x and not removed:
            removed = True
            continue
        new_list += [item]
    if not removed:
        raise ValueError("Value not found in list")
    return new_list
