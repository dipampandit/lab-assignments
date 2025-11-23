# Calculate the sum of even numbers in a list

def sum_even(lst):
    if not lst:
        return 0
    return (lst[0] if lst[0] % 2 == 0 else 0) + sum_even(lst[1:])

print(sum_even([1, 2, 3, 4, 5, 6]))
