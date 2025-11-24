# 1. What is the correct way to create an empty tuple in Python?
t = ()
print(t)

# 2. What will be the output type of t = (1, 2, 3); print(type(t))?
t = (1, 2, 3)
print(type(t))      #Output: <class 'tuple'>

# 3. Are tuples mutable or immutable in Python?
t = (1, 2, 3)
# Tuples are immutable
print("Immutable")

# 4. What is the result of tuple([1, 2, 3])?
print(tuple([1, 2, 3]))

# 5. Which function is used to convert a tuple into a list?
t = (1, 2, 3)
print(list(t))

# 6. What is the output of tuple('abc')?
print(tuple('abc'))

# 7. What is the output of ''.join(('h', 'e', 'l', 'l', 'o'))?
print(''.join(('h', 'e', 'l', 'l', 'o')))

# 8. What does str((1, 2, 3)) return?
print(str((1, 2, 3)))

# 9. What is the result of tuple((1, 2, 3))?
print(tuple((1, 2, 3)))

# 10. What is the result of set((1, 2, 3, 3))?
print(set((1, 2, 3, 3)))

# 11. What is returned by tuple({'a': 1, 'b': 2})?
print(tuple({'a': 1, 'b': 2}))

# 12. What will be the output of dict((('a', 1), ('b', 2)))?
print(dict((('a', 1), ('b', 2))))

# 13. What is the result of tuple(range(1, 4))?
print(tuple(range(1, 4)))

# 14. What will tuple(float(x) for x in (1, 2)) return?
print(tuple(float(x) for x in (1, 2)))

# 15. What is the output of tuple(b'hi')?
print(tuple(b'hi'))

# 16. Which statement correctly converts a tuple of integers to bytes?
print(bytes((65, 66, 67)))

# 17. What will complex(1, 2) return?
print(complex(1, 2))

# 18. What is the result of converting [[1, 2], [3, 4]] to a nested tuple?
print(tuple([tuple(x) for x in [[1, 2], [3, 4]]]))

# 19. What is the output of tuple(map(int, ('1', '2', '3')))?
print(tuple(map(int, ('1', '2', '3'))))

# 20. What will tuple(map(float, ('1.1', '2.2'))) return?
print(tuple(map(float, ('1.1', '2.2'))))

# 21. What is the result of tuple(map(str, (1, 2, 3)))?
print(tuple(map(str, (1, 2, 3))))

# 22. What is the output of xxx(x**2 for x in (1, 2))? (Replace xxx with tuple)
print(tuple(x**2 for x in (1, 2)))

# 23. Which method is not valid for tuple conversion?
print("list_to_tuple_only")  # placeholder

# 24. Why are tuples often preferred over lists in certain situations?
print("Tuples are faster and immutable")

# 25. What happens when you try to modify a tuple element with t[0] = 100?
print("'tuple' object does not support item assignment")

# 26. How can you create a tuple with only one element?
t = (5,)
print(t)

# 27. What is the length of tuple('Python')?
print(len(tuple("Python")))

# 28. Which built-in function cannot directly convert to a tuple?
print("int")  # int() cannot convert sequences to tuples

# 29. What is the output of iterating through a tuple using a for loop and printing elements separated by spaces?
t = (1, 2, 3)
print(*t)
