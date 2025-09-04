"""
Q: Write a Python program to find all unique palindromic substrings of a given string.
   Example:
   Input: "ababa"
   Output: ['a', 'b', 'aba', 'bab', 'ababa']
"""

def find_palindromic_substrings(s):
    n = len(s)
    pal = set()
    
    for i in range(n):
        for j in range(i, n):
            sub = s[i:j + 1]
            if sub == sub[::-1]:
                pal.add(sub)
    
    res = []
    for i in range(n):
        for j in range(i, n):
            sub = s[i:j + 1]
            if sub in pal:
                res.append(sub)
                pal.remove(sub)
    return res

print(find_palindromic_substrings("ababa"))
