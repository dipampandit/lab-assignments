m = int(input("Enter first integer: "))
n = int(input("Enter second integer: "))

# Using conditional operator
print("m is greater" if m > n else ("n is greater" if n > m else "Both are equal"))

# Using logical operators
if m == n:
    print("Both are equal")
else:
    print("They are not equal")
