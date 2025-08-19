# Given a string and a number N, slice the string to move the first N characters to the end.
s = "abcdef"
N = 2
res = s[N:] + s[:N]
print(res)
