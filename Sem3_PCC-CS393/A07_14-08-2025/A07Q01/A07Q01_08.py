# Implement isalnum() without using built-in function
s = "Hello123"
res = True
for c in s:
    if not ('a' <= c <= 'z' or 'A' <= c <= 'Z' or '0' <= c <= '9'):
        res = False
        break
print(res)
