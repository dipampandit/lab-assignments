# Implement count() without using built-in function
s = "banana"
ch = "a"
cnt = 0
for c in s:
    if c == ch:
        cnt += 1
print("Count:", cnt)
