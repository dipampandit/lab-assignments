"""
Q: Implement sort(key=None, reverse=False) without using Python's built-in sort.
"""

def sort(lst, key=None, reverse=False):
    new_list = lst[:]
    n = len(new_list)
    for i in range(n):
        for j in range(0, n - i - 1):
            a = new_list[j]
            b = new_list[j + 1]
            if key:
                a = key(new_list[j])
                b = key(new_list[j + 1])
            if (not reverse and a > b) or (reverse and a < b):
                new_list[j], new_list[j + 1] = new_list[j + 1], new_list[j]
    return new_list
