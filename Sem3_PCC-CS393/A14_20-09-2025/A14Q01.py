# Find the size of a List without using built-in functions.

arr = []
n = int(input("Enter number of elements: "))
for i in range(n):
    val = int(input(f"Enter element {i+1}: "))
    arr += [val]

count = 0
for _ in arr:
    count += 1

print("Size of the list:", count)
