# Move the last n characters of a string to the front using slicing.
s = "abcdef"
n = 2
res = s[-n:] + s[:-n]
print(res)
