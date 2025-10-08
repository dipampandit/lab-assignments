# Generate all permutations of a string
def permute(s, answer=""):
    if len(s) == 0:
        print(answer)
        return
    for i in range(len(s)):
        ch = s[i]
        left = s[:i] + s[i+1:]
        permute(left, answer + ch)

permute("abc")
