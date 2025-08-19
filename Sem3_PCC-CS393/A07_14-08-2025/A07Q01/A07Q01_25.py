# Implement lstrip() without using built-in function
s = "   hello   "
start = 0
while start < len(s) and s[start] == " ":
    start += 1
res = s[start:]
print(res)
