# Implement capitalize() without using built-in function
s = "python programming"
if len(s) > 0:
    res = s[0].upper() + s[1:].lower()
else:
    res = s
print(res)
