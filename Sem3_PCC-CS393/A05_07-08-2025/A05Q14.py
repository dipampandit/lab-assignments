# Check whether a given number is a Harshad (Niven) number or not.
def is_harshad(n):
    return n % sum(int(d) for d in str(n)) == 0

print(is_harshad(18))
