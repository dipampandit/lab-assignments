# Implement islower() without using built-in function
s = "hello"
res = len(s) > 0
for c in s:
    if 'A' <= c <= 'Z':
        res = False
        break
else:
    res = True
print(res)
