# Find the sum of all elements in an integer List without using built-in functions.

arr = []
n = int(input("Enter number of elements: "))
for i in range(n):
    val = int(input(f"Enter element {i+1}: "))
    arr += [val]

total = 0
for x in arr:
    total += x

print("Sum of elements:", total)
