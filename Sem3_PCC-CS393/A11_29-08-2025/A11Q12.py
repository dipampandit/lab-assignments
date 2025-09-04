"""
Q: Generate a list of numbers from 1 to 100 that are divisible by both 3 and 5.
"""
nums = [x for x in range(1, 101) if x % 3 == 0 and x % 5 == 0]
print(nums)
# Output: [15, 30, 45, 60, 75, 90]