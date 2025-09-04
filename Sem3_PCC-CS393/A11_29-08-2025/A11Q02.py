"""
Q: Create a list of even numbers between 1 and 50 using list comprehension.
"""
evens = [x for x in range(1, 51) if x % 2 == 0]
print(evens)
# Output: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]