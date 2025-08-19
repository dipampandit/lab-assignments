# Implement isnumeric() without using built-in function
s = "12345"
res = len(s) > 0
for c in s:
    if not ('0' <= c <= '9'):
        res = False
        break
print(res)
