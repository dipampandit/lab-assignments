# Convert a given decimal number to its binary equivalent.

num = int(input("Enter a decimal number: "))
binary = ''
while num > 0:
    binary = str(num % 2) + binary
    num //= 2
print("Binary:", binary)
