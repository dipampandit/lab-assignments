# Implement isascii() without using built-in function
s = "Hello"
res = True
for c in s:
    if ord(c) > 127:
        res = False
        break
print(res)
