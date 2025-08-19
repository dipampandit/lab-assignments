# Implement rindex() without using built-in function
s = "hello hello"
sub = "lo"
pos = -1
for i in range(len(s) - len(sub), -1, -1):
    if s[i:i+len(sub)] == sub:
        pos = i
        break
if pos == -1:
    raise ValueError("Substring not found")
print("Last index:", pos)
