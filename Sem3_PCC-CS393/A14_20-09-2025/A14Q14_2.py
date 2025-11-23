"""
Q: Write a Python program to find the sum of the series:
   1 + 1/2 + 1/4 + 1/8 + ... up to n terms.
"""

n = int(input("Enter number of terms: "))
sum2 = 0.0
term = 1.0
for i in range(n):
    sum2 += term
    term /= 2

print("Sum of the series:", sum2)
