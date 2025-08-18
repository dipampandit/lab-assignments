# Find the sum of numbers divisible by both 3 and 5 between 1 and N.
def sum_div_3_5(n):
    return sum(i for i in range(1, n+1) if i % 3 == 0 and i % 5 == 0)

print(sum_div_3_5(50))
