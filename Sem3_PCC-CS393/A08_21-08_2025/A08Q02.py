# Count "hi" Problem
# Prompt: Return the number of times substring "hi" appears in string.

def count_hi(s):
    count = 0
    for i in range(len(s) - 1):
        if s[i] == "h" and s[i+1] == "i":
            count += 1
    return count

# Examples
print(count_hi("abc hi ho"))   # 1
print(count_hi("ABChi hi"))    # 2
print(count_hi("hihi"))        # 2
