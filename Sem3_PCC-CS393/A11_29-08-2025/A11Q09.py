"""
Q: From a list of integers, generate a list of only positive numbers.
"""
nums = [-3, -1, 0, 2, 4, -5]
positives = [x for x in nums if x > 0]
print(positives)
# Output: [2, 4]