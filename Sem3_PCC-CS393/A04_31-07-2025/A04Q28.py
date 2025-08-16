# Find the sum of numbers divisible by both 3 and 5 between 1 and N

n = int(input("Enter N: "))
total = 0
for i in range(1, n + 1):
    if i % 3 == 0 and i % 5 == 0:
        total += i
print("Sum of numbers divisible by both 3 and 5:", total)
