# 1. Slice and print the first 3 elements of a tuple.
t = (1, 2, 3, 4, 5)
print(t[:3])

# 2. Given a tuple t = (10, 20, 30, 40, 50), slice and print the last 2 elements.
t = (10, 20, 30, 40, 50)
print(t[-2:])

# 3. Slice a tuple to print all elements except the first one.
t = (1, 2, 3, 4, 5)
print(t[1:])

# 4. Slice a tuple to print all elements except the last one.
t = (1, 2, 3, 4, 5)
print(t[:-1])

# 5. Slice and print the middle three elements of a 7-element tuple.
t = (1, 2, 3, 4, 5, 6, 7)
print(t[2:5])

# 6. Given t = (1, 2, 3, 4, 5, 6), slice and print elements from index 2 to 4.
t = (1, 2, 3, 4, 5, 6)
print(t[2:5])

# 7. Slice a tuple to print elements from the start up to index 3 (excluding 3).
t = (10, 20, 30, 40, 50)
print(t[:3])

# 8. Slice a tuple to print elements from index 3 to the end.
t = (10, 20, 30, 40, 50, 60)
print(t[3:])

# 9. Given a tuple of 10 elements, slice and print every 2nd element.
t = tuple(range(1, 11))
print(t[::2])

# 10. Write a program to reverse a tuple using slicing.
t = (1, 2, 3, 4, 5)
print(t[::-1])

# 11. Given t = (5, 10, 15, 20, 25, 30), slice to print (10, 15, 20).
t = (5, 10, 15, 20, 25, 30)
print(t[1:4])

# 12. Slice a tuple using negative indices to print the last 3 elements.
t = (10, 20, 30, 40, 50)
print(t[-3:])

# 13. Write a program to slice and print a tuple excluding the first and last elements.
t = (1, 2, 3, 4, 5)
print(t[1:-1])

# 14. Given t = (1, 2, 3, 4, 5, 6, 7, 8, 9), slice to get elements at even indices.
t = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(t[::2])

# 15. Slice a tuple to get elements at odd indices.
t = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(t[1::2])

# 16. Write a program to get the first half of a tuple using slicing.
t = (1, 2, 3, 4, 5, 6)
print(t[:len(t)//2])

# 17. Write a program to get the second half of a tuple using slicing.
t = (1, 2, 3, 4, 5, 6)
print(t[len(t)//2:])

# 18. Given t = ('a', 'b', 'c', 'd', 'e', 'f'), slice to get ('b', 'c', 'd', 'e').
t = ('a', 'b', 'c', 'd', 'e', 'f')
print(t[1:-1])

# 19. Slice a tuple to get all elements except the first 3 and last 2.
t = (1, 2, 3, 4, 5, 6, 7, 8)
print(t[3:-2])

# 20. Write a program to get a slice of a tuple starting from index 1 to index -1.
t = (10, 20, 30, 40, 50)
print(t[1:-1])

# 21. Given a nested tuple, slice the outer tuple to get the last two inner tuples.
t = ((1, 2), (3, 4), (5, 6), (7, 8))
print(t[-2:])

# 22. Slice a tuple to print every 3rd element starting from index 0.
t = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(t[::3])

# 23. Slice a tuple to print every 2nd element starting from index 1.
t = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(t[1::2])

# 24. Write a program to check if slicing a tuple returns a new tuple or modifies the original.
t = (1, 2, 3, 4)
sliced = t[:2]
print("Original:", t)
print("Sliced:", sliced)
print("Same object?", t is sliced)

# 25. Given t = (100, 200, 300, 400, 500), use slicing to extract (200, 300, 400).
t = (100, 200, 300, 400, 500)
print(t[1:4])

# 26. Use a slice with step -2 to print elements in reverse with alternate skipping.
t = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(t[::-2])

# 27. Write a program to slice a tuple to obtain only the last element using negative indexing.
t = (10, 20, 30, 40, 50)
print(t[-1:])

# 28. Slice a tuple to get elements between index -5 and -2.
t = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(t[-5:-2])

# 29. Slice a tuple of elements between index 3 and 5.
t = (1, 2, 3, 4, 5, 6, 7, 8)
print(t[3:6])

# 30. Write a Python program to slice a tuple dynamically based on user-provided start, end, and step values.
t = (10, 20, 30, 40, 50, 60, 70)
start = int(input("Enter start index: "))
end = int(input("Enter end index: "))
step = int(input("Enter step value: "))
print(t[start:end:step])
