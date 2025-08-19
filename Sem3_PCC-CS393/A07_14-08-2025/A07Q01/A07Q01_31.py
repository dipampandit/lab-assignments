# Implement endswith() without using built-in function
s = "hello world"
suffix = "world"
res = s[-len(suffix):] == suffix
print(res)
