# Delete element in any position from a List without using built-in functions.

arr = []
n = int(input("Enter number of elements: "))
for i in range(n):
    val = int(input(f"Enter element {i+1}: "))
    arr += [val]

pos = int(input("Enter position to delete: "))

new_arr = []
for i in range(n):
    if i != pos:
        new_arr += [arr[i]]

print("List after deletion:", new_arr)
