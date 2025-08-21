# String Explosion Problem
# Prompt: Take a string like "Code" and return "CCoCodCode"

def string_explosion(s):
    result = ""
    for i in range(len(s)):
        result += s[:i+1]
    return result

print(string_explosion("Code"))   # CCoCodCode
