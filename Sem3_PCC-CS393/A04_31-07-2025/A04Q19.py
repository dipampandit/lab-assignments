# Find the sum of all odd numbers between 1 and N

n = int(input("Enter N: "))
total = 0
for i in range(1, n + 1, 2):
    total += i
print("Sum of odd numbers between 1 and", n, ":", total)
