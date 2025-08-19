# Implement upper() without using built-in function
s = "python"
res = ""
for c in s:
    if "a" <= c <= "z":
        res += chr(ord(c) - 32)
    else:
        res += c
print(res)
