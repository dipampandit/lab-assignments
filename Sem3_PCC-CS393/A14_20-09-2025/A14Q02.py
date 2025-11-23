# Insert user-defined element in any position in a List without using built-in functions.

arr = []
n = int(input("Enter number of elements: "))
for i in range(n):
    val = int(input(f"Enter element {i+1}: "))
    arr += [val]

pos = int(input("Enter position to insert: "))
val = int(input("Enter value to insert: "))

new_arr = []
for i in range(pos):
    new_arr += [arr[i]]
new_arr += [val]
for i in range(pos, n):
    new_arr += [arr[i]]

print("List after insertion:", new_arr)
