# Calculate the power of a number (base^exponent) without using library functions

base = int(input("Enter base: "))
exp = int(input("Enter exponent: "))

result = 1
for _ in range(exp):
    result *= base

print("Result:", result)
