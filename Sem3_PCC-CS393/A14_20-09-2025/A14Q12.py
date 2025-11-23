# Remove duplicates from a List without using built-in functions.

arr = []
n = int(input("Enter number of elements: "))
for i in range(n):
    val = int(input(f"Enter element {i+1}: "))
    arr += [val]

unique = []
for x in arr:
    found = False
    for y in unique:
        if x == y:
            found = True
            break
    if not found:
        unique += [x]

print("List after removing duplicates:", unique)
