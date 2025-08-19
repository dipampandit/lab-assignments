# Implement rstrip() without using built-in function
s = "   hello   "
end = len(s) - 1
while end >= 0 and s[end] == " ":
    end -= 1
res = s[:end+1]
print(res)
