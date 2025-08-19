# Implement startswith() without using built-in function
s = "hello world"
prefix = "hello"
res = s[:len(prefix)] == prefix
print(res)
