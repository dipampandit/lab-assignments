# Implement maketrans() without using built-in function
frm = "abc"
to = "123"
trans = {}
for i in range(len(frm)):
    trans[frm[i]] = to[i]
print(trans)
