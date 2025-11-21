# 1. Write a Python program to find the square root of a number using math.sqrt().
import math
print(math.sqrt(49))

# 2. How can you calculate 7 raised to the power 4 using math.pow()?
import math
print(math.pow(7, 4))

# 3. Write a program to compute the exponential value of 3 using math.exp().
import math
print(math.exp(3))

# 4. How do you find the natural logarithm of 20 using Python?
import math
print(math.log(20))

# 5. Write a program to find the base-10 logarithm of 1000.
import math
print(math.log10(1000))

# 6. How can you round a number 4.2 up to the nearest integer using math.ceil()?
import math
print(math.ceil(4.2))

# 7. Write a program to round down the value 9.8 using math.floor().
import math
print(math.floor(9.8))

# 8. How can you get the absolute value of -45.9 using math.fabs()?
import math
print(math.fabs(-45.9))

# 9. Write a program to compute the factorial of 7 using Python’s math module.
import math
print(math.factorial(7))

# 10. Find the greatest common divisor of 24 and 36 using math.gcd().
import math
print(math.gcd(24, 36))

# 11. Write a Python program to find the sine of 45 degrees.
import math
print(math.sin(math.radians(45)))

# 12. How do you calculate the cosine of π/4 radians?
import math
print(math.cos(math.pi / 4))

# 13. Write a program to compute the tangent of 60 degrees.
import math
print(math.tan(math.radians(60)))

# 14. Find the inverse sine of 0.5 using math.asin().
import math
print(math.asin(0.5))

# 15. Calculate the inverse cosine of 0 using math.acos().
import math
print(math.acos(0))

# 16. Find the inverse tangent of 1 using math.atan().
import math
print(math.atan(1))

# 17. Use math.atan2() to find the angle between points (3, 4).
import math
print(math.atan2(4, 3))

# 18. Write a program to convert radians π to degrees.
import math
print(math.degrees(math.pi))

# 19. Convert 180 degrees to radians using math.radians().
import math
print(math.radians(180))

# 20. Find the hypotenuse of a right triangle with sides 8 and 15 using math.hypot().
import math
print(math.hypot(8, 15))

# 21. Write a Python program to print the value of π using math.pi.
import math
print(math.pi)

# 22. Display the value of Euler’s number using math.e.
import math
print(math.e)

# 23. Print the value of tau (2π) using math.tau.
import math
print(math.tau)

# 24. Check if a number equals infinity using math.inf.
import math
x = math.inf
print(x == math.inf)

# 25. How can you represent a “Not a Number” value in Python?
import math
print(math.nan)

# 26. Round the number 12.5678 to two decimal places.
print(round(12.5678, 2))

# 27. Write a program to find the absolute value of -99.
print(abs(-99))

# 28. Truncate the decimal part of 15.789 using math.trunc().
import math
print(math.trunc(15.789))

# 29. Split the number 7.89 into fractional and integer parts using math.modf().
print(math.modf(7.89))

# 30. Find the IEEE remainder of 23 divided by 5.
print(math.remainder(23, 5))

# 31. Use divmod() to find the quotient and remainder when dividing 25 by 4.
print(divmod(25, 4))

# 32. Write a program to sum all elements in a list [5, 10, 15].
print(sum([5, 10, 15]))

# 33. Find the maximum of the numbers 3, 9, and 7.
print(max(3, 9, 7))

# 34. Find the minimum of the numbers 6, 4, and 2.
print(min(6, 4, 2))

# 35. Convert 25 into binary, octal, and hexadecimal.
print(bin(25), oct(25), hex(25))

# 36. Write a program to find e³ using math.exp().
print(math.exp(3))

# 37. Compute e² - 1 using math.expm1().
print(math.expm1(2))

# 38. Calculate the logarithm of 1000 with base 10.
print(math.log10(1000))

# 39. Find the logarithm of 16 with base 2.
print(math.log2(16))

# 40. Compute log(1+x) where x = 5 using math.log1p().
print(math.log1p(5))

# 41. Write a program to calculate the log base 2 of 64.
print(math.log2(64))

# 42. Find the natural log of 50 using math.log().
print(math.log(50))

# 43. Compare the outputs of math.log10(100) and math.log10(100, 10).
print(math.log10(100), math.log(100, 10))

# 44. Use math.log2() to find how many times 2 must be multiplied to get 128.
print(math.log2(128))

# 45. Write a program to calculate both math.exp() and math.expm1() for x = 3.
print(math.exp(3), math.expm1(3))

# 46. Find the number of ways to choose 3 items from 5 using math.comb().
print(math.comb(5, 3))

# 47. Calculate the number of permutations of 5 objects taken 2 at a time.
print(math.perm(5, 2))

# 48. Write a program to find the factorial of 10.
print(math.factorial(10))

# 49. Find how many combinations are possible when selecting 4 out of 10 items.
print(math.comb(10, 4))

# 50. Write a program that prints all factorial values from 1 to 5.
for i in range(1, 6):
    print(math.factorial(i))

# 51. Check if 3.14 is finite using math.isfinite().
print(math.isfinite(3.14))

# 52. Find whether a number is infinite using math.isinf().
print(math.isinf(math.inf))

# 53. Verify if a value float('nan') is NaN using math.isnan().
print(math.isnan(float('nan')))

# 54. Copy the sign of -9 to 4 using math.copysign().
print(math.copysign(4, -9))

# 55. Find the next floating-point number after 1.0 toward 2.0 using math.nextafter().
print(math.nextafter(1.0, 2.0))

# 56. Split the floating number 32 into mantissa and exponent using math.frexp().
import math
print(math.frexp(32.0))

# 57. Combine mantissa 0.5 and exponent 6 using math.ldexp().
import math
print(math.ldexp(0.5, 6))

# 58. Write a program to check whether math.inf - math.inf results in NaN.
import math
x = math.inf - math.inf
print(math.isnan(x))

# 59. Find the next smaller floating-point value after 10.0 toward 0.0.
import math
print(math.nextafter(10.0, 0.0))

# 60. Use math.frexp() to display the internal representation of 100.
import math
print(math.frexp(100.0))

# 61. Write a program to compute the gamma function of 6.
import math
print(math.gamma(6))

# 62. Find the logarithm of the gamma function for 8.
import math
print(math.lgamma(8))

# 63. Compute the error function of x = 1.5 using math.erf().
import math
print(math.erf(1.5))

# 64. Find the complementary error function of x = 2.
import math
print(math.erfc(2))

# 65. Compare the results of math.gamma(6) and math.factorial(5).
import math
print(math.gamma(6), math.factorial(5))

# 66. Write a program that prints gamma values from 1 to 5.
import math
for i in range(1, 6):
    print(math.gamma(i))

# 67. Calculate math.lgamma(10).
import math
print(math.lgamma(10))

# 68. Compute math.erf(0) and math.erf(1).
import math
print(math.erf(0), math.erf(1))

# 69. Find the value of math.erfc(0) and math.erfc(1).
import math
print(math.erfc(0), math.erfc(1))

# 70. Write a Python program to demonstrate the relation between erf() and erfc().
import math
x = 0.7
print(1 - math.erf(x), math.erfc(x))

# 71. Generate a random float between 0 and 1.
import random
print(random.random())

# 72. Generate a random integer between 10 and 50.
import random
print(random.randint(10, 50))

# 73. Select a random element from a list [2, 4, 6, 8].
import random
print(random.choice([2, 4, 6, 8]))

# 74. Generate a random float between 100 and 200.
import random
print(random.uniform(100, 200))

# 75. Simulate rolling a dice using random.randint(1, 6).
import random
print(random.randint(1, 6))

# 76. Pick a random name from a list of 5 names.
import random
names = ["Asha", "Bala", "Chirag", "Diya", "Eshan"]
print(random.choice(names))

# 77. Generate 10 random numbers between 0 and 1 using a loop.
import random
for _ in range(10):
    print(random.random())

# 78. Write a program to simulate a coin toss using random choice.
import random
print(random.choice(["Heads", "Tails"]))

# 79. Shuffle a list [1,2,3,4,5] randomly.
import random
lst = [1, 2, 3, 4, 5]
random.shuffle(lst)
print(lst)

# 80. Generate a list of 5 random integers between 1 and 100.
import random
print([random.randint(1, 100) for _ in range(5)])

# 81. Find the mean of numbers [10, 20, 30, 40].
import statistics
print(statistics.mean([10, 20, 30, 40]))

# 82. Calculate the median of [7, 8, 9, 10, 11].
import statistics
print(statistics.median([7, 8, 9, 10, 11]))

# 83. Find the mode of [2, 3, 3, 4, 5].
import statistics
print(statistics.mode([2, 3, 3, 4, 5]))

# 84. Compute the standard deviation of [5, 10, 15].
import statistics
print(statistics.stdev([5, 10, 15]))

# 85. Calculate the variance of [1, 2, 3, 4, 5].
import statistics
print(statistics.variance([1, 2, 3, 4, 5]))

# 86. Write a program to find mean, median, and mode together for a list.
import statistics
data = [1, 2, 2, 3, 4]
print(statistics.mean(data), statistics.median(data), statistics.mode(data))

# 87. Compare statistics.mean() and sum()/len() for a dataset.
import statistics
data = [1, 2, 3, 4]
print(statistics.mean(data), sum(data) / len(data))

# 88. Find the standard deviation of 100 random integers.
import random, statistics
nums = [random.randint(1, 100) for _ in range(100)]
print(statistics.stdev(nums))

# 89. Use statistics.median() on an even-length dataset.
import statistics
print(statistics.median([1, 2, 3, 4]))

# 90. Write a program to calculate variance and standard deviation manually and using the module.
import math, statistics
data = [2, 4, 4, 4, 5, 5, 7, 9]
mean = sum(data) / len(data)
sample_var = sum((x - mean) ** 2 for x in data) / (len(data) - 1)
sample_std = math.sqrt(sample_var)
print(sample_var, sample_std, statistics.variance(data), statistics.stdev(data))

# 91. Find 2 to the power 8 using pow().
print(pow(2, 8))

# 92. Write a program to find the sum of the first 10 natural numbers.
print(sum(range(1, 11)))

# 93. Find the maximum value in the tuple (4, 9, 2, 7).
print(max((4, 9, 2, 7)))

# 94. Find the minimum value in the set {12, 8, 15, 3}.
print(min({12, 8, 15, 3}))

# 95. Calculate the sum of even numbers from 1 to 20.
print(sum(i for i in range(1, 21) if i % 2 == 0))

# 96. Convert 255 to binary using bin().
print(bin(255))

# 97. Convert 64 to octal using oct().
print(oct(64))

# 98. Convert 255 to hexadecimal using hex().
print(hex(255))

# 99. Write a program that takes three numbers and prints the largest using max().
a, b, c = 3, 7, 5
print(max(a, b, c))

# 100. Write a Python program that calculates (x**y + y**x) using pow() and prints the result.
x, y = 3, 2
print(pow(x, y) + pow(y, x))
