# Check whether a number is a Strong number or not
# (Strong number = sum of factorial of digits = number)

num = int(input("Enter a number: "))
temp = num
total = 0

while num > 0:
    digit = num % 10
    fact = 1
    for i in range(1, digit + 1):
        fact *= i
    total += fact
    num //= 10

if total == temp:
    print("Strong number")
else:
    print("Not a Strong number")
