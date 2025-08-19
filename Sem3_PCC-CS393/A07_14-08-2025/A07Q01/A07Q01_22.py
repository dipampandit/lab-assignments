# Implement ljust() without using built-in function
s = "hello"
width = 10
res = s + " " * (width - len(s))
print(res)
