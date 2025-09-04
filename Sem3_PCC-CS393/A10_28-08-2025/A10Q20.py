"""
Q: Implement sorted() without using Python's built-in sorted.
"""

def sorted_custom(iterable, reverse=False):
    lst = [x for x in iterable]
    n = len(lst)
    for i in range(n):
        for j in range(0, n - i - 1):
            if (not reverse and lst[j] > lst[j + 1]) or (reverse and lst[j] < lst[j + 1]):
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst
