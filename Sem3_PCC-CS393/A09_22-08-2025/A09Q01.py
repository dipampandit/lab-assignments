"""
Q: Write a Python program to reverse a string and then print only the characters
   at even indices of the reversed string.
   Example: For "chandragupta", the result should be "atpurdn".
"""

s = "chandragupta"

reversed_str = ""
for i in range(len(s) - 1, -1, -1):
    reversed_str += s[i]

result = ""
for i in range(len(reversed_str)):
    if i % 2 == 0:
        result += reversed_str[i]

print(result.strip())
