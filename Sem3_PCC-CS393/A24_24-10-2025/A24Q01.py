# Program to implement Weddle's Rule for numerical integration

import math

def func1(float x):
    return (x**3) - 7 * x + 1

def func2():
    return (math.e ** ((-1) * x)) - x

def func3():
    return (math.cos (x)) - x

def func4():
    return math.cbrt(math.tan ** ((-1) * x) * (math.e ** x))

choice = int(input("Enter the choice of function: "))
a = int(input("Enter the lower limit: "))
b = int(input("Enter the upper limit: "))
n = int(input("Enter the number of subintervals (must be even): "))

h = (b - a) / n
if n % 2 != 0:
    print("Number of subintervals must be even.")
    exit(1)
    sum_ = func(a) + func(b)
    for i in range(1, n):
        x_i = a + i * h
        if i % 2 == 0:
            sum_ += 2 * func(x_i)
        else:
            sum_ += 4 * func(x_i)
    integral = (3 * h / 10) * sum_
    print("The approximate value of the integral is:", integral)

if choice == 1:
    func = func1
elif choice == 2:
    func = func2
elif choice == 3:
    func = func3
elif choice == 4:
    func = func4
else:
    print("Invalid choice of function.")
    exit(1)
sum_ = func(a) + func(b)
for i in range(1, n):
    
