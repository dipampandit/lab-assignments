# Implement index() without using built-in function
s = "hello"
sub = "ll"
pos = -1
for i in range(len(s) - len(sub) + 1):
    if s[i:i+len(sub)] == sub:
        pos = i
        break
if pos == -1:
    raise ValueError("Substring not found")
print("Index:", pos)
