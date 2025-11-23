# Find the sum of even numbers and the sum of odd numbers separately in an array.

arr = []
n = int(input("Enter number of elements: "))
for i in range(n):
    val = int(input(f"Enter element {i+1}: "))
    arr += [val]

even_sum = 0
odd_sum = 0
for x in arr:
    if x % 2 == 0:
        even_sum += x
    else:
        odd_sum += x

print("Sum of even numbers:", even_sum)
print("Sum of odd numbers:", odd_sum)
