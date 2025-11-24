# What is the difference between a tuple and a list in Python?
tuple_example = (1, 2, 3)
list_example = [1, 2, 3]
print("Tuple:", tuple_example, "Type:", type(tuple_example))
print("List:", list_example, "Type:", type(list_example))
print("Tuples are immutable, cannot modify elements.")
print("Lists are mutable, can modify elements.")

# Can a tuple contain mutable objects like lists? Provide an example.
mixed_tuple = ([1, 2], 3, 4)
print("Original mixed_tuple:", mixed_tuple)
mixed_tuple[0].append(3)
print("After modifying inner list:", mixed_tuple)

# How do you access elements in a tuple?
t = ("a", "b", "c", "d", "e")
print("First element:", t[0])
print("Last element:", t[-1])
print("Slice from index 1 to 3:", t[1:4])

# How do you unpack the elements of a tuple into separate variables?
coords = (10, 20, 30)
x, y, z = coords
print("Unpacked values -> x:", x, "y:", y, "z:", z)

# How can you concatenate two tuples?
t1 = (1, 2, 3)
t2 = (4, 5)
concatenated = t1 + t2
print("Concatenated tuple:", concatenated)

# Can you modify an element in a tuple? Why or why not?
immutable_tuple = (1, 2, 3)
print("Cannot modify tuple element because tuples are immutable.")

# How do you iterate through a tuple in Python?
iterate_tuple = ("red", "green", "blue")
for color in iterate_tuple:
    print("Color:", color)

# How can you check if an item exists within a tuple?
numbers = (1, 2, 3, 4, 5)
print("Is 3 in numbers?", 3 in numbers)
print("Is 10 in numbers?", 10 in numbers)

# How do you find the length of a tuple?
length_tuple = ("apple", "banana", "cherry")
print("Length of tuple:", len(length_tuple))

# Can you convert a tuple to a list? If so, how?
tuple_to_convert = (10, 20, 30)
converted_list = list(tuple_to_convert)
print("Converted list:", converted_list, "Type:", type(converted_list))

# How do you create a tuple from a list?
list_to_convert = [7, 8, 9]
converted_tuple = tuple(list_to_convert)
print("Converted tuple:", converted_tuple, "Type:", type(converted_tuple))

# What happens if you try to delete an element from a tuple?
delete_tuple = (1, 2, 3)
print("Cannot delete individual elements from a tuple.")
print("But you can delete the whole tuple object with 'del delete_tuple'.")

# How do you sort a tuple?
unsorted_tuple = (5, 2, 9, 1)
sorted_list_from_tuple = sorted(unsorted_tuple)
sorted_tuple = tuple(sorted_list_from_tuple)
print("Original tuple:", unsorted_tuple)
print("Sorted as list:", sorted_list_from_tuple)
print("Sorted as new tuple:", sorted_tuple)

# How can you find the index of a specific element in a tuple?
index_tuple = ("cat", "dog", "bird", "dog")
print("Index of 'dog' (first occurrence):", index_tuple.index("dog"))

# Can a tuple be used as a dictionary key? Explain why.
key_tuple = (1, 2, 3)
sample_dict = {key_tuple: "This tuple is a key"}
print("Dictionary with tuple key:", sample_dict)
print("Reason: Tuples are immutable and hashable, so they can be used as keys.")

# How do you reverse the order of elements in a tuple?
original_tuple = (1, 2, 3, 4, 5)
reversed_tuple = original_tuple[::-1]
print("Original tuple:", original_tuple)
print("Reversed tuple:", reversed_tuple)

# How do you slice a tuple in Python?
slice_tuple = (0, 1, 2, 3, 4, 5, 6)
print("Slice from index 2 to 5:", slice_tuple[2:6])
print("Slice with step 2:", slice_tuple[0:7:2])

# How do you count the occurrences of a specific value in a tuple?
count_tuple = (1, 2, 2, 3, 2, 4)
print("Occurrences of 2:", count_tuple.count(2))

# What are the advantages of using tuples over lists in Python?
advantages = (
    "1. Tuples are immutable, which makes them safer for fixed data.",
    "2. Tuples can be used as dictionary keys (when elements are hashable).",
    "3. Tuples can be slightly faster than lists for iteration and access.",
    "4. Immutability can help prevent accidental data modification."
)
for advantage in advantages:
    print(advantage)
