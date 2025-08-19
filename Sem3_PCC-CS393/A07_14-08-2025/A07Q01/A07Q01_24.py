# Implement strip() without using built-in function
s = "   hello   "
start = 0
end = len(s) - 1
while start < len(s) and s[start] == " ":
    start += 1
while end >= 0 and s[end] == " ":
    end -= 1
res = s[start:end+1]
print(res)
