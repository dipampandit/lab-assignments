# Find the maximum element in a list
def max_in_list(lst):
    if len(lst) == 1:
        return lst[0]
    return max(lst[0], max_in_list(lst[1:]))

print(max_in_list([3, 7, 2, 9, 5]))
