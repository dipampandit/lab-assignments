# Sum of digits using *args
def sum_of_digits(*args):
    return [sum(int(d) for d in str(num)) for num in args]

print(sum_of_digits(123, 456, 789))
