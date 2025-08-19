# Implement find() without using built-in function
s = "hello"
sub = "ll"
pos = -1
for i in range(len(s) - len(sub) + 1):
    if s[i:i+len(sub)] == sub:
        pos = i
        break
print("Found at:", pos)
