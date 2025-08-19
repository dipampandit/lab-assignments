# Implement expandtabs() without using built-in function
s = "a\tb\tc"
result = ""
for c in s:
    if c == "\t":
        result += " " * 8
    else:
        result += c
print(result)
