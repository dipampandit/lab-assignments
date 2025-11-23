# Replace any element via user-defined element in a List without using built-in functions.

arr = []
n = int(input("Enter number of elements: "))
for i in range(n):
    val = int(input(f"Enter element {i+1}: "))
    arr += [val]

pos = int(input("Enter position to replace: "))
val = int(input("Enter new value: "))

for i in range(n):
    if i == pos:
        arr[i] = val

print("List after replacement:", arr)
