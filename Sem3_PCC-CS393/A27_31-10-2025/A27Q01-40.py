# What is set comprehension in Python?
# It is a concise way to create sets using a single line expression.
squares = {x**2 for x in range(5)}
print(squares)

# How do you create a set of squares for numbers 1 to 5 using set comprehension?
squares = {x**2 for x in range(1, 6)}
print(squares)

# Write a set comprehension to extract even numbers from a list.
nums = [1, 2, 3, 4, 5, 6]
evens = {x for x in nums if x % 2 == 0}
print(evens)

# How can you use set comprehension to remove duplicates from a list?
nums = [1, 2, 2, 3, 4, 4, 5]
unique = {x for x in nums}
print(unique)

# Create a set comprehension to store the first letter of each word in a list of strings.
words = ["apple", "banana", "cherry"]
first_letters = {w[0] for w in words}
print(first_letters)

# Write a set comprehension to generate a set of all vowels in a given string.
text = "programming"
vowels = {ch for ch in text if ch in "aeiou"}
print(vowels)

# How can you use set comprehension to get all unique characters from a string?
s = "hello world"
unique_chars = {ch for ch in s}
print(unique_chars)

# Write a set comprehension that includes only numbers divisible by 3 from a range of 1 to 30.
div3 = {x for x in range(1, 31) if x % 3 == 0}
print(div3)

# How do you create a set of squares only for odd numbers using set comprehension?
odd_squares = {x**2 for x in range(1, 11) if x % 2 != 0}
print(odd_squares)

# Write a set comprehension that converts all words in a list to uppercase.
words = ["apple", "banana", "cherry"]
upper = {w.upper() for w in words}
print(upper)

# How can you use set comprehension to find unique lengths of words in a sentence?
sentence = "Set comprehension makes Python powerful and elegant"
unique_lengths = {len(word) for word in sentence.split()}
print(unique_lengths)

# Write a set comprehension to filter out all negative numbers from a list.
nums = [-3, -1, 0, 2, 4, -5]
positive = {x for x in nums if x >= 0}
print(positive)

# How do you create a set comprehension that includes only numbers greater than 50 from a given list?
nums = [10, 55, 23, 99, 60]
greater_50 = {x for x in nums if x > 50}
print(greater_50)

# Write a set comprehension to find all unique digits in a given number (as a string).
num = "123451234"
digits = {ch for ch in num}
print(digits)

# How can you use set comprehension to find all characters that are not vowels in a string?
text = "education"
non_vowels = {ch for ch in text if ch not in "aeiou"}
print(non_vowels)

# Write a set comprehension to get all unique ASCII values of characters in a word.
word = "Hello"
ascii_values = {ord(ch) for ch in word}
print(ascii_values)

# How can you use set comprehension to flatten a list of tuples into a set of unique elements?
lst = [(1, 2), (3, 4), (2, 5)]
flat = {x for t in lst for x in t}
print(flat)

# Write a set comprehension that stores only prime numbers from 1 to 50.
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

primes = {x for x in range(1, 51) if is_prime(x)}
print(primes)

# How do you use conditional logic inside a set comprehension?
result = {"even" if x % 2 == 0 else "odd" for x in range(1, 6)}
print(result)

# Write a set comprehension to store all lowercase letters from a string.
s = "PythonProgramming"
lower = {ch for ch in s if ch.islower()}
print(lower)

# How can you use set comprehension to store squares of only positive numbers from a list?
nums = [-3, -2, 1, 2, 3]
pos_squares = {x**2 for x in nums if x > 0}
print(pos_squares)

# Write a set comprehension to store all words longer than 4 letters from a list.
words = ["set", "comprehension", "is", "powerful", "tool"]
long_words = {w for w in words if len(w) > 4}
print(long_words)

# How do you use a nested set comprehension? Give an example.
nested = {y for x in [[1, 2], [3, 4]] for y in x}
print(nested)

# Write a set comprehension to get all unique factors of numbers 1 to 10.
factors = {x for n in range(1, 11) for x in range(1, n+1) if n % x == 0}
print(factors)

# How can you use set comprehension to get all unique letters in a list of words?
words = ["apple", "banana", "cherry"]
letters = {ch for w in words for ch in w}
print(letters)

# Write a set comprehension to find all unique uppercase characters in a string.
text = "HeLLo WoRLD"
upper = {ch for ch in text if ch.isupper()}
print(upper)

# How do you use set comprehension with enumerate() to create a set of indices of even numbers?
nums = [1, 2, 3, 4, 5, 6]
indices = {i for i, x in enumerate(nums) if x % 2 == 0}
print(indices)

# Write a set comprehension to get all unique multiples of 5 from 1 to 100.
multiples_5 = {x for x in range(1, 101) if x % 5 == 0}
print(multiples_5)

# How can you use set comprehension to filter words that start with a vowel?
words = ["apple", "banana", "orange", "grape"]
starts_vowel = {w for w in words if w[0].lower() in "aeiou"}
print(starts_vowel)

# Write a set comprehension that converts a list of numbers to their string equivalents.
nums = [1, 2, 3, 4]
strings = {str(x) for x in nums}
print(strings)

# How do you use set comprehension to get all unique results of x % 5 for x in range(1, 20)?
remainders = {x % 5 for x in range(1, 20)}
print(remainders)

# Write a set comprehension to extract all unique words from a paragraph.
text = "Python is powerful and Python is easy to learn"
unique_words = {word.lower() for word in text.split()}
print(unique_words)

# How can you use set comprehension to find all unique square roots of perfect squares up to 100?
roots = {int(x**0.5) for x in range(1, 101) if int(x**0.5)**2 == x}
print(roots)

# Write a set comprehension that keeps only words with unique lengths from a list.
words = ["cat", "dog", "apple", "pear", "grape"]
unique_len_words = {w for w in words if len(w) == len(set(w))}
print(unique_len_words)

# How can you use set comprehension to generate all unique pairs (i, j) where i < j for i in range(5)?
pairs = {(i, j) for i in range(5) for j in range(i+1, 5)}
print(pairs)

# Write a set comprehension that includes only characters that appear more than once in a string.
s = "programming"
repeated = {ch for ch in s if s.count(ch) > 1}
print(repeated)

# How can you use set comprehension with a function call inside it?
def square(x): return x * x
squares = {square(x) for x in range(1, 6)}
print(squares)

# Write a set comprehension to create a set of tuples (x, x**2) for x in range(1, 6).
pairs = {(x, x**2) for x in range(1, 6)}
print(pairs)

# Write a set comprehension that produces all unique letters common to two strings.
s1 = "programming"
s2 = "gaming"
common = {ch for ch in s1 if ch in s2}
print(common)
