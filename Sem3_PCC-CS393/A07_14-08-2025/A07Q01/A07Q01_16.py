# Implement isspace() without using built-in function
s = "  "
res = len(s) > 0
for c in s:
    if c != ' ' and c != '\t' and c != '\n':
        res = False
        break
print(res)
