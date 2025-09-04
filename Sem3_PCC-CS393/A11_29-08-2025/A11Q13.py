"""
Q: Create a list of palindromic words from a list of given words.
"""
words = ["madam", "racecar", "hello", "level"]
palindromes = [w for w in words if w == w[::-1]]
print(palindromes)
# Output: ['madam', 'racecar', 'level']