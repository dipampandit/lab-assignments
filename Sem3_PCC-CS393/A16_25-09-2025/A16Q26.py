# Question: Longest Substring Without Repeating Characters
# Problem Statement:
# Given a string s, find the length of the longest substring without repeating characters 
# and return the substring as well.

def longest_unique_substring(s):
    start = 0
    max_len = 0
    max_sub = ""
    seen = {}

    for i in range(len(s)):
        if s[i] in seen and seen[s[i]] >= start:
            start = seen[s[i]] + 1
        seen[s[i]] = i
        if i - start + 1 > max_len:
            max_len = i - start + 1
            max_sub = s[start:i + 1]

    return max_len, max_sub

s = input("Enter a string: ")
length, substring = longest_unique_substring(s)
print("Length of longest substring without repeating characters:", length)
print("Substring:", substring)
