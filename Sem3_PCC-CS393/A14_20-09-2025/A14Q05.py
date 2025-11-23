# Copy an array to a new List without using built-in functions.

arr = []
n = int(input("Enter number of elements: "))
for i in range(n):
    val = int(input(f"Enter element {i+1}: "))
    arr += [val]

copy = []
for x in arr:
    copy += [x]

print("Copied list:", copy)
