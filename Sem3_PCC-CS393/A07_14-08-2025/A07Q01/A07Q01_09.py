# Implement isalpha() without using built-in function
s = "HelloWorld"
res = True
for c in s:
    if not ('a' <= c <= 'z' or 'A' <= c <= 'Z'):
        res = False
        break
print(res)
