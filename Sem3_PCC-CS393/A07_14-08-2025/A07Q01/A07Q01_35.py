# Implement title() without using built-in function
s = "python programming language"
res = ""
capitalize_next = True
for c in s:
    if c == " ":
        res += c
        capitalize_next = True
    elif capitalize_next:
        if "a" <= c <= "z":
            res += chr(ord(c) - 32)
        else:
            res += c
        capitalize_next = False
    else:
        if "A" <= c <= "Z":
            res += chr(ord(c) + 32)
        else:
            res += c
print(res)
