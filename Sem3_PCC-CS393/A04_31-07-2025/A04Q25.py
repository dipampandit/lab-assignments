# Find the product of digits of a given number

num = int(input("Enter a number: "))
product = 1

while num > 0:
    product *= num % 10
    num //= 10

print("Product of digits:", product)
