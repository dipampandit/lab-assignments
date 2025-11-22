# 1. Create a set containing the numbers 1 through 5.
s = {1, 2, 3, 4, 5}
print(s)

# 2. What is the length of the set {1, 2, 3, 4, 5, 5, 6, 7}? Explain why duplicates do not affect the length.
s = {1, 2, 3, 4, 5, 5, 6, 7}
print("Length of set:", len(s))  # Duplicates are ignored in sets

# 3. Add the number 8 to the set {1, 2, 3, 4, 5}.
s = {1, 2, 3, 4, 5}
s.add(8)
print(s)

# 4. Remove the number 4 from the set {1, 2, 3, 4, 5}.
s = {1, 2, 3, 4, 5}
s.remove(4)
print(s)

# 5. Check if the number 3 is in the set {1, 2, 3, 4, 5}.
s = {1, 2, 3, 4, 5}
print(3 in s)

# 6. Create two sets: A = {1, 2, 3} and B = {3, 4, 5}. Find the union of sets A and B.
A = {1, 2, 3}
B = {3, 4, 5}
print(A | B)

# 7. Using sets A = {1, 2, 3} and B = {3, 4, 5}, find the intersection of A and B.
A = {1, 2, 3}
B = {3, 4, 5}
print(A & B)

# 8. With sets A = {1, 2, 3} and B = {3, 4, 5}, find the difference of A and B.
A = {1, 2, 3}
B = {3, 4, 5}
print(A - B)

# 9. Check if A = {1, 2, 3} is a subset of B = {1, 2, 3, 4, 5}.
A = {1, 2, 3}
B = {1, 2, 3, 4, 5}
print(A.issubset(B))

# 10. Verify if A = {1, 2, 3, 4, 5} and B = {5, 4, 3, 2, 1} are equal sets.
A = {1, 2, 3, 4, 5}
B = {5, 4, 3, 2, 1}
print(A == B)

# 11. Use set comprehension to create a set of squares for numbers 1 through 5.
squares = {x**2 for x in range(1, 6)}
print(squares)

# 12. Use a set comprehension to find all even numbers from a list [1, 2, 3, 4, 5, 6].
nums = [1, 2, 3, 4, 5, 6]
evens = {x for x in nums if x % 2 == 0}
print(evens)

# 13. Create a set of only unique vowels in the string "programming".
vowels = {ch for ch in "programming" if ch in "aeiou"}
print(vowels)

# 14. Given a set {2, 3, 4, 5}, write a conditional to check if all elements are greater than 1.
s = {2, 3, 4, 5}
print(all(x > 1 for x in s))

# 15. Write a comprehension to create a set of words from the list ["apple", "banana", "apple", "cherry", "banana"].
fruits = ["apple", "banana", "apple", "cherry", "banana"]
unique = {fruit for fruit in fruits}
print(unique)

# 16. Create a set with values from 1 to 10 and remove all even numbers.
s = set(range(1, 11))
for x in list(s):
    if x % 2 == 0:
        s.remove(x)
print(s)

# 17. Check if two sets X = {2, 4, 6} and Y = {3, 4, 5} have any elements in common.
X = {2, 4, 6}
Y = {3, 4, 5}
print(not X.isdisjoint(Y))

# 18. Using a set of numbers from 1 to 10, find the symmetric difference with a set {5, 6, 7, 8, 11, 12}.
A = set(range(1, 11))
B = {5, 6, 7, 8, 11, 12}
print(A ^ B)

# 19. Create a set from the dictionary keys {'name': 'Alice', 'age': 25, 'city': 'New York'}.
dic = {'name': 'Alice', 'age': 25, 'city': 'New York'}
print(set(dic.keys()))

# 20. Write a program that accepts a list of numbers and returns a set of numbers that appear more than once.
nums = [1, 2, 3, 2, 4, 5, 1, 6, 2]
duplicates = {x for x in nums if nums.count(x) > 1}
print(duplicates)
