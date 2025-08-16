# Find and display the reverse of a given number.

num = int(input("Enter a number: "))
rev = 0
temp = num

while temp != 0:
    rev = rev * 10 + temp % 10
    temp //= 10

print("Reversed number:", rev)
