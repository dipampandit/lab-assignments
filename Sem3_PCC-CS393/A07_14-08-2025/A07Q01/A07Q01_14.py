# Implement isupper() without using built-in function
s = "HELLO"
res = len(s) > 0
for c in s:
    if 'a' <= c <= 'z':
        res = False
        break
else:
    res = True
print(res)
