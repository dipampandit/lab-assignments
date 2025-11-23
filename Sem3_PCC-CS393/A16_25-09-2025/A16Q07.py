# Find the greatest common divisor (gcd) of two numbers

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

print(gcd(48, 18))
