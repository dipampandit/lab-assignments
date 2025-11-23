# Calculate the sum of odd numbers in a list

def sum_odd(lst):
    if not lst:
        return 0
    return (lst[0] if lst[0] % 2 != 0 else 0) + sum_odd(lst[1:])

print(sum_odd([1, 2, 3, 4, 5, 6]))
