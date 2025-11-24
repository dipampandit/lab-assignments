# 1. Square each number
def square(x): return x * x
nums = [1, 2, 3, 4, 5]
print(list(map(square, nums)))

# 2. Integers to string equivalents
def to_str(x): return str(x)
nums = [1, 2, 3]
print(list(map(to_str, nums)))

# 3. Length of each word
def word_len(w): return len(w)
words = ["hello", "world", "python"]
print(list(map(word_len, words)))

# 4. Add 5 to every number
def add5(x): return x + 5
nums = [10, 20, 30]
print(list(map(add5, nums)))

# 5. Celsius to Fahrenheit
def c_to_f(c): return (c * 9/5) + 32
temps = [0, 25, 100]
print(list(map(c_to_f, temps)))

# 6. Capitalize each string
def cap(s): return s.capitalize()
names = ["alice", "bob", "carol"]
print(list(map(cap, names)))

# 7. Floats to integers
def to_int(f): return int(f)
floats = [1.2, 3.8, 5.5]
print(list(map(to_int, floats)))

# 8. Multiply each element by 10
def mul10(x): return x * 10
nums = [1, 2, 3]
print(list(map(mul10, nums)))

# 9. Numbers to binary
def to_bin(x): return bin(x)[2:]
nums = [2, 5, 10]
print(list(map(to_bin, nums)))

# 10. Even or Odd
def even_odd(x): return "Even" if x % 2 == 0 else "Odd"
nums = [1, 2, 3, 4]
print(list(map(even_odd, nums)))

# 11. Add elements pairwise
def add_pair(a, b): return a + b
a = [1, 2, 3]
b = [4, 5, 6]
print(list(map(add_pair, a, b)))

# 12. Reverse each string
def reverse(s): return s[::-1]
words = ["apple", "banana", "cherry"]
print(list(map(reverse, words)))

# 13. Factorial of each number
def fact(n):
    f = 1
    for i in range(1, n + 1):
        f *= i
    return f
nums = [3, 4, 5]
print(list(map(fact, nums)))

# 14. Extract names from tuple
def get_name(t): return t[0]
data = [("Alice", 20), ("Bob", 25)]
print(list(map(get_name, data)))

# 15. Convert string numbers to integers
def to_int_str(s): return int(s)
str_nums = ["1", "2", "3"]
print(list(map(to_int_str, str_nums)))

# 16. Strip whitespace
def strip_ws(s): return s.strip()
lines = ["  hello  ", " world ", "python "]
print(list(map(strip_ws, lines)))

# 17. Round to 2 decimals
def round2(f): return round(f, 2)
nums = [1.2345, 2.6789, 3.14159]
print(list(map(round2, nums)))

# 18. Positive, Negative, or Zero
def classify(x):
    if x > 0: return "Positive"
    elif x < 0: return "Negative"
    else: return "Zero"
nums = [10, -5, 0, 7]
print(list(map(classify, nums)))

# 19. Larger number at each index
def larger(a, b): return a if a > b else b
a = [1, 5, 3]
b = [2, 4, 6]
print(list(map(larger, a, b)))

# 20. Strings of comma-separated numbers to list of ints
def to_int_list(s): return list(map(int, s.split(',')))
data = ["1,2,3", "4,5,6"]
print(list(map(to_int_list, data)))

# 21. Extract marks from list of dicts
def get_marks(d): return d['marks']
students = [{"name": "A", "marks": 90}, {"name": "B", "marks": 85}]
print(list(map(get_marks, students)))

# 22. Cube only if divisible by 3
def cube_if3(x): return x**3 if x % 3 == 0 else x
nums = [2, 3, 4, 6, 9]
print(list(map(cube_if3, nums)))

# 23. Apply multiple string functions
def both_cases(s): return (s.upper(), s.lower())
words = ["Hello", "World"]
print(list(map(both_cases, words)))

# 24. Remove file extensions
def remove_ext(f): return f.split('.')[0]
files = ["data.txt", "image.png", "script.py"]
print(list(map(remove_ext, files)))

# 25. Check if string starts with vowel
def starts_with_vowel(s): return s[0].lower() in "aeiou"
words = ["apple", "banana", "orange", "grape"]
print(list(map(starts_with_vowel, words)))

# 26. Flatten one level of nesting
def flatten_list(lists):
    result = []
    for sub in lists:
        result.extend(sub)
    return result
nested = [[1, 2], [3, 4], [5, 6]]
print(flatten_list(nested))

# 27. Length of each sublist
def sublist_len(l): return len(l)
lists = [[1, 2], [3, 4, 5], [6]]
print(list(map(sublist_len, lists)))

# 28. Prime or Composite
def is_prime(n):
    if n < 2: return "Composite"
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return "Composite"
    return "Prime"
nums = [2, 4, 5, 9, 11]
print(list(map(is_prime, nums)))
