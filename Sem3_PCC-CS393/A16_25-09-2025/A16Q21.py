# Compute the nth triangular number

def triangular_number(n):
    if n == 0:
        return 0
    return n + triangular_number(n-1)

print(triangular_number(5))
