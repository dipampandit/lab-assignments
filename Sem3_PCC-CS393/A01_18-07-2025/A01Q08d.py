a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)  # True (same object)
print(a is c)  # False (different objects with same value)
print(a == c)  # True (values are same)
