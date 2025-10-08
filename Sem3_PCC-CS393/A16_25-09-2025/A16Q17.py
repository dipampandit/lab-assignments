# Generate all subsets of a set
def subsets(s, current="", index=0):
    if index == len(s):
        print(current)
        return
    subsets(s, current, index + 1)
    subsets(s, current + s[index], index + 1)

subsets("abc")
