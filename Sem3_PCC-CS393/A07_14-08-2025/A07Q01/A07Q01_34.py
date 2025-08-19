# Implement swapcase() without using built-in function
s = "PyThOn"
res = ""
for c in s:
    if "a" <= c <= "z":
        res += chr(ord(c) - 32)
    elif "A" <= c <= "Z":
        res += chr(ord(c) + 32)
    else:
        res += c
print(res)
