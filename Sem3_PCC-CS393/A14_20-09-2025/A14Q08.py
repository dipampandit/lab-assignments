# Find the second largest element in a List without using built-in functions.

arr = []
n = int(input("Enter number of elements: "))
for i in range(n):
    val = int(input(f"Enter element {i+1}: "))
    arr += [val]

largest = arr[0]
second = arr[0]

for x in arr:
    if x > largest:
        second = largest
        largest = x
    elif x > second and x != largest:
        second = x

print("Second largest element:", second)
