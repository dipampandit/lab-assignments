# Implement lower() without using built-in function
s = "PYTHON"
res = ""
for c in s:
    if "A" <= c <= "Z":
        res += chr(ord(c) + 32)
    else:
        res += c
print(res)
