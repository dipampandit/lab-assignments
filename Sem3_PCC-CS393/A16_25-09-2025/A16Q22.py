# Count the occurrences of a character in a string
def count_char(s, c):
    if s == "":
        return 0
    count = 1 if s[0] == c else 0
    return count + count_char(s[1:], c)

print(count_char("hello world", "l"))
