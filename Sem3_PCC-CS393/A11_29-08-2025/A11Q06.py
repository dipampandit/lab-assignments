"""
Q: Generate a list of prime numbers between 1 and 100 using list comprehension.
"""
primes = [x for x in range(2, 101) if all(x % d != 0 for d in range(2, int(x**0.5) + 1))]
print(primes)
# Output: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]