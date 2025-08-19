# Implement join() without using built-in function
sep = "-"
lst = ["a", "b", "c"]
res = ""
for i in range(len(lst)):
    res += lst[i]
    if i != len(lst) - 1:
        res += sep
print(res)
