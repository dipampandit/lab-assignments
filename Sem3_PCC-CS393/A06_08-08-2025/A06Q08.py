# Power of a number (base, exponent) using *args
def power(*args):
    results = []
    for i in range(0, len(args), 2):
        base, exp = args[i], args[i+1]
        results.append(base ** exp)
    return results

print(power(2, 5, 3, 4))
