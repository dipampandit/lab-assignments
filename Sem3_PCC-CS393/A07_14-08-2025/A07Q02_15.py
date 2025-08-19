# Slice a string to reverse only its last half using negative slicing.
s = "abcdefgh"
half = len(s) // 2
res = s[:half] + s[:half-1:-1]
print(res)
