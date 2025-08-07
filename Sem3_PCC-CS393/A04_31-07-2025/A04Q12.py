# Display Fibonacci numbers up to a given number of terms

n = int(input("Enter number of terms: "))
a, b = 0, 1
count = 0

while count < n:
    print(a, end=" ")
    c = a + b
    a = b
    b = c
    count += 1
