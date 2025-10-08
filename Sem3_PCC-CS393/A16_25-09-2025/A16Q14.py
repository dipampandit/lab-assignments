# Find the minimum element in a list
def min_in_list(lst):
    if len(lst) == 1:
        return lst[0]
    return min(lst[0], min_in_list(lst[1:]))

print(min_in_list([3, 7, 2, 9, 5]))
