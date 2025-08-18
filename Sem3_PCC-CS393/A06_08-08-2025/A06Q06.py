# Prime numbers in a range using *args (each arg = range end, starts from 2)
def primes_in_range(*args):
    result = []
    for n in args:
        primes = []
        for i in range(2, n+1):
            for j in range(2, int(i**0.5) + 1):
                if i % j == 0:
                    break
            else:
                primes.append(i)
        result.append(primes)
    return result

print(primes_in_range(10, 20))
