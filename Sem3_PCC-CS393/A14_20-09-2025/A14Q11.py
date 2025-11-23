# Reverse a List without using built-in functions.

arr = []
n = int(input("Enter number of elements: "))
for i in range(n):
    val = int(input(f"Enter element {i+1}: "))
    arr += [val]

rev = []
for i in range(n-1, -1, -1):
    rev += [arr[i]]

print("Reversed list:", rev)
