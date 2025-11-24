# 1. Numbers from 1 to 10
print(tuple(i for i in range(1, 11)))

# 2. Squares of numbers 1 to 10
print(tuple(i*i for i in range(1, 11)))

# 3. Even numbers between 1 and 20
print(tuple(i for i in range(1, 21) if i % 2 == 0))

# 4. Odd numbers 1 to 15
print(tuple(i for i in range(1, 16) if i % 2 != 0))

# 5. Cubes of numbers 1 to 5
print(tuple(i**3 for i in range(1, 6)))

# 6. All uppercase letters in a string
s = "Hello World"
print(tuple(ch for ch in s if ch.isupper()))

# 7. Length of each word
words = ["apple", "banana", "cherry"]
print(tuple(len(w) for w in words))

# 8. Numbers divisible by 3 from 1–30
print(tuple(i for i in range(1, 31) if i % 3 == 0))

# 9. Characters except vowels
text = "COMPREHENSION"
print(tuple(ch for ch in text if ch.lower() not in "aeiou"))

# 10. All elements ×2
nums = [1, 2, 3, 4]
print(tuple(i * 2 for i in nums))

# 11. Squares of even numbers from 1–20
print(tuple(i*i for i in range(1, 21) if i % 2 == 0))

# 12. Elements greater than 50
nums = [10, 60, 75, 45, 100]
print(tuple(i for i in nums if i > 50))

# 13. Reversed strings
words = ["apple", "banana", "grape"]
print(tuple(w[::-1] for w in words))

# 14. (Number, square) pairs
print(tuple((i, i*i) for i in range(1, 6)))

# 15. (Index, value) pairs
lst = ["a", "b", "c"]
print(tuple((i, v) for i, v in enumerate(lst)))

# 16. Lowercase letters from string
s = "Python PROGRAM"
print(tuple(ch for ch in s if ch.islower()))

# 17. Unique elements using set
nums = [1, 2, 2, 3, 4, 4, 5]
print(tuple({i for i in nums}))

# 18. Numbers 1–20 skipping multiples of 5
print(tuple(i for i in range(1, 21) if i % 5 != 0))

# 19. Factorials of 1–6
def fact(n):
    f = 1
    for i in range(1, n+1):
        f *= i
    return f
print(tuple(fact(i) for i in range(1, 7)))

# 20. Tuples (n, n², n³)
print(tuple((n, n**2, n**3) for n in range(1, 6)))

# 21. Booleans if numbers 1–10 are even
print(tuple(i % 2 == 0 for i in range(1, 11)))

# 22. Words starting with a specific letter
words = ["apple", "banana", "avocado", "grape"]
letter = "a"
print(tuple(w for w in words if w.startswith(letter)))

# 23. ASCII values of each char in "Python"
print(tuple(ord(ch) for ch in "Python"))

# 24. Characters with even ASCII
print(tuple(ch for ch in "Python" if ord(ch) % 2 == 0))

# 25. Strings uppercased from lowercase list
words = ["apple", "grape", "melon"]
print(tuple(w.upper() for w in words))

# 26. Words longer than 4 letters
sentence = "Python comprehension makes coding easy"
print(tuple(w for w in sentence.split() if len(w) > 4))

# 27. All digits in string
s = "abc123xyz456"
print(tuple(ch for ch in s if ch.isdigit()))

# 28. Power of 2 if even else 3 if odd
nums = [1, 2, 3, 4, 5]
print(tuple(i**2 if i % 2 == 0 else i**3 for i in nums))

# 29. All possible products from two lists
a = [1, 2]
b = [3, 4]
print(tuple(x * y for x in a for y in b))

# 30. All pairs (x, y)
print(tuple((x, y) for x in range(1, 4) for y in range(4, 7)))

# 31. Elements not present in another list
a = [1, 2, 3, 4]
b = [3, 4, 5]
print(tuple(i for i in a if i not in b))

# 32. Prime numbers 1–50
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: return False
    return True
print(tuple(i for i in range(1, 51) if is_prime(i)))

# 33. Words stripped of punctuation
text = ["hello,", "world!", "python."]
print(tuple(w.strip(".,!") for w in text))

# 34. All characters except spaces
s = "Python is fun"
print(tuple(ch for ch in s if ch != " "))

# 35. Squares of numbers from 1–10
print(tuple(i**2 for i in range(1, 11)))

# 36. Length of each element in a tuple
t = ("apple", "banana", "kiwi")
print(tuple(len(i) for i in t))

# 37. Elements appearing more than once
lst = [1, 2, 2, 3, 4, 4, 5]
print(tuple(i for i in set(lst) if lst.count(i) > 1))

# 38. Indexes of a specific char
s = "comprehension"
target = "e"
print(tuple(i for i, ch in enumerate(s) if ch == target))

# 39. (Char, ASCII) for "COMPREHENSION"
s = "COMPREHENSION"
print(tuple((ch, ord(ch)) for ch in s))

# 40. Unique words from a sentence
sentence = "Python is fun and Python is powerful"
print(tuple({w for w in sentence.split()}))
