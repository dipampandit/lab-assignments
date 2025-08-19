# Implement partition() without using built-in function
s = "hello=world"
sep = "="
idx = -1
for i in range(len(s)):
    if s[i:i+len(sep)] == sep:
        idx = i
        break
if idx != -1:
    res = (s[:idx], sep, s[idx+len(sep):])
else:
    res = (s, "", "")
print(res)
