# Implement center() without using built-in function
s = "hello"
width = 11
pad = width - len(s)
left = pad // 2
right = pad - left
res = " " * left + s + " " * right
print(res)
