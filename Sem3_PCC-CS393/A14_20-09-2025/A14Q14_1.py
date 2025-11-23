"""
Q: Write a Python program to find the sum of the series:
   1 + 2^2 + 3^2 + 4^2 + ... up to n terms.
"""

n = int(input("Enter number of terms: "))
sum1 = 0
for i in range(1, n + 1):
    sum1 += i * i

print("Sum of the series:", sum1)
