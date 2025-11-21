# How can you convert a list into a set in Python?
lst = [1, 2, 3, 4, 2, 3]
s = set(lst)
print(s)

# What happens when you convert a string into a set using the set() function?
s = set("banana")
print(s)  # Converts each unique character into a set element

# How do you convert a tuple containing duplicate elements into a set?
t = (1, 2, 3, 2, 1)
s = set(t)
print(s)

# How can you convert a dictionary’s keys into a set?
d = {'a': 1, 'b': 2, 'c': 3}
s = set(d.keys())
print(s)

# How can you convert a dictionary’s values into a set?
d = {'a': 1, 'b': 2, 'c': 3, 'd': 1}
s = set(d.values())
print(s)

# What is the result of converting a dictionary directly into a set using set(dict)?
d = {'a': 1, 'b': 2, 'c': 3}
s = set(d)
print(s)  # Only keys are printed

# How can you convert a set back into a list?
s = {1, 2, 3}
lst = list(s)
print(lst)

# How do you convert a set into a tuple?
s = {1, 2, 3}
t = tuple(s)
print(t)

# How can you convert a set into a string?
s = {'a', 'b', 'c'}
str_val = ''.join(s)
print(str_val)

# What happens when you convert a set containing numbers into a list and sort it?
s = {5, 1, 3, 2, 4}
lst = sorted(list(s))
print(lst)

# Can you convert a frozen set into a normal set? If yes, how?
fs = frozenset([1, 2, 3])
s = set(fs)
print(s)

# How do you convert a list of lists into a set without getting an error?
# Lists are unhashable, so convert each list into a tuple first
lst = [[1, 2], [3, 4], [1, 2]]
s = set(tuple(x) for x in lst)
print(s)

# What is the output of set([1, 2, 2, 3, 3, 3])?
print(set([1, 2, 2, 3, 3, 3]))  # Removes duplicates

# How can you remove duplicates from a string using set type casting?
string = "programming"
unique = ''.join(set(string))
print(unique)

# What happens when you try to convert a nested list directly into a set?
# It will cause a TypeError because lists inside are unhashable.
try:
    s = set([[1, 2], [3, 4]])
except TypeError as e:
    print("Error:", e)

# How can you convert a range object into a set?
r = range(1, 6)
s = set(r)
print(s)

# How can you convert a set into a dictionary where each element becomes both key and value?
s = {1, 2, 3}
d = {x: x for x in s}
print(d)

# What happens when you cast a boolean list into a set, like set([True, False, True])?
lst = [True, False, True]
s = set(lst)
print(s)  # True and False are treated as 1 and 0 (unique values)

# How can you convert a mixed-type list (e.g., [1, '1', 2.0]) into a set and explain the result?
lst = [1, '1', 2.0]
s = set(lst)
print(s)  # 1 and 2.0 are treated as equal because they represent the same numeric value

# How can you convert a set of characters back into a sorted string without duplicates?
s = {'b', 'a', 'd', 'c'}
sorted_str = ''.join(sorted(s))
print(sorted_str)
