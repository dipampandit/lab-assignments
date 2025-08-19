# Implement len() without using built-in function
s = "hello"
count = 0
for _ in s:
    count += 1
print("Length:", count)
