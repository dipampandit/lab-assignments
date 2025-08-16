# Find the Least Common Multiple (LCM) of two given numbers.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
lcm = max(a, b)

while True:
    if lcm % a == 0 and lcm % b == 0:
        print("LCM is:", lcm)
        break
    lcm += 1
