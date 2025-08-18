# Find the Least Common Multiple (LCM) of two given numbers.
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a*b) // gcd(a, b)

print(lcm(12, 18))
