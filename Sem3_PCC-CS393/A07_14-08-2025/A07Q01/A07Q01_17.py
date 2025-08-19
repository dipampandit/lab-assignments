# Implement istitle() without using built-in function
s = "Hello World"
words = s.split(" ")
res = True
for w in words:
    if len(w) == 0:
        continue
    if not ('A' <= w[0] <= 'Z'):
        res = False
        break
    for c in w[1:]:
        if 'A' <= c <= 'Z':
            res = False
            break
print(res)
