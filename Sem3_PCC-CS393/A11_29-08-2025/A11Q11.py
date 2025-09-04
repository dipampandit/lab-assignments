"""
Q: From a given sentence, extract all words that start with a vowel.
"""
sentence = "An elephant is in the open area"
words = [w for w in sentence.split() if w[0].lower() in "aeiou"]
print(words)
# Output: ['An', 'elephant', 'is', 'in', 'open', 'area']