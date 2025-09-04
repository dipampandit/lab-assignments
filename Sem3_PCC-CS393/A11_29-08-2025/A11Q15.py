"""
Q: Extract all digits from a string into a list of integers.
"""
s = "ab123cd45"
digits = [int(ch) for ch in s if ch.isdigit()]
print(digits)
# Output: [1, 2, 3, 4, 5]