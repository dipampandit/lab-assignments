# Implement splitlines() without using built-in function
s = "hello\nworld\npython"
res = []
line = ""
for c in s:
    if c == "\n":
        res.append(line)
        line = ""
    else:
        line += c
if line != "":
    res.append(line)
print(res)
