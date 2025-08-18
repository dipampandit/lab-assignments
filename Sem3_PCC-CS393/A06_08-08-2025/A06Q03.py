# Factorial of a number using *args
def factorial(*args):
    results = []
    for n in args:
        fact = 1
        for i in range(1, n+1):
            fact *= i
        results.append(fact)
    return results

print(factorial(5, 6))
