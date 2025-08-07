# Check whether a given number is an Armstrong number or not.

num = int(input("Enter a number: "))
n = num
order = len(str(num))
sum = 0
while n > 0:
    digit = n % 10
    sum += digit ** order
    n //= 10
if num == sum:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
