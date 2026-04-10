# Write a recursive solution for generating all permutations of a string.

def permutations(s, current=""):
    if len(s) == 0:
        print(current)
        return 1

    count = 0

    for i in range(len(s)):
        ch = s[i]
        remaining = s[:i] + s[i+1:]
        count += permutations(remaining, current + ch)

    return count

string = input("Enter a string: ")
total = permutations(string)
print("Total permutations: ", total)
