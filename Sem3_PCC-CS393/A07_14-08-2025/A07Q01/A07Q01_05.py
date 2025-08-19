# Implement rfind() without using built-in function
s = "hello hello"
sub = "lo"
pos = -1
for i in range(len(s) - len(sub), -1, -1):
    if s[i:i+len(sub)] == sub:
        pos = i
        break
print("Last found at:", pos)
