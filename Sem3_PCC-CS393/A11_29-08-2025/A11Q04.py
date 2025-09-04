"""
Q: Extract all vowels from a given string using list comprehension.
"""
s = "chandragupta"
vowels = [ch for ch in s if ch.lower() in "aeiou"]
print(vowels)
# Output: ['a', 'a', 'u', 'a']