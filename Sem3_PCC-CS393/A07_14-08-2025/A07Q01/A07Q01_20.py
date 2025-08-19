# Implement replace() without using built-in function
s = "banana"
old = "na"
new = "xy"
res = ""
i = 0
while i < len(s):
    if s[i:i+len(old)] == old:
        res += new
        i += len(old)
    else:
        res += s[i]
        i += 1
print(res)
