# Check whether a given number is a Harshad (Niven) number or not
# (Harshad number = divisible by sum of its digits)

num = int(input("Enter a number: "))
temp = num
digit_sum = 0

while num > 0:
    digit_sum += num % 10
    num //= 10

if temp % digit_sum == 0:
    print("Harshad (Niven) number")
else:
    print("Not a Harshad number")
