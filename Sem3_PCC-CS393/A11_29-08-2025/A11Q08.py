"""
Q: Create a list of all uppercase characters from a string.
"""
s = "PyThOn LiSt CoMpReHeNsIoN"
upper_chars = [ch for ch in s if ch.isupper()]
print(upper_chars)
# Output: ['P', 'T', 'O', 'L', 'C', 'M', 'R', 'H', 'I']