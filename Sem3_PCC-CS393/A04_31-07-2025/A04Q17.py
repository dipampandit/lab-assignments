# Find the sum of the first N natural numbers

n = int(input("Enter N: "))
total = 0
for i in range(1, n + 1):
    total += i
print("Sum of first", n, "natural numbers:", total)
