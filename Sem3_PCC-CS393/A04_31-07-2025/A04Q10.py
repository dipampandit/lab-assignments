# Find the sum of digits of a given number.

num = int(input("Enter a number: "))
total = 0
while num > 0:
    total += num % 10
    num //= 10
print("Sum of digits:", total)
