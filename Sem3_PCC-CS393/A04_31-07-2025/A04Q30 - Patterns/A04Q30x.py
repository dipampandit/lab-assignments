# Pattern:
#     A
#    B B
#   C C C
#  D D D D
# E E E E E

n = 5
for i in range(n):
    print(" " * (n - i - 1), end="")
    for j in range(i + 1):
        print(chr(65 + i), end="")
        if j != i:
            print(" ", end="")
    print()
