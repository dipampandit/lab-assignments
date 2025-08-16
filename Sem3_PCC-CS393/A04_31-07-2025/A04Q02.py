# Find and display all Armstrong numbers within a given range.

lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))

for num in range(lower, upper + 1):
    order = len(str(num))
    total = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        total += digit ** order
        temp //= 10
    if num == total:
        print(num)
