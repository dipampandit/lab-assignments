# 1. Create a dictionary from user input and display all key-value pairs.

d1 = {}
n = int(input("Enter number of pairs: "))
for _ in range(n):
    key = input("Key: ")
    value = input("Value: ")
    d1[key] = value
print(d1)
for k, v in d1.items():
    print(k, ":", v)


# 2. Count the frequency of each character in a string using a dictionary.

s = input("Enter a string: ")
d2 = {}
for ch in s:
    d2[ch] = d2.get(ch, 0) + 1
print(d2)


# 3. Find the key associated with the maximum value in a dictionary.

d3 = {'a': 10, 'b': 25, 'c': 15}
max_key = max(d3, key=lambda x: d3[x])
print(max_key)


# 4. Reverse a dictionary by swapping keys and values.

d4 = {'a': 1, 'b': 2, 'c': 3}
reversed_dict = {v: k for k, v in d4.items()}
print(reversed_dict)


# 5. Merge two dictionaries without using update().

d5 = {'a': 1, 'b': 2}
d5_2 = {'c': 3, 'd': 4}
merged = {**d5, **d5_2}
print(merged)


# 6. Merge three dictionaries using dictionary unpacking.

d6 = {'a': 1}
d6_2 = {'b': 2}
d6_3 = {'c': 3}
result = {**d6, **d6_2, **d6_3}
print(result)


# 7. Check whether a given key exists in a dictionary.

d7 = {'a': 10, 'b': 20, 'c': 30}
key = input("Enter key: ")
print(key in d7)


# 8. Replace the value of an existing key if it exists.

d8 = {'a': 10, 'b': 20}
key = 'a'
if key in d8:
    d8[key] = 100
print(d8)


# 9. Add a new key only if it is not already present.

d9 = {'a': 10, 'b': 20}
key = 'c'
if key not in d9:
    d9[key] = 30
print(d9)


# 10. Remove a key safely without raising an error.

d10 = {'a': 10, 'b': 20}
d10.pop('c', None)
print(d10)


# 11. Create a dictionary from two lists using zip().

keys = ['a', 'b', 'c']
values = [10, 20, 30]
d11 = dict(zip(keys, values))
print(d11)


# 12. Convert a list of tuples into a dictionary.

data = [('a', 1), ('b', 2), ('c', 3)]
d12 = dict(data)
print(d12)


# 13. Create a dictionary containing squares of numbers from 1 to N.

n = 5
d13 = {i: i**2 for i in range(1, n + 1)}
print(d13)


# 14. Create a dictionary containing cubes of numbers from 1 to N.

n = 5
d14 = {i: i**3 for i in range(1, n + 1)}
print(d14)


# 15. Generate a dictionary of even numbers and their squares.

n = 10
d15 = {i: i**2 for i in range(2, n + 1, 2)}
print(d15)


# 16. Generate a dictionary of odd numbers and their cubes.

n = 10
d16 = {i: i**3 for i in range(1, n + 1, 2)}
print(d16)


# 17. Find the sum of all dictionary values.

d17 = {'a': 10, 'b': 20, 'c': 30}
total = sum(d17.values())
print(total)


# 18. Find the average of all dictionary values.

d18 = {'a': 10, 'b': 20, 'c': 30}
avg = sum(d18.values()) / len(d18)
print(avg)


# 19. Find the minimum-valued key in a dictionary.

d19 = {'a': 10, 'b': 5, 'c': 15}
min_key = min(d19, key=lambda x: d19[x])
print(min_key)


# 20. Find the maximum-valued key in a dictionary.

d20 = {'a': 10, 'b': 5, 'c': 15}
max_key = max(d20, key=lambda x: d20[x])
print(max_key)


# 21. Sort a dictionary by keys in ascending order.

d21 = {'c': 30, 'a': 10, 'b': 20}
sorted_d21 = dict(sorted(d21.items()))
print(sorted_d21)


# 22. Sort a dictionary by keys in descending order.

d22 = {'c': 30, 'a': 10, 'b': 20}
sorted_d22 = dict(sorted(d22.items(), reverse=True))
print(sorted_d22)


# 23. Sort a dictionary by values in ascending order.

d23 = {'a': 30, 'b': 10, 'c': 20}
sorted_d23 = dict(sorted(d23.items(), key=lambda item: item[1]))
print(sorted_d23)


# 24. Sort a dictionary by values in descending order.

d24 = {'a': 30, 'b': 10, 'c': 20}
sorted_d24 = dict(sorted(d24.items(), key=lambda item: item[1], reverse=True))
print(sorted_d24)


# 25. Remove duplicate values from a dictionary.

d25 = {'a': 10, 'b': 20, 'c': 10, 'd': 30}
unique_d25 = {}
for k, v in d25.items():
    if v not in unique_d25.values():
        unique_d25[k] = v
print(unique_d25)


# 26. Create a frequency dictionary for words in a sentence.

sentence = "python is easy and python is powerful"
words = sentence.split()
d26 = {}
for word in words:
    d26[word] = d26.get(word, 0) + 1
print(d26)


# 27. Find the most frequent word in a sentence.

sentence = "python is easy and python is powerful"
words = sentence.split()
d27 = {}
for word in words:
    d27[word] = d27.get(word, 0) + 1
most_frequent = max(d27, key=lambda x: d27[x])
print(most_frequent)


# 28. Find all keys having the same value.

d28 = {'a': 10, 'b': 20, 'c': 10, 'd': 30}
value = 10
keys = [k for k, v in d28.items() if v == value]
print(keys)


# 29. Create a nested dictionary for student records.

d29 = {
    '101': {'name': 'Amit', 'marks': 85},
    '102': {'name': 'Riya', 'marks': 90}
}
print(d29)


# 30. Calculate the total marks of each student from a nested dictionary.

d30 = {
    'Amit': {'Math': 80, 'Science': 90},
    'Riya': {'Math': 85, 'Science': 95}
}
for student, marks in d30.items():
    total = sum(marks.values())
    print(student, total)


# 31. Find the topper from a nested dictionary of students.

d31 = {
    'Amit': {'total': 170},
    'Riya': {'total': 180},
    'Raj': {'total': 160}
}
topper = max(d31, key=lambda k: d31[k]['total'])
print(topper)


# 32. Update marks of a student inside a nested dictionary.

d32 = {
    'Amit': {'marks': 80},
    'Riya': {'marks': 90}
}
d32['Amit']['marks'] = 95
print(d32)


# 33. Delete a course from a nested dictionary.

d33 = {
    'Amit': {'Math': 80, 'Science': 90}
}
del d33['Amit']['Science']
print(d33)


# 34. Add a new student record dynamically.

d34 = {
    '101': {'name': 'Amit', 'marks': 85}
}
d34['102'] = {'name': 'Riya', 'marks': 90}
print(d34)


# 35. Flatten a nested dictionary into a single-level dictionary.

d35 = {
    'student': {'name': 'Amit', 'marks': 85}
}
flat_d35 = {}
for k, v in d35.items():
    for sub_k, sub_v in v.items():
        flat_d35[sub_k] = sub_v
print(flat_d35)


# 36. Count the total number of keys in a nested dictionary.

d36 = {
    'A': {'x': 1, 'y': 2},
    'B': {'z': 3}
}
count = len(d36)
for v in d36.values():
    count += len(v)
print(count)


# 37. Create a multiplication table using nested dictionary comprehension.

d37 = {i: {j: i * j for j in range(1, 6)} for i in range(1, 6)}
print(d37)


# 38. Generate coordinate pairs (x, y) as dictionary keys.

d38 = {(x, y): x + y for x in range(3) for y in range(3)}
print(d38)


# 39. Store factorial values from 1 to N in a dictionary.

d39 = {}
fact = 1
n = 5
for i in range(1, n + 1):
    fact *= i
    d39[i] = fact
print(d39)


# 40. Create a dictionary mapping numbers to "Even" or "Odd".

d40 = {i: "Even" if i % 2 == 0 else "Odd" for i in range(1, 11)}
print(d40)


# 41. Create a dictionary mapping numbers to "Prime" or "Composite".

d41 = {}
for i in range(2, 21):
    is_prime = True
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            is_prime = False
            break
    d41[i] = "Prime" if is_prime else "Composite"
print(d41)


# 42. Find all prime-number keys in a dictionary.

d42 = {2: 'a', 3: 'b', 4: 'c', 5: 'd', 6: 'e'}
prime_keys = []
for key in d42:
    if key > 1:
        is_prime = True
        for i in range(2, int(key ** 0.5) + 1):
            if key % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_keys.append(key)
print(prime_keys)


# 43. Create a dictionary using enumerate().

fruits = ['apple', 'banana', 'mango']
d43 = dict(enumerate(fruits))
print(d43)


# 44. Convert dictionary keys into a list.

d44 = {'a': 1, 'b': 2, 'c': 3}
keys_list = list(d44.keys())
print(keys_list)


# 45. Convert dictionary values into a tuple.

d45 = {'a': 1, 'b': 2, 'c': 3}
values_tuple = tuple(d45.values())
print(values_tuple)


# 46. Find common keys between two dictionaries.

d46 = {'a': 1, 'b': 2, 'c': 3}
d46_2 = {'b': 5, 'c': 6, 'd': 7}
common_keys = d46.keys() & d46_2.keys()
print(common_keys)


# 47. Find common values between two dictionaries.

d47 = {'a': 1, 'b': 2, 'c': 3}
d47_2 = {'x': 2, 'y': 3, 'z': 4}
common_values = set(d47.values()) & set(d47_2.values())
print(common_values)


# 48. Find keys present in one dictionary but not another.

d48 = {'a': 1, 'b': 2, 'c': 3}
d48_2 = {'b': 2, 'c': 3, 'd': 4}
difference = d48.keys() - d48_2.keys()
print(difference)


# 49. Create a dictionary from a string and count vowels.

s = "programming"
d49 = {}
for ch in s.lower():
    if ch in "aeiou":
        d49[ch] = d49.get(ch, 0) + 1
print(d49)


# 50. Find the least frequent character in a string.

s = "programming"
d50 = {}
for ch in s:
    d50[ch] = d50.get(ch, 0) + 1
least_char = min(d50, key=lambda x: d50[x])
print(least_char)


# 51. Find all characters occurring exactly twice.

s = "programming"
d51 = {}
for ch in s:
    d51[ch] = d51.get(ch, 0) + 1
result = [ch for ch, count in d51.items() if count == 2]
print(result)


# 52. Create a histogram using a dictionary.

numbers = [1, 2, 2, 3, 3, 3, 4]
d52 = {}
for num in numbers:
    d52[num] = d52.get(num, 0) + 1
print(d52)


# 53. Group words by their lengths using a dictionary.

words = ["cat", "dog", "apple", "ball"]
d53 = {}
for word in words:
    length = len(word)
    d53.setdefault(length, []).append(word)
print(d53)


# 54. Group students by grades using a dictionary.

students = {'Amit': 'A', 'Riya': 'B', 'Raj': 'A'}
d54 = {}
for name, grade in students.items():
    d54.setdefault(grade, []).append(name)
print(d54)


# 55. Create a dictionary where keys are uppercase versions of words.

words = ["python", "java", "c"]
d55 = {word.upper(): word for word in words}
print(d55)


# 56. Create a dictionary of word lengths.

words = ["python", "java", "c"]
d56 = {word: len(word) for word in words}
print(d56)


# 57. Find all palindromic words and store their lengths.

words = ["madam", "python", "level", "radar"]
d57 = {word: len(word) for word in words if word == word[::-1]}
print(d57)


# 58. Create a dictionary using dictionary comprehension and filters.

d58 = {x: x ** 2 for x in range(1, 11) if x % 2 == 0}
print(d58)


# 59. Create a dictionary containing only values greater than 100.

d59 = {'a': 50, 'b': 150, 'c': 200, 'd': 80}
filtered_d59 = {k: v for k, v in d59.items() if v > 100}
print(filtered_d59)


# 60. Create a dictionary containing only keys divisible by 3.

d60 = {1: 'a', 3: 'b', 6: 'c', 8: 'd', 9: 'e'}
filtered_d60 = {k: v for k, v in d60.items() if k % 3 == 0}
print(filtered_d60)


# 61. Use setdefault() to build a grouping dictionary.

words = ['apple', 'ant', 'banana', 'ball']
d61 = {}
for word in words:
    d61.setdefault(word[0], []).append(word)
print(d61)


# 62. Use get() to count occurrences efficiently.

numbers = [1, 2, 2, 3, 3, 3]
d62 = {}
for num in numbers:
    d62[num] = d62.get(num, 0) + 1
print(d62)


# 63. Compare two dictionaries and display differences.

d63 = {'a': 1, 'b': 2, 'c': 3}
d63_2 = {'a': 1, 'b': 5, 'd': 4}
difference = {}
for key in set(d63) | set(d63_2):
    if d63.get(key) != d63_2.get(key):
        difference[key] = (d63.get(key), d63_2.get(key))
print(difference)


# 64. Check whether two dictionaries are identical.

d64 = {'a': 1, 'b': 2}
d64_2 = {'a': 1, 'b': 2}
print(d64 == d64_2)


# 65. Find the intersection of two dictionaries.

d65 = {'a': 1, 'b': 2, 'c': 3}
d65_2 = {'b': 2, 'c': 5, 'd': 4}
intersection = {k: d65[k] for k in d65 if k in d65_2 and d65[k] == d65_2[k]}
print(intersection)


# 66. Find the union of two dictionaries using |.

d66 = {'a': 1, 'b': 2}
d66_2 = {'c': 3, 'd': 4}
union_d66 = d66 | d66_2
print(union_d66)


# 67. Update a dictionary using |=.

d67 = {'a': 1, 'b': 2}
d67_2 = {'c': 3}
d67 |= d67_2
print(d67)


# 68. Simulate a phonebook using dictionaries.

d68 = {
    'Amit': '9876543210',
    'Riya': '9123456780'
}
name = input("Enter name: ")
print(d68.get(name, "Contact not found"))


# 69. Implement a simple inventory management system.

d69 = {
    'Pen': 50,
    'Book': 20,
    'Pencil': 100
}
print(d69)
d69['Pen'] -= 5
print(d69)


# 70. Implement a student attendance tracker.

d70 = {
    'Amit': 20,
    'Riya': 18,
    'Raj': 22
}
print(d70)


# 71. Store employee records using nested dictionaries.

d71 = {
    101: {'name': 'Amit', 'salary': 50000},
    102: {'name': 'Riya', 'salary': 60000}
}
print(d71)


# 72. Search for an employee by ID.

d72 = {
    101: {'name': 'Amit', 'salary': 50000},
    102: {'name': 'Riya', 'salary': 60000}
}
emp_id = 101
print(d72.get(emp_id, "Employee not found"))


# 73. Find employees with the highest salary.

d73 = {
    'Amit': 50000,
    'Riya': 65000,
    'Raj': 65000
}
max_salary = max(d73.values())
result = [name for name, salary in d73.items() if salary == max_salary]
print(result)


# 74. Calculate average salary department-wise.

d74 = {
    'IT': {'Amit': 50000, 'Raj': 60000},
    'HR': {'Riya': 55000, 'Sita': 65000}
}
for dept, employees in d74.items():
    avg = sum(employees.values()) / len(employees)
    print(dept, avg)


# 75. Create a dictionary-based voting system.

d75 = {'A': 0, 'B': 0, 'C': 0}
votes = ['A', 'B', 'A', 'C', 'A']
for vote in votes:
    d75[vote] += 1
print(d75)


# 76. Determine the winner of a vote using dictionary counts.

d76 = {'A': 10, 'B': 15, 'C': 12}
winner = max(d76, key=lambda x: d76[x])
print(winner)


# 77. Build a menu-driven dictionary application.

d77 = {}
d77['name'] = 'Python'
print(d77)
del d77['name']
print(d77)


# 78. Implement CRUD operations on a dictionary.

d78 = {}
d78['id'] = 101
print(d78)
d78['id'] = 102
print(d78)
print(d78['id'])
del d78['id']
print(d78)


# 79. Store and retrieve course details using nested dictionaries.

d79 = {
    'CSE101': {'name': 'Python', 'credits': 4},
    'CSE102': {'name': 'DBMS', 'credits': 3}
}
print(d79['CSE101'])


# 80. Create a dictionary-based cache system.

d80 = {}
number = 5
if number not in d80:
    d80[number] = number ** 2
print(d80[number])


# 81. Find duplicate keys after merging data sources.

d81 = {'a': 1, 'b': 2, 'c': 3}
d81_2 = {'b': 5, 'd': 4}
duplicates = d81.keys() & d81_2.keys()
print(duplicates)


# 82. Simulate a library book catalog.

d82 = {
    'B101': 'Python Programming',
    'B102': 'Data Structures',
    'B103': 'Database Systems'
}
print(d82)


# 83. Find books belonging to a specific category.

d83 = {
    'Python': 'Programming',
    'Java': 'Programming',
    'Hamlet': 'Literature',
    'Macbeth': 'Literature'
}
category = 'Literature'
books = [book for book, cat in d83.items() if cat == category]
print(books)


# 84. Create a dictionary of month names and days.

d84 = {
    'January': 31,
    'February': 28,
    'March': 31,
    'April': 30,
    'May': 31,
    'June': 30,
    'July': 31,
    'August': 31,
    'September': 30,
    'October': 31,
    'November': 30,
    'December': 31
}
print(d84)


# 85. Convert a dictionary into a list of tuples.

d85 = {'a': 1, 'b': 2, 'c': 3}
tuple_list = list(d85.items())
print(tuple_list)


# 86. Convert a list of dictionaries into a single dictionary.

d86_list = [{'a': 1}, {'b': 2}, {'c': 3}]
d86 = {}
for item in d86_list:
    d86.update(item)
print(d86)


# 87. Create a dictionary from user-entered names and marks.

d87 = {}
n = int(input("Enter number of students: "))
for i in range(n):
    name = input("Enter name: ")
    marks = int(input("Enter marks: "))
    d87[name] = marks
print(d87)


# 88. Find students scoring above a threshold.

d88 = {'Amit': 75, 'Riya': 92, 'Raj': 68, 'Sita': 85}
threshold = 80
result = {k: v for k, v in d88.items() if v > threshold}
print(result)


# 89. Create a grade report using dictionary comprehension.

d89 = {'Amit': 95, 'Riya': 82, 'Raj': 67}
grades = {k: ('A' if v >= 90 else 'B' if v >= 75 else 'C') for k, v in d89.items()}
print(grades)


# 90. Build a dictionary mapping countries to capitals.

d90 = {
    'India': 'New Delhi',
    'Japan': 'Tokyo',
    'France': 'Paris'
}
print(d90)


# 91. Search for a capital by country name.

d91 = {
    'India': 'New Delhi',
    'Japan': 'Tokyo',
    'France': 'Paris'
}
country = input("Enter country name: ")
print(d91.get(country, "Country not found"))


# 92. Search for a country by capital name.

d92 = {
    'India': 'New Delhi',
    'Japan': 'Tokyo',
    'France': 'Paris'
}
capital = input("Enter capital name: ")
for country, cap in d92.items():
    if cap == capital:
        print(country)


# 93. Count occurrences of each digit in a number.

number = input("Enter a number: ")
d93 = {}
for digit in number:
    d93[digit] = d93.get(digit, 0) + 1
print(d93)


# 94. Store Fibonacci numbers in a dictionary.

d94 = {}
a, b = 0, 1
n = 10
for i in range(n):
    d94[i] = a
    a, b = b, a + b
print(d94)


# 95. Memoize Fibonacci computation using a dictionary.

d95 = {}
def fibonacci(n):
    if n in d95:
        return d95[n]
    if n <= 1:
        return n
    d95[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return d95[n]
print(fibonacci(10))


# 96. Implement a simple translation dictionary.

d96 = {
    'hello': 'namaste',
    'water': 'pani',
    'book': 'kitab'
}
word = input("Enter English word: ")
print(d96.get(word, "Translation not found"))


# 97. Create an anagram grouping dictionary.

words = ['eat', 'tea', 'ate', 'bat', 'tab']
d97 = {}
for word in words:
    key = ''.join(sorted(word))
    d97.setdefault(key, []).append(word)
print(d97)


# 98. Count frequency of each element in a list.

numbers = [1, 2, 2, 3, 3, 3, 4]
d98 = {}
for num in numbers:
    d98[num] = d98.get(num, 0) + 1
print(d98)


# 99. Find the first non-repeating element using a dictionary.

numbers = [4, 5, 1, 2, 1, 2, 5]
d99 = {}
for num in numbers:
    d99[num] = d99.get(num, 0) + 1
for num in numbers:
    if d99[num] == 1:
        print(num)
        break


# 100. Find the first repeating element using a dictionary.

numbers = [4, 5, 1, 2, 1, 2, 5]
d100 = {}
for num in numbers:
    if num in d100:
        print(num)
        break
    d100[num] = 1


# 101. Create a dictionary mapping ASCII values to characters.

d101 = {i: chr(i) for i in range(65, 91)}
print(d101)


# 102. Create a dictionary mapping characters to ASCII values.

d102 = {chr(i): i for i in range(65, 91)}
print(d102)


# 103. Count uppercase and lowercase letters using dictionaries.

text = "Python Programming"
d103 = {"uppercase": 0, "lowercase": 0}
for ch in text:
    if ch.isupper():
        d103["uppercase"] += 1
    elif ch.islower():
        d103["lowercase"] += 1
print(d103)


# 104. Store temperature readings and find the highest temperature.

d104 = {
    "Monday": 32,
    "Tuesday": 35,
    "Wednesday": 30,
    "Thursday": 36
}
highest_day = max(d104, key=lambda x: d104[x])
print(highest_day, d104[highest_day])


# 105. Store temperature readings and find the average temperature.

d105 = {
    "Monday": 32,
    "Tuesday": 35,
    "Wednesday": 30,
    "Thursday": 36
}
average = sum(d105.values()) / len(d105)
print(average)


# 106. Create a dictionary of numbers and their binary equivalents.

d106 = {i: bin(i) for i in range(1, 11)}
print(d106)


# 107. Create a dictionary of numbers and their hexadecimal equivalents.

d107 = {i: hex(i) for i in range(1, 11)}
print(d107)


# 108. Create a dictionary mapping students to their percentages.

d108 = {
    "Amit": [80, 90, 85],
    "Riya": [75, 88, 92]
}
percentage = {k: sum(v) / len(v) for k, v in d108.items()}
print(percentage)


# 109. Find students whose percentage is above 80.

d109 = {
    "Amit": 85,
    "Riya": 78,
    "Raj": 91,
    "Sita": 82
}
result = {k: v for k, v in d109.items() if v > 80}
print(result)


# 110. Create a dictionary-based shopping cart.

d110 = {
    "Pen": 10,
    "Book": 50,
    "Pencil": 5
}
print(d110)


# 111. Calculate the total bill from a shopping cart dictionary.

d111 = {
    "Pen": 10,
    "Book": 50,
    "Pencil": 5
}
total = sum(d111.values())
print(total)


# 112. Find the costliest item in a shopping cart.

d112 = {
    "Pen": 10,
    "Book": 50,
    "Pencil": 5
}
costliest = max(d112, key=lambda x: d112[x])
print(costliest, d112[costliest])


# 113. Create a dictionary of city populations.

d113 = {
    "Kolkata": 15000000,
    "Delhi": 32000000,
    "Mumbai": 21000000
}
print(d113)


# 114. Find the city with the highest population.

d114 = {
    "Kolkata": 15000000,
    "Delhi": 32000000,
    "Mumbai": 21000000
}
largest_city = max(d114, key=lambda x: d114[x])
print(largest_city)


# 115. Find the city with the lowest population.

d115 = {
    "Kolkata": 15000000,
    "Delhi": 32000000,
    "Mumbai": 21000000
}
smallest_city = min(d115, key=lambda x: d115[x])
print(smallest_city)


# 116. Create a dictionary of products and discounts.

d116 = {
    "Laptop": 10,
    "Mobile": 15,
    "Tablet": 12
}
print(d116)


# 117. Calculate discounted prices using a dictionary.

d117 = {
    "Laptop": (50000, 10),
    "Mobile": (20000, 15),
    "Tablet": (15000, 12)
}
discounted = {k: price - (price * discount / 100) for k, (price, discount) in d117.items()}
print(discounted)


# 118. Find the product with the maximum discount.

d118 = {
    "Laptop": 10,
    "Mobile": 15,
    "Tablet": 12
}
product = max(d118, key=lambda x: d118[x])
print(product)


# 119. Create a dictionary-based contact management system.

d119 = {
    "Amit": "9876543210",
    "Riya": "9123456780"
}
print(d119)
name = input("Enter contact name: ")
print(d119.get(name, "Contact not found"))