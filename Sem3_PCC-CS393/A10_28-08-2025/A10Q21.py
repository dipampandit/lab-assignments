"""
Q: Implement zip() without using Python's built-in zip.
"""

def zip_custom(*iterables):
    min_len = min([len(it) for it in iterables])
    result = []
    for i in range(min_len):
        group = []
        for it in iterables:
            group.append(it[i])
        result.append(tuple(group))
    return result
