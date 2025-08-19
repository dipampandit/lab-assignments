# Implement rjust() without using built-in function
s = "hello"
width = 10
res = " " * (width - len(s)) + s
print(res)
