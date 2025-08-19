# Implement split() without using built-in function
s = "one two three"
sep = " "
res = []
word = ""
for c in s:
    if c == sep:
        if word != "":
            res.append(word)
            word = ""
    else:
        word += c
if word != "":
    res.append(word)
print(res)
